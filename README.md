# Agno Agentic Demo 🚀

> A compact agentic app built with **Agno** that pulls live tech news, classifies topics through a custom **MCP** tool, enriches the context with **Wikipedia**, and turns everything into an Italian tech bulletin with serious AI-native energy. 🤖

## Why This Repo Is Cool ✨

This repository is a clean and concrete showcase of what a real **agentic** experience looks like:

- 🧠 an agent with a clear objective
- 🔧 external tools orchestrated in a single workflow
- 🌐 live data gathered during execution
- 🗂️ local memory with SQLite persistence
- 📰 a final output that is readable, useful, and shareable

This is not just a script that generates text. The model **acts**, uses tools, expands context, and assembles a final result through a modern and elegant pipeline.

## What It Does 🕹️

The application runs a super clean workflow:

1. fetches the top stories from Hacker News
2. classifies each title with `classify_topic`
3. explores the main topic with Wikipedia
4. generates an Italian tech bulletin in Markdown

The result is a small but sharp showcase of how **Agno** can turn an LLM demo into a real **agentic application**.

## Stack Nerd 💾

- `Agno Agent` as the central orchestrator
- `MistralChat("mistral-small-latest")` as the current model
- `HackerNewsTools` for the news feed
- `WikipediaTools` for context enrichment
- `MCPTools` to connect the custom MCP server
- `FastMCP` to expose the `classify_topic` tool
- `SqliteDb("tmp/agno_demo.db")` for local memory and history

## Architecture Vibes 🧩

```text
Hacker News ──┐
              ├──> Agno Agent ───> Italian Tech Bulletin
Wikipedia ────┤
              │
MCP Server ───┘
   classify_topic()
```

This demo has the feel of a modern agentic lab: compact, readable, extensible, and perfect for showing **tool use**, **multi-step reasoning**, and **real orchestration**.

## Repository Map 🗺️

```text
.
├── agent.py
├── mcp_server.py
├── requirements.txt
└── README.md
```

## Files At A Glance 📁

### `agent.py`

Defines the Agno agent, wires the tools together, and runs the full workflow.

### `mcp_server.py`

Exposes an MCP server with the custom `classify_topic` tool, useful for quickly tagging tech headlines into categories such as `ai`, `web`, `security`, `business`, and `hardware`.

### `requirements.txt`

Lists the dependencies required to run the demo.

## Quickstart ⚡

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdir -p tmp
```

## Run The Magic 🪄

Start the MCP server first:

```bash
python mcp_server.py
```

Then, in another terminal:

```bash
python agent.py
```

The agent runs the complete workflow and streams an Italian tech bulletin straight to the terminal with strong AI engineer dashboard vibes. 📡

## Why Agno Here Hits Different 🔥

With Agno, this repository packs several core agentic AI ideas into just a few files:

- agent orchestration
- external tool integration
- MCP interoperability
- live information gathering
- contextual enrichment
- persistent memory
- user-ready final synthesis

That is what makes the project interesting: it is small enough to understand quickly, yet rich enough to demonstrate the real potential of an **agent-first** application.

## Great Starting Point For 🚧

- automated tech newsletters
- vertical research assistants
- monitoring and reporting workflows
- MCP + Agno portfolio demos
- multi-tool agent experiments

## Final Take 👾

If you want a repository that immediately signals **Agentic AI** energy, this one lands the point: a small codebase, a clear idea, smart integrations, and a workflow that shows how **Agno** can turn a simple prompt into a real operational application.
