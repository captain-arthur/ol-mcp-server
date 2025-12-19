import os
from fastmcp import FastMCP

SLACK_API_KEY = os.environ.get("SLACK_MCP_API_KEY", "my-super-secret")

config = {
    "mcpServers": {
        "slack": {
            "url": "http://127.0.0.1:3001/sse",
            "headers": {
                "Authorization": f"Bearer {SLACK_API_KEY}"
            },
            "timeout": 30000,
        }
    }
}

# FastMCP Proxy 생성
proxy = FastMCP.as_proxy(
    config,
    name="ol-mcp-proxy"
)

if __name__ == "__main__":
    # 🔥 핵심: HTTP(Remote MCP)로 실행
    proxy.run(
        transport="sse",   # 또는 "streamable-http"
        host="0.0.0.0",
        port=3333
    )