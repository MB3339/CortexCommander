from core.prompts import llm
from core.state import SupervisorState
from core.prompts import create_supervisor_prompt
from langchain_core.messages import AIMessage,HumanMessage
from typing import Dict
from core.prompts import create_supervisor_chain


def supervisor_agent(state: SupervisorState) -> Dict:
    """Supervisor_agent decides next agent using LLM."""
    
    messages = state["messages"]
    task = messages[-1].content if messages else "No task"

    # Determine current stage
    has_research = bool(state.get("research_data", ""))
    has_analysis = bool(state.get("analysis", ""))
    has_report = bool(state.get("final_report", ""))

    # Get decision from LLM
    chain = create_supervisor_chain()
    decision = chain.invoke({
        "task": task,
        "has_research": has_research,
        "has_analysis": has_analysis,
        "has_report": has_report
    })

    decision_text = decision.content.strip().lower()
    print(f"Supervisor Decision: {decision_text}")

    # Tighten up decision logic
    if decision_text in ["done", "end"] or (has_research and has_analysis and has_report):
        next_agent = "END"
        supervisor_msg = "Supervisor: All tasks are completed. Great job team!"

    elif decision_text == "researcher" or not has_research:
        next_agent = "researcher"
        supervisor_msg = "Supervisor: Researcher, please gather information on the topic."

    elif decision_text == "analyst" or (has_research and not has_analysis):
        next_agent = "analyst"
        supervisor_msg = "Supervisor: Analyst, please analyze the research data."

    elif decision_text == "writer" or (has_analysis and not has_report):
        next_agent = "writer"
        supervisor_msg = "Supervisor: Writer, please prepare the final report."

    else:
        next_agent = "supervisor"
        supervisor_msg = "Supervisor: Re-evaluating... no valid task decision."

    return {
        "messages": messages + [AIMessage(content=supervisor_msg)],
        "next_agent": next_agent,
        "current_task": task
    }

