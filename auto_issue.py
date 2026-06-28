#!/usr/bin/env python3
"""
PromptDrop 自动 Issue 发报脚本
- 每天自动发一条进展 issue（或更新已有 issue）
- 用 gh CLI（需先 gh auth login）
"""
import subprocess
import sys
import os
from pathlib import Path
from datetime import datetime

REPO = "snail2sky/promptdrop"
ROOT = Path(__file__).parent


def get_stats():
    """从本地 EVENTS.jsonl / ORDERS.jsonl 读统计"""
    events = []
    orders = []
    for fname, store in [("docs/EVENTS.jsonl", events), ("docs/ORDERS.jsonl", orders)]:
        f = ROOT / fname
        if f.exists():
            with open(f) as fp:
                for line in fp:
                    line = line.strip()
                    if line:
                        (events if store is events else orders).append(__import__('json').loads(line))
    return {
        "events": len(events),
        "orders": len(orders),
        "gmv": sum(o.get("price", 0) for o in orders),
        "skus": {o["sku"]: sum(1 for x in orders if x["sku"] == o["sku"]) for o in orders}
    }


def main():
    stats = get_stats()
    today = datetime.now().strftime("%Y-%m-%d")
    title = f"📊 每日数据报告 · {today}"
    body = f"""## {today} 自动数据报告

| 指标 | 数值 |
|------|------|
| 累计事件 | {stats['events']} |
| 累计订单 | {stats['orders']} |
| 累计 GMV | ¥{stats['gmv']} |
| 真实订单 | {stats['orders']} |

### 各 SKU 销量

""" + "\n".join([f"- **{k}**: {v} 件" for k, v in stats["skus"].items()]) + f"""

---

🌐 在线：https://rebound-annotated-fundamentals-providing.trycloudflare.com
📦 代码：https://github.com/snail2sky/promptdrop

> 本 issue 由 auto-issue.py 自动生成（每 24 小时）
"""
    # 写到临时文件
    tmp = Path("/tmp/pd_daily_report.md")
    tmp.write_text(body, encoding="utf-8")
    # 调用 gh
    r = subprocess.run(
        ["gh", "issue", "create", "--repo", REPO, "--title", title, "--body-file", str(tmp), "--label", "💰-sales"],
        capture_output=True, text=True
    )
    print(r.stdout)
    print(r.stderr, file=sys.stderr)
    if r.returncode != 0:
        sys.exit(r.returncode)
    print(f"✅ Issue 已发：{title}")


if __name__ == "__main__":
    main()