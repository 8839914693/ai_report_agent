from mcp.server.fastmcp  import FastMCP

mcp = FastMCP()

@mcp.tool()
def get_market_benchmarks(topic:str):
    return {
        "topic": topic,
        "sentiment_score": 0.75,
        "cost_index" : 1.50
    }


@mcp.tool()
def check_compliance_risks(topic:str):
    return {
        "topic": topic,
        "compliance_risk": "low",
        "risks": [
            "data privacy",
            "Ip leakage",
        ]
    }

if __name__ == "__main__":
    mcp.run()