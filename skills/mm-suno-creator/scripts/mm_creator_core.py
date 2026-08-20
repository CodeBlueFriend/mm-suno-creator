#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
TAGS_PATH = ROOT / "assets" / "tags.json"
SECTION_RE = re.compile(r"^\s*\[([^\]]+)\]\s*$")
WORD_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
CJK_RE = re.compile(r"[\u3400-\u9fff]")


def load_tags() -> list[dict[str, Any]]:
    return json.loads(TAGS_PATH.read_text(encoding="utf-8"))


def normalize(value: str) -> str:
    return re.sub(r"[\s_-]+", " ", value.casefold()).strip()


def query_tags(query: str, limit: int = 8) -> list[dict[str, Any]]:
    q = normalize(query)
    q_tokens = set(q.split())
    ranked: list[tuple[float, dict[str, Any]]] = []
    for tag in load_tags():
        names = [tag["canonical_en"], tag["name_zh_cn"], *tag.get("aliases", [])]
        normalized = [normalize(item) for item in names]
        score = 0.0
        if q in normalized:
            score = 100.0
        elif any(q and q in item for item in normalized):
            score = 70.0
        else:
            tokens = set(" ".join(normalized).split())
            overlap = len(tokens & q_tokens)
            score = 10.0 * overlap / max(1, len(q_tokens))
        haystack = normalize(" ".join(tag.get("best_for", [])))
        scene_overlap = len(set(haystack.split()) & q_tokens)
        if q and q in haystack:
            score += 20.0
        elif scene_overlap:
            score += 12.0 * scene_overlap / max(1, len(q_tokens))
        if score:
            ranked.append((score, tag))
    ranked.sort(key=lambda item: (-item[0], item[1]["id"]))
    return [{"score": score, **tag} for score, tag in ranked[:limit]]


def split_style(style: str) -> list[str]:
    return [item.strip() for item in re.split(r"[,;，；\n]+", style) if item.strip()]


def lint_style(style: str, max_chars: int = 1000) -> dict[str, Any]:
    items = split_style(style)
    normalized = [normalize(item) for item in items]
    warnings: list[dict[str, str]] = []
    seen: set[str] = set()
    for raw, item in zip(items, normalized):
        if item in seen:
            warnings.append({"code": "duplicate", "message": f"重复标签：{raw}"})
        seen.add(item)
    if len(style) > max_chars:
        warnings.append({"code": "length", "message": f"Style 为 {len(style)} 字符，超过项目预算 {max_chars}；请用已核验的平台限制覆盖该值。"})
    tags = load_tags()
    lookup = {normalize(name): tag for tag in tags for name in [tag["canonical_en"], tag["name_zh_cn"], *tag.get("aliases", [])]}
    selected = [lookup[item] for item in normalized if item in lookup]
    selected_names = {normalize(tag["canonical_en"]) for tag in selected}
    conflicts: set[tuple[str, str]] = set()
    for tag in selected:
        for other in tag.get("conflicts_with", []):
            if normalize(other) in selected_names:
                conflicts.add(tuple(sorted((tag["canonical_en"], other))))
    for left, right in sorted(conflicts):
        warnings.append({"code": "conflict", "message": f"已知冲突或强张力组合：{left} ↔ {right}"})
    genres = [tag["canonical_en"] for tag in selected if tag["category"] == "genre"]
    if len(genres) > 3:
        warnings.append({"code": "genre_overload", "message": "主/次曲风超过三项，执行焦点可能分散：" + ", ".join(genres)})
    return {"characters": len(style), "budget": max_chars, "items": items, "known_tags": [tag["id"] for tag in selected], "warnings": warnings, "ok": not warnings}


def english_syllables(word: str) -> int:
    word = re.sub(r"[^a-z]", "", word.casefold())
    if not word:
        return 0
    groups = re.findall(r"[aeiouy]+", word)
    count = len(groups)
    if word.endswith("e") and count > 1 and not word.endswith(("le", "ye")):
        count -= 1
    return max(1, count)


def analyze_lyrics(text: str) -> dict[str, Any]:
    sections: list[dict[str, Any]] = []
    current = {"name": "Unlabeled", "lines": []}
    for raw in text.splitlines():
        match = SECTION_RE.match(raw)
        if match:
            if current["lines"]:
                sections.append(current)
            current = {"name": match.group(1).strip(), "lines": []}
        elif raw.strip():
            current["lines"].append(raw.strip())
    if current["lines"]:
        sections.append(current)
    cjk = len(CJK_RE.findall(text))
    words = WORD_RE.findall(text)
    syllables = sum(english_syllables(word) for word in words)
    punctuation_pauses = len(re.findall(r"[,，;；:.。！？!?]", text))
    seconds = cjk / 2.8 + syllables / 2.5 + punctuation_pauses * 0.18
    if sections:
        seconds += max(0, len(sections) - 1) * 1.2
    repeated = []
    line_counts: dict[str, int] = {}
    for section in sections:
        for line in section["lines"]:
            key = normalize(line)
            line_counts[key] = line_counts.get(key, 0) + 1
    repeated = [{"line": line, "count": count} for line, count in line_counts.items() if count > 1]
    return {
        "sections": [{"name": section["name"], "line_count": len(section["lines"])} for section in sections],
        "line_count": sum(len(section["lines"]) for section in sections),
        "cjk_characters": cjk,
        "english_words": len(words),
        "estimated_english_syllables": syllables,
        "estimated_duration_sec": round(seconds, 1),
        "estimated_duration_range_sec": [round(seconds * 0.82, 1), round(seconds * 1.25, 1)],
        "repeated_lines": repeated,
        "note": "时长为文本启发式估算；旋律、停顿、器乐段和平台生成行为会改变结果。",
    }


def render_pack(data: dict[str, Any]) -> str:
    brief = data.get("brief", {})
    lyrics = data.get("lyrics", "")
    styles = data.get("styles", {})
    analysis = analyze_lyrics(lyrics)
    sections = [
        "# Suno 创作生成包",
        "## 1. 创作简报",
        *[f"- {key}: {value}" for key, value in brief.items()],
        "\n## 2. 可直接粘贴的歌词\n",
        lyrics.strip() or "（待补）",
        "\n## 3. 精简 Style\n",
        styles.get("concise", "（待补）"),
        "\n## 4. 标准 Style\n",
        styles.get("standard", "（待补）"),
        "\n## 5. Exclude 建议\n",
        data.get("exclude", "（无）"),
        "\n## 6. 参数建议与原因",
        *[f"- {key}: {value}" for key, value in data.get("parameters", {}).items()],
        "\n## 7. 时长与结构预算",
        f"- 歌词演唱估算：{analysis['estimated_duration_sec']} 秒，合理区间 {analysis['estimated_duration_range_sec'][0]}–{analysis['estimated_duration_range_sec'][1]} 秒。",
        *[f"- [{item['name']}]: {item['line_count']} 行" for item in analysis["sections"]],
        "\n## 8. 标签释义",
        *[f"- {item}" for item in data.get("tag_notes", ["请用 query_tags.py 核验关键标签。"])],
        "\n## 9. 风险检查",
        *[f"- {item}" for item in data.get("risks", ["核验咬字、音域、Style 冲突和参考风格边界。"])],
        "\n## 10. 下一轮单变量计划",
        data.get("next_iteration", "若第一轮偏离，先只改一个最高影响变量并保留稳定版本。"),
        "",
    ]
    return "\n".join(sections)
