#!/usr/bin/env python3
"""
PromptDrop 本地试运行服务器
- 端口 8765（避免和常用端口冲突）
- 仅服务 public/ 目录
- 健康检查端点 /health
"""
import http.server
import socketserver
import os
import sys
import json
from pathlib import Path

ROOT = Path(__file__).parent / "public"
PORT = int(os.environ.get("PORT", 8765))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "status": "ok",
                "service": "PromptDrop",
                "port": PORT
            }).encode())
            return
        return super().do_GET()

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {format % args}", file=sys.stderr)


if __name__ == "__main__":
    print(f"🚀 PromptDrop server starting on http://localhost:{PORT}")
    print(f"   Health: http://localhost:{PORT}/health")
    print(f"   Landing: http://localhost:{PORT}/index.html")
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()