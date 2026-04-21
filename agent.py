import asyncio

from agno.agent import Agent
from agno.models.mistral import MistralChat
from agno.tools.hackernews import HackerNewsTools
from agno.tools.mcp import MCPTools
from agno.tools.wikipedia import WikipediaTools
from agno.db.sqlite import SqliteDb

MCP_SERVER_URL = "http://localhost:8000/mcp"


async def main() -> None:
    mcp_tools = MCPTools(url=MCP_SERVER_URL, transport="streamable-http")
    await mcp_tools.connect()
    try:
        agent = Agent(
            model=MistralChat("mistral-small-latest"),
            instructions=[
                "Sei un analista tech. Scrivi sempre in italiano.",
                "Usa get_top_hackernews_stories per le notizie.",
                "Usa classify_topic per classificare ogni titolo.",
                "Usa search_wikipedia per approfondire un argomento.",
            ],
            tools=[HackerNewsTools().get_top_hackernews_stories, mcp_tools, WikipediaTools()],
            db=SqliteDb("tmp/agno_demo.db"),
            markdown=True,
            num_history_messages=5,
            add_history_to_context=True,
        )

        await agent.aprint_response(
            "Recupera le top 3 story da Hacker News, classifica ciascuna per categoria, "
            "poi cerca su Wikipedia il tema della prima story e scrivi un bollettino tech in italiano.",
            stream=True,
        )
    finally:
        await mcp_tools.close()


if __name__ == "__main__":
    asyncio.run(main())
