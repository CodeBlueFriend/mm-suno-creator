# 使用指南

## 完整创作

提供主题、语言、主要曲风、情绪弧、人声、目标时长、Hook、使用场景和禁止项。缺省项会采用可逆默认值。完整输出包含简报、歌词、两套 Style、Exclude、参数理由、时长预算、标签释义、风险与下一轮单变量计划。

## 词典查询

在 Skill 目录运行 `python3 scripts/query_tags.py "dream pop"`。结果中的证据等级描述知识来源强度，不保证平台每次执行。

## Style 校验

运行 `python3 scripts/lint_style_prompt.py "..." --max-chars N`。`N` 应来自当前可见平台或官方文档；默认值只是项目预算。

## 歌词分析

使用 `[Verse]`、`[Chorus]` 等段落标记，然后运行 `python3 scripts/analyze_lyrics.py lyrics.txt`。时长范围用于结构规划，不是生成承诺。

## 失败后的迭代

保留稳定版本，每轮只改一个高影响变量，例如人声、主曲风、段落长度或 Weirdness 方向。不要同时重写歌词、曲风和参数，否则无法判断原因。
