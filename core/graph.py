from langgraph.graph import StateGraph, END
from core.state import SupervisorState
from agents import supervisor_agent, researcher_agent, analyst_agent, writer_agent

def router(state: SupervisorState):
    if state.get("task_complete"):
        return END
    return state.get("next_agent", "supervisor").lower()

def build_graph():
    builder = StateGraph(SupervisorState)

    builder.add_node("supervisor", supervisor_agent)
    builder.add_node("researcher", researcher_agent)
    builder.add_node("analyst", analyst_agent)
    builder.add_node("writer", writer_agent)

    builder.set_entry_point("supervisor")

    for node in ["supervisor", "researcher", "analyst", "writer"]:
        builder.add_conditional_edges(node, router, {
            "supervisor": "supervisor",
            "researcher": "researcher",
            "analyst": "analyst",
            "writer": "writer",
            "END": END,
            "__end__": END  
        })

    return builder.compile()
