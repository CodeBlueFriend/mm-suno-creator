# mm-suno-creator

把歌曲创意整理成可执行、可检查、可迭代的 Suno 创作生成包。项目包含一个可独立安装的 Codex Skill、可查询标签种子库，以及零第三方 Python 依赖的命令行工具。

> 当前版本：`v0.1.0` · 状态：可运行 MVP · 默认本地执行

## 产品能力一览

| 用户输入 | 产品能力 | 直接输出 |
|---|---|---|
| 一句话创意、故事或情绪 | 建立主题、人声、语言、时长、Hook 与禁止项完整简报 | 可执行创作方向 |
| 中文、英文或双语歌词需求 | 设计段落、检查可唱性、重复、句长与演唱时长 | 可粘贴的结构化歌词 |
| 模糊曲风描述 | 装配主曲风、辅轴、律动、人声、乐器、制作与情绪标签 | 精简版和标准版 Style |
| 标签名称或使用场景 | 查询中英文别名、听感、适配、冲突与证据等级 | 标签解释和组合建议 |
| 已写好的 Style | 检查长度预算、重复、已知冲突与曲风堆叠 | 结构化 Lint 结果 |
| 第一轮生成反馈 | 保留稳定版本并定位最高影响变量 | 下一轮单变量修改方案 |

完整交付包包含：**创作简报、歌词、两套 Style、Exclude、参数理由、时长预算、标签释义、风险提示和下一轮计划**。

## 设计思路

这个项目不把大量标签堆进一次提示词，而是把创作拆成“简报 → 结构 → 歌词 → Style 装配 → 参数建议 → 生成前审核 → 单变量迭代”的可复用流程。

核心原则：

- **主轴优先**：一个主曲风、有限辅轴，避免标签互相抵消；
- **先结构后歌词**：先确定段落功能与时长预算，再写可唱文本；
- **证据分级**：音乐术语、平台观察和未知支持状态分开呈现；
- **平台规则可替换**：不把会变化的 Suno 限制硬编码成永久事实；
- **权利边界清晰**：参考作品转换为音乐属性，不复刻旋律、歌词、声音或独特风格；
- **可控迭代**：每轮只修改一个高影响变量，保留稳定版本。

完整架构、数据流与阶段规划见 [设计说明](docs/DESIGN.md)。

## 当前可用工具

- 中文、英文和双语创作流程与结构检查；
- 标签精确/别名/语义场景查询；
- Style 长度、重复、已知冲突和曲风堆叠检查；
- 歌词段落、行数、重复与演唱时长启发式估算；
- 统一 Markdown 生成包；
- 明确区分音乐术语、平台观察和未知支持状态。

## 快速开始

```bash
cd skills/mm-suno-creator
python3 scripts/query_tags.py "凌晨 雨夜"
python3 scripts/lint_style_prompt.py "folk pop, warm baritone, acoustic guitar"
python3 scripts/build_generation_pack.py assets/example-input.json --output /tmp/song-pack.md
```

安装到 Codex：

```bash
cp -R skills/mm-suno-creator ~/.codex/skills/mm-suno-creator
```

然后在任务中使用 `$mm-suno-creator`。

典型请求：

```text
使用 $mm-suno-creator：写一首三分钟以内的中文民谣流行，
温暖男中低音，克制到爆发，副歌第一句要有记忆点，不要说唱。
```

当前词典是经过字段校验的 MVP 种子，不声称达到设计基线中的 1,500 个 A 级条目。平台控制和输入限制会变化，运行时应以当前官方界面/文档为准。

## 文档

- [设计说明](docs/DESIGN.md)
- [安装](docs/INSTALL.md)
- [使用指南](docs/USER_GUIDE.md)
- [开发与数据规则](docs/DEVELOPMENT.md)
- [隐私、来源与权利边界](docs/PRIVACY_AND_RIGHTS.md)
- [故障排除](docs/TROUBLESHOOTING.md)
- [版本记录](CHANGELOG.md)

## 版本范围

`v0.1.0` 已完成可安装 Skill、标签种子库、查询/校验/分析脚本、十段式生成包和测试。尚未完成设计目标中的 1,500 个 A 级标签、3,000 个别名和持续更新后台；版本记录会明确区分已交付、实验性与后续计划。

Copyright © 2026 CodeBlueFriend. All rights reserved.
