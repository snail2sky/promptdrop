#!/usr/bin/env python3
"""
PromptDrop 自动备份脚本
- 把 docs/ 下的关键数据备份到 GitHub
- 每天执行 1 次（建议通过 cron 跑）
"""
import subprocess
import os
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent
MSG = f"backup: orders/events/tokens @ {datetime.now().strftime('%Y-%m-%d %H:%M')}"


def main():
    os.chdir(ROOT)
    # 只备份 docs/ 数据，不备份代码（代码已经手动推过）
    subprocess.run(["git", "add", "docs/STATE.md", "docs/ORDERS.jsonl", "docs/TOKENS.jsonl", "docs/EVENTS.jsonl"], check=False)
    r = subprocess.run(["git", "-c", "user.email=ai@promptdrop.dev", "-c", "user.name=PromptDrop", "commit", "-m", MSG], capture_output=True, text=True)
    print(r.stdout)
    print(r.stderr)
    subprocess.run(["git", "push", "origin", "main"], check=False)
    print("✅ 备份完成")


if __name__ == "__main__":
    main()