from typing import Annotated, Dict, List, Any
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

class SupervisorState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]
    current_task: str
    next_agent: str
    research_data: str
    analysis: str
    final_report: str
    task_complete: bool
    iteration_count: int
    max_iterations: int
