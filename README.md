# study

学习资料与练习代码，使用 [uv](https://docs.astral.sh/uv/) 管理 Python 环境与依赖。

## 结构

```
src/study/ai/   AI 相关学习代码
tests/          测试
```

## 使用

```bash
uv sync          # 创建 .venv 并安装依赖
uv run pytest    # 运行测试
uv add <pkg>     # 添加依赖
```
