from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from core.graph import build_graph
import os

load_dotenv()  # Load your GROQ_API_KEY from .env

def main():
    graph = build_graph()

    user_task = "What are the strategic implications of MIRV systems in international defense policy?"

    initial_state = {
        "messages": [HumanMessage(content=user_task)],
        "current_task": user_task,
        "next_agent": "supervisor",
        "research_data": "",
        "analysis": "",
        "final_report": "",
        "task_complete": False,
        "iteration_count": 0,
        "max_iterations": 10
    }

    result = graph.invoke(initial_state)

    print("\n Final Messages:\n")
    for msg in result["messages"]:
        print(msg.content)

    print("\n  Final Report:\n")
    print(result.get("final_report", "[No report generated]"))

if __name__ == "__main__":
    main()
