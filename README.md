# Agno Agentic Demo

An agentic application built on [Agno](https://github.com/agno-agi/agno) that pairs a Mistral-powered agent with a custom MCP server to deliver Italian-language tech analysis. The agent fetches Hacker News stories, classifies their topic, enriches context from Wikipedia, and retrieves live stock quotes from Yahoo Finance — all orchestrated through a single workflow.

## Features

- **Agent orchestration** — a single Agno agent drives the workflow, selects tools, and reasons over their outputs.
- **Custom MCP server** — exposes `classify_topic` and `get_live_stock` over the streamable-HTTP transport.
- **Live market data** — natural-language stock requests are parsed by the model, the ticker is extracted, and the quote is resolved through `yfinance`.
- **Context enrichment** — on-demand Wikipedia lookups widen topic coverage.
- **Persistent memory** — conversation history is stored in SQLite, keeping continuity across runs.

## Architecture

```text
   Hacker News ──┐
                 │
   Wikipedia ────┼──▶  Agno Agent  ──▶  Italian briefing / answer
                 │           ▲
   MCP Server ───┘           │
   ├─ classify_topic ────────┘
   └─ get_live_stock ──▶ yfinance ──▶ live market data
```

## Project Structure

```text
.
├── agent.py            # Agno agent entrypoint
├── mcp_server.py       # FastMCP server (classify_topic, get_live_stock)
├── requirements.txt    # Python dependencies
└── README.md
```

## Stack

| Component | Role |
|-----------|------|
| `agno.Agent` | Orchestration and reasoning loop |
| `MistralChat("mistral-small-latest")` | LLM backend |
| `HackerNewsTools` | News retrieval |
| `WikipediaTools` | Context enrichment |
| `MCPTools` | MCP client (streamable-HTTP) |
| `FastMCP` | MCP server runtime |
| `yfinance` | Live market quotes |
| `SqliteDb` | Conversation persistence (`tmp/agno_demo.db`) |

## Prerequisites

- Python 3.10 or newer
- A valid `MISTRAL_API_KEY` available in the environment

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdir -p tmp
export MISTRAL_API_KEY="your-key-here"
```

## Usage

Start the MCP server in one terminal:

```bash
python mcp_server.py
```

The server listens on `http://localhost:8000/mcp` (streamable-HTTP transport).

In a second terminal, launch the agent:

```bash
python agent.py
```

The agent prompts for an input query and streams the response in Italian, invoking Hacker News, Wikipedia, and the MCP tools as needed.

## How Stock Detection Works

The agent's system instructions teach it to recognise natural-language stock requests, extract the ticker symbol (e.g. `AAPL`, `MSFT`, `TSLA`) directly from the prompt, and invoke `get_live_stock` with that symbol. There is no static mapping or fixed grammar: tool selection is driven by the model's reasoning over the user message and the tool descriptions exposed by the MCP server.

## MCP Tools

### `classify_topic(title: str) -> str`

Tags a headline into one of: `ai`, `web`, `security`, `business`, `hardware`, or `other`, based on a lightweight keyword match.

### `get_live_stock(stock: str) -> str`

Takes a ticker symbol and returns the current price and currency from Yahoo Finance via `yfinance`. Returns a clear error message when the ticker cannot be resolved.

## Suitable Starting Points For

- automated tech newsletters
- vertical research assistants
- monitoring and reporting workflows
- multi-tool agent experiments
- Agno + MCP portfolio demos

## Notes

The repository is intentionally compact: a small surface area that demonstrates agent orchestration, MCP interoperability, live information gathering, and persistent memory in an idiomatic Agno setup.
