import os

from crewai import Agent, Crew, LLM, Process, Task
from dotenv import load_dotenv


load_dotenv()


def build_llm() -> LLM:
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    model = os.getenv("OLLAMA_MODEL", "qwen2.5:7b")
    return LLM(
        model=f"ollama/{model}",
        base_url=base_url,
        api_base=base_url,
        temperature=0.2,
    )


def build_crew() -> Crew:
    llm = build_llm()

    researcher = Agent(
        role="Researcher",
        goal="与えられたトピックの要点を短時間で正確に整理する",
        backstory="調査要点の抽出が得意なリサーチャー。事実ベースで簡潔にまとめる。",
        llm=llm,
        verbose=True,
    )

    writer = Agent(
        role="Writer",
        goal="調査内容を読みやすい日本語記事に仕上げる",
        backstory="読み手視点で構成を整えるテクニカルライター。",
        llm=llm,
        verbose=True,
    )

    research_task = Task(
        description=(
            "トピック『{topic}』を調査し、次をまとめてください。\n"
            "1. 背景\n"
            "2. 重要ポイント3つ\n"
            "3. 初学者が理解しづらい点\n"
        ),
        expected_output="背景、重要ポイント3つ、注意点を含む300-500字の調査メモ",
        agent=researcher,
    )

    writing_task = Task(
        description=(
            "Researcherの調査結果をもとに、トピック『{topic}』の解説文を作成してください。\n"
            "見出し付きで、初心者でも理解できる構成にしてください。"
        ),
        expected_output="見出し付きの日本語解説記事（600-900字）",
        agent=writer,
        context=[research_task],
    )

    return Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        process=Process.sequential,
        verbose=True,
    )
