# Agent 2 Analyst Agent
from core.prompts import llm
from core.state import SupervisorState
from core.prompts import create_supervisor_prompt
from langchain_core.messages import AIMessage,HumanMessage
from typing import Dict

def analyst_agent(state:SupervisorState) -> Dict:
    """Analyst agent analyzes the research data."""

    research_data = state.get("research_data","")
    task=state.get("current_task","")

    #Create analysis prompt
    analyst_agent_prompt=f""" As a Expert Analyst, analyze the research data and provide insights.

    Research data: {research_data}

    provide:
    1. Key insights and patterns
    2. Stratergic implications
    3. Risk and opportunities
    4. Recommendations
    
    focus on actionable insights related to: {task}"""

    # Get analysis from LLM
    analysis_response=llm.invoke([HumanMessage(content=analyst_agent_prompt)])
    analysis= analysis_response.content

    # create agent message
    agent_message=f'Analyst: I have completed the analysis.\n\n insights:\n{analysis[:400]}...'

    return {
        "messages": [AIMessage(content=agent_message)],
        "analysis": analysis,
        "next_agent": "supervisor"
    }


