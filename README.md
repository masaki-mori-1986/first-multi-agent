# first-multi-agent

CrewAI + Ollama を使った最小構成のマルチエージェント（`Researcher` + `Writer`）サンプルです。
タスクは `sequential` で実行され、Researcher の出力を Writer が引き継いで記事化します。

## 構成

- `src/agents/researcher.py`: Researcher エージェント定義
- `src/agents/writer.py`: Writer エージェント定義
- `src/tasks/research_task.py`: 調査タスク定義
- `src/tasks/writing_task.py`: 執筆タスク定義
- `src/crew.py`: Crew 構築処理
- `src/main.py`: エントリポイント
- `.env.example`: Ollama 接続設定サンプル
- `pyproject.toml` / `uv.lock`: `uv` による依存管理

## 前提

- macOS / Linux
- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- [Ollama](https://ollama.com/) インストール済み

## セットアップ

1. 環境変数ファイルを作成

```bash
cp .env.example .env
```

2. 依存関係をインストール

```bash
uv sync
```

3. Ollama サーバー起動（未起動の場合）

```bash
ollama serve
```

4. 推奨モデルを取得

```bash
ollama pull qwen2.5:7b
```

5. 接続確認

```bash
curl -sS http://localhost:11434/api/tags
```

## 実行

```bash
uv run python src/main.py "CrewAIとOllamaの仕組み"
```

トピックを省略するとデフォルト値で実行されます。

```bash
uv run python src/main.py
```

## .env 設定

`.env.example`:

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=qwen2.5:7b
```

## 補足

- CrewAI v1 系では Ollama 利用時に `litellm` が必要です。
- このプロジェクトでは `crewai[litellm]` を使用しています。
