# 开发与数据规则

标签数据位于 `skills/mm-suno-creator/assets/tags.json`。新增条目必须含规范 ID、中英文名称、分类、定义、听感、适用场景、组合、冲突、证据等级与核验日期。单次生成经验不得直接升级为稳定规则。

所有脚本必须保持结构化 JSON 输出，错误写入 stderr 并返回非零状态。不得把可变平台行为写成永久事实。新增依赖前记录许可证；当前运行时代码仅使用 Python 标准库。

运行测试：`python3 -m unittest discover -s tests -v`。验证 Skill：`python3 <skill-creator>/scripts/quick_validate.py skills/mm-suno-creator`。
