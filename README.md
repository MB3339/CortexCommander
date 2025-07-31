# CortexCommander
# Multi-Agent AI Workflow with LangGraph + Groq

This project implements a **supervised multi-agent system** using [LangGraph](https://python.langchain.com/docs/langgraph/), [LangChain](https://www.langchain.com/), and [Groq LLMs](https://console.groq.com/). The architecture simulates an AI team where a **Supervisor agent** coordinates three specialized roles:

-  **Researcher** – gathers data and key facts
-  **Analyst** – synthesizes insights from the research
-  **Writer** – generates a professional final report

Each agent operates independently but passes control back to the **Supervisor**, who determines the next step based on current state.

---

##  Features

-  **LLM-driven task delegation** using Groq's Llama3
-  **LangGraph conditional flow** for routing between agents
-  Stateful execution with shared `SupervisorState`
-  Final report generation with structured formatting
-  Auto-stops when task is complete

---

##  Stack

- **LangGraph** – for orchestrating agent workflow
- **LangChain** – for LLM chaining and messaging
- **Groq** – for fast Llama3 model inference
- **Python 3.10+**

---

##  Sample Output

```text
> Task: What are the benefits of MIRV technology in modern warfare?

Supervisor: Researcher, please gather information.
Researcher: [Provides in-depth MIRV research]
Supervisor: Analyst, please analyze the findings.
Analyst: [Summarizes insights, risks, and trends]
Supervisor: Writer, please prepare the final report.
Writer: [Returns full formatted executive report]
Supervisor: All tasks completed. Great job team!
