#!/usr/bin/env python3
"""
PromptDrop 自动发货脚本（v1 — 半自动）

使用流程：
1. 用户扫码付款（微信/支付宝）
2. 用户截图发到客服微信
3. 你（运营者）收到截图后，运行本脚本：
   python3 ship.py --sku PD-001 --order 123456 --buyer "张三"
4. 脚本自动：
   - 生成一个一次性下载链接（带 token + 24h 过期）
   - 把链接打印到终端
   - 你复制链接 → 微信发给买家
5. 同时记录到 docs/DAILY.md

未来升级方向：
- 接微信机器人自动发货（itchat / wechaty）
- 接 webhook → 支付宝到账通知 → 自动发货
"""
import argparse
import secrets
import json
from datetime import datetime, timedelta
from pathlib import Path


SKU_DIR = Path(__file__).parent / "prompts"
ORDERS_LOG = Path(__file__).parent / "docs" / "ORDERS.jsonl"
TOKENS_FILE = Path(__file__).parent / "docs" / "TOKENS.jsonl"


def generate_token(sku: str, order_id: str, buyer: str) -> str:
    """生成一次性下载 token"""
    token = secrets.token_urlsafe(16)
    expires = (datetime.now() + timedelta(hours=24)).isoformat()
    record = {
        "token": token,
        "sku": sku,
        "order_id": order_id,
        "buyer": buyer,
        "issued_at": datetime.now().isoformat(),
        "expires_at": expires,
        "downloaded": False,
        "redeemed_at": None
    }
    TOKENS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(TOKENS_FILE, "a") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    return token


def log_order(sku: str, order_id: str, buyer: str, price: float, token: str):
    """记录成交订单"""
    ORDERS_LOG.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "ts": datetime.now().isoformat(),
        "sku": sku,
        "order_id": order_id,
        "buyer": buyer,
        "price": price,
        "token": token,
        "status": "shipped"
    }
    with open(ORDERS_LOG, "a") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def main():
    parser = argparse.ArgumentParser(description="PromptDrop 自动发货")
    parser.add_argument("--sku", required=True, help="SKU 编号，如 PD-001")
    parser.add_argument("--order", required=True, help="订单号（时间戳后6位）")
    parser.add_argument("--buyer", required=True, help="买家称呼")
    parser.add_argument("--price", type=float, default=9.9, help="成交价格")
    args = parser.parse_args()

    # 找 SKU 文件
    sku_files = list(SKU_DIR.glob(f"{args.sku.lower()}-*.md"))
    if not sku_files:
        print(f"❌ 没找到 SKU {args.sku} 对应的内容文件")
        print(f"   期望路径: {SKU_DIR}/{args.sku.lower()}-*.md")
        return 1

    sku_file = sku_files[0]
    token = generate_token(args.sku, args.order, args.buyer)
    log_order(args.sku, args.order, args.buyer, args.price, token)

    print("=" * 60)
    print(f"✅ 发货成功")
    print(f"=" * 60)
    print(f"  SKU:     {args.sku}")
    print(f"  文件:    {sku_file.name}")
    print(f"  买家:    {args.buyer}")
    print(f"  金额:    ¥{args.price}")
    print(f"  订单号:  {args.order}")
    print(f"  Token:   {token}")
    print(f"  过期:    24h 内有效")
    print()
    print(f"  📤 微信发给买家的话术：")
    print(f"  ─────────────────────")
    print(f"  {args.buyer} 你好，感谢支持 PromptDrop！")
    print(f"  你的订单 {args.order} 已发货，下载链接：")
    print(f"  https://promptdrop.example.com/download/{token}")
    print(f"  链接 24 小时内有效，可重复下载。")
    print(f"  使用过程中有任何问题随时找我，祝使用愉快！")
    print(f"  ─────────────────────")
    print()
    print(f"  📝 已记录到 docs/ORDERS.jsonl")
    return 0


if __name__ == "__main__":
    exit(main())