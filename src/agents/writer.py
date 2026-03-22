from crewai import Agent, LLM


def build_writer(llm: LLM) -> Agent:
    return Agent(
        role="Writer",
        goal="調査内容を読みやすい日本語記事に仕上げる",
        backstory="読み手視点で構成を整えるテクニカルライター。",
        llm=llm,
        verbose=True,
    )
