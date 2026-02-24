# Agentic Market Intelligence

An autonomous multi-agent system built with **CrewAI**, **Streamlit**. This tool orchestrates a team of AI agents to perform deep market research, audit technical repositories, and synthesize competitive strategy reports.

## Key Features

* **Multi-Agent Orchestration**: Specialized agents for research, technical auditing, and management.
* **Clean Streamlit UI**: A professional dashboard that filters out terminal logs to show only the final strategy report.
* **Rate-Limit Guardrails**: Integrated `max_rpm` settings to ensure stability on Free Tier API keys.

## Tech Stack

* **Framework**: [CrewAI](https://crewai.com)
* **Intelligence**: Groq (Llama 3.3) / Google Gemini 2.0
* **Search**: Serper Dev Tool
* **UI**: Streamlit

## Prerequisites

* [uv](https://github.com/astral-sh/uv) installed on your system.
* API Keys for **Serper**, **Groq**, or **Gemini**.

## Setup

1. **Clone the repository**:
```bash
git https://github.com/Kidus-Yoseph1/agentic-market-intelligence.git
cd agentic-market-intelligence

```


2. **Environment Variables**:
Create a `.env` file in the root directory:
```env
use the .env.examples as a template

```


3. **Install Dependencies**:
```bash
uv sync

```



## Running the App

To launch the Streamlit interface, simply run:

```bash
uv run streamlit run src/app.py

```

## The Crew

* **Researcher**: Scours the internet for the top 3 established competitors and 2 emerging "hidden gem" startups.
* **Auditor**: Analyzes technical signals and primary value propositions.
* **Manager**: Synthesizes all findings into a final, actionable strategy report.

---

### Project Structure

```text
├── config/
│   ├── agents.yaml      # Agent roles and goals
│   └── tasks.yaml       # Task descriptions and expected outputs
├── src/
│   ├── app.py           # Streamlit UI
│   ├── crew.py          # CrewAI Class & Agent logic
│   └── main.py          # Entry point and execution logic
├── pyproject.toml       # Managed by uv
└── .env                 # API Credentials

```