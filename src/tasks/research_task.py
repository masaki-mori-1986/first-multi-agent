from crewai import Agent, Task


def build_research_task(researcher: Agent) -> Task:
    return Task(
        description=(
            "トピック『{topic}』を調査し、次をまとめてください。\n"
            "1. 背景\n"
            "2. 重要ポイント3つ\n"
            "3. 初学者が理解しづらい点\n"
        ),
        expected_output="背景、重要ポイント3つ、注意点を含む300-500字の調査メモ",
        agent=researcher,
    )
