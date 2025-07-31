# Agent 1 Researcher Agent
from core.state import SupervisorState
from core.prompts import create_supervisor_prompt
from core.prompts import llm

from langchain_core.messages import AIMessage, HumanMessage
from typing import Dict

def researcher_agent(state:SupervisorState) -> Dict:
    """ Researcher agent uses Groq to gather information."""

    task=state.get("current_task", "research topic")

    # create a research prompt
    research_prompt=f"""As a Expert Researcher, your task is to gather information on the topic: {task}.

    Include:
    1. Key facts and Background information
    2. Current trends and developments
    3. Important statistics or data points
    4. Notable examples or case studies.

    Be concise but thorough in your research."""

    # Get research from LLM
    research_response= llm.invoke([HumanMessage(content=research_prompt)])
    research_data=research_response.content

    # Create agent message
    agent_message=f" Researcher: I have completed the research on {task}. Here are my findings:\n\n{research_data}"

    return {
        "messages":state['messages']+[AIMessage(content=agent_message)],
        "research_data": research_data,
        "next_agent":"supervisor",  # Route to supervisor for next steps
    }