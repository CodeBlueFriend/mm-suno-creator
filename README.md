# mm-suno-creator

把歌曲创意整理成可执行、可检查、可迭代的 Suno 创作生成包。项目包含一个可独立安装的 Codex Skill、可查询标签种子库，以及零第三方 Python 依赖的命令行工具。

## 当前能力

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

当前词典是经过字段校验的 MVP 种子，不声称达到设计基线中的 1,500 个 A 级条目。平台控制和输入限制会变化，运行时应以当前官方界面/文档为准。

## 文档

- [安装](docs/INSTALL.md)
- [使用指南](docs/USER_GUIDE.md)
- [开发与数据规则](docs/DEVELOPMENT.md)
- [隐私、来源与权利边界](docs/PRIVACY_AND_RIGHTS.md)
- [故障排除](docs/TROUBLESHOOTING.md)

Copyright © 2026 CodeBlueFriend. All rights reserved.
