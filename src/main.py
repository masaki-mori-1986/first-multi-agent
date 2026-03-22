import os
import sys

from dotenv import load_dotenv

from crew import build_crew


load_dotenv()


def main() -> int:
    topic = " ".join(sys.argv[1:]).strip() or "ローカルLLMを使ったマルチエージェント開発"

    print(f"[INFO] Topic: {topic}")
    print(f"[INFO] OLLAMA_BASE_URL: {os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')}")
    print(f"[INFO] OLLAMA_MODEL: {os.getenv('OLLAMA_MODEL', 'qwen2.5:7b')}")

    crew = build_crew()

    try:
        result = crew.kickoff(inputs={"topic": topic})
    except Exception as exc:
        print("[ERROR] Crew execution failed.")
        print(f"[ERROR] {exc}")
        print("[HINT] 1) `ollama serve` が起動中か 2) 指定モデルが pull 済みか確認してください。")
        return 1

    print("\n===== Final Output =====\n")
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
