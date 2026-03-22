import os

from crewai import Crew, LLM, Process
from dotenv import load_dotenv

from agents.researcher import build_researcher
from agents.writer import build_writer
from tasks.research_task import build_research_task
from tasks.writing_task import build_writing_task


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

    researcher = build_researcher(llm)
    writer = build_writer(llm)

    research_task = build_research_task(researcher)
    writing_task = build_writing_task(writer, research_task)

    return Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        process=Process.sequential,
        verbose=True,
    )
