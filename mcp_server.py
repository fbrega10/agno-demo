from mcp.server.fastmcp import FastMCP

mcp = FastMCP("topic_classifier")


@mcp.tool()
def classify_topic(title: str) -> str:
    title = title.lower()

    topics = {
        "ai": ["ai", "llm", "gpt", "model", "neural", "transformer"],
        "web": ["web", "browser", "css", "javascript", "react"],
        "security": ["security", "hack", "vulnerability", "cve", "encrypt"],
        "business": ["startup", "funding", "acquisition", "ipo", "revenue"],
        "hardware": ["chip", "gpu", "hardware", "risc", "arm"],
    }

    for topic, keywords in topics.items():
        if any(word in keywords for word in title.split()):
            return topic
    return "other"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
