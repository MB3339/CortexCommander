from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama3-8b-8192",
    api_key=os.getenv("GROQ_API_KEY")
)

__all__ = ["llm", "create_supervisor_chain", "create_supervisor_prompt"]

def create_supervisor_prompt():
    return ChatPromptTemplate.from_messages([
        ("system", """You are a supervisor managing a team of AI agents:
1. Researcher
2. Analyst
3. Writer

Your goal is to assign tasks in order, based on current state:
- Has research: {has_research}
- Has analysis: {has_analysis}
- Has final report: {has_report}

Reply only with: Researcher, Analyst, Writer, or done.
"""),
        ("human", "{task}")
    ])


def create_supervisor_chain():
    prompt = create_supervisor_prompt()
    return prompt | llm