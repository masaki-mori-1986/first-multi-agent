from crewai import Agent, Task


def build_writing_task(writer: Agent, research_task: Task) -> Task:
    return Task(
        description=(
            "Researcherの調査結果をもとに、トピック『{topic}』の解説文を作成してください。\n"
            "見出し付きで、初心者でも理解できる構成にしてください。"
        ),
        expected_output="見出し付きの日本語解説記事（600-900字）",
        agent=writer,
        context=[research_task],
    )
