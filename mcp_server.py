from mcp.server.fastmcp import FastMCP
import yfinance as yf

mcp = FastMCP("topic_classifier")


@mcp.tool()
def classify_topic(title: str) -> str:
    """This function classifies a title based on its words

    Args:
        title (str): The title to be classified

    Returns:
        str: the corresponding topic
    """
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


@mcp.tool()
def get_live_stock(stock: str) -> str:
    """Retrieves the live stock price for a given ticker symbol.

    Args:
        stock (str): ticker symbol (e.g. AAPL, MSFT, TSLA)

    Returns:
        str: current price with currency, or error message if ticker not found
    """
    ticker = stock.upper().strip()
    try:
        info = yf.Ticker(ticker).fast_info
        price = info.last_price
        currency = info.currency
        if price is None:
            return f"No price data available for '{ticker}'. Check the ticker symbol."
        return f"{ticker}: {price:.2f} {currency}"
    except Exception as e:
        return f"Could not retrieve stock data for '{ticker}': {e}"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
