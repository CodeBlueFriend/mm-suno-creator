import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "skills" / "mm-suno-creator" / "scripts"
sys.path.insert(0, str(SCRIPTS))
from mm_creator_core import analyze_lyrics, lint_style, query_tags, render_pack


class CreatorTests(unittest.TestCase):
    def test_alias_query(self):
        results = query_tags("木吉他")
        self.assertEqual(results[0]["id"], "instrument.acoustic-guitar")

    def test_lint_duplicate_and_conflict(self):
        result = lint_style("dream pop, dry close-miked drums, dream pop")
        codes = {item["code"] for item in result["warnings"]}
        self.assertIn("duplicate", codes)
        self.assertIn("conflict", codes)

    def test_lyrics_analysis(self):
        result = analyze_lyrics("[Verse]\n雨落在窗边\n[Chorus]\n回来吧\n回来吧")
        self.assertEqual(result["line_count"], 3)
        self.assertTrue(result["estimated_duration_sec"] > 0)
        self.assertEqual(result["repeated_lines"][0]["count"], 2)

    def test_pack_has_ten_sections(self):
        pack = render_pack({"brief": {"主题": "夜归"}, "lyrics": "[Verse]\n我回来了", "styles": {"concise": "folk pop", "standard": "folk pop, warm baritone"}})
        self.assertIn("## 10. 下一轮单变量计划", pack)


if __name__ == "__main__":
    unittest.main()
