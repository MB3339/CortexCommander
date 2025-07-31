# Agent 3: Writer Agent
from core.prompts import llm
from core.state import SupervisorState
from core.prompts import create_supervisor_prompt
from langchain_core.messages import AIMessage,HumanMessage
from typing import Dict
from datetime import datetime


def writer_agent(state: SupervisorState) -> Dict:
    """Writer agent that creates a final executive report based on research and analysis."""

    research_data = state.get("research_data", "")
    analysis = state.get("analysis", "")
    task = state.get("current_task", "the task")

    # Build the writing prompt
    writing_prompt = f"""As a professional writer, create an executive report based on:

Task: {task}
Research findings: {research_data[:1000]}
Analysis: {analysis[:1000]}

Ensure the report is clear, concise, and well-structured with:
1. Executive Summary
2. Key Findings
3. Analysis and Insights
4. Conclusion
5. Recommendations

Keep it professional and concise.
"""

    #  Call LLM to generate report
    response = llm.invoke([HumanMessage(content=writing_prompt)])
    report = response.content

    # Format final report
    final_report = f"""
FINAL REPORT
{'='*50}
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Topic: {task}
{'='*50}

{report}

{'='*50}
Report compiled by Multi-Agent AI system powered by Groq LLM.
"""

    return {
        "final_report": final_report,
        "messages": state["messages"] + [AIMessage(content="Writer: Report completed!\n\n" + final_report)],
        "next_agent": "supervisor",
        "task_complete": True
    }
