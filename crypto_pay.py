#!/usr/bin/env python3
"""
PromptDrop 加密支付模块（v1 — demo）

原理：
- 用户选 SKU → 后台生成"订单"（订单号 + 金额）
- 用户用任何加密钱包（MetaMask、OKX、imToken）向商家地址转账
- 转账后用户提交 tx hash
- 后台人工/自动 verify → 触发发货

优点：
- ✅ 完全不需要实名
- ✅ 全球任何用户都能付
- ✅ 7×24 自动到账（区块链层面）
- ⚠️ 缺点：国内用户接受度低，但跨境用户/技术圈可用

商家收款地址（占位，实际需要替换成你的）：
USDT-TRC20: TXYZ...（Tron 网络，0 手续费）
USDT-ERC20: 0x...（以太坊主网，手续费高，不推荐）
BTC: bc1q...（比特币主网）
ETH: 0x...（以太坊主网）
"""
import os
import secrets
import json
import time
from pathlib import Path
from datetime import datetime


# 占位地址（实际部署替换成你的）
MERCHANT_WALLETS = {
    "USDT-TRC20": "TXxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  # Tron
    "BTC": "bc1qxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  # Bitcoin
    "ETH": "0xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",   # Ethereum mainnet
}

ORDERS_FILE = Path(__file__).parent / "docs" / "CRYPTO_ORDERS.jsonl"


def create_crypto_order(sku, price_cny, crypto="USDT-TRC20"):
    """创建加密货币订单"""
    order_id = str(int(time.time()))[-6:]
    order = {
        "order_id": order_id,
        "sku": sku,
        "price_cny": price_cny,
        "crypto": crypto,
        "wallet": MERCHANT_WALLETS.get(crypto, "unknown"),
        "status": "pending",
        "created_at": datetime.now().isoformat(),
        "tx_hash": None,
        "buyer_contact": None,
    }
    with open(ORDERS_FILE, "a") as f:
        f.write(json.dumps(order, ensure_ascii=False) + "\n")
    return order


def verify_tx_hash(tx_hash, expected_wallet):
    """
    验证 tx hash（v1: 占位，实际应该调用区块浏览器 API）
    真实实现：用 https://api.trongrid.io 或 https://blockchain.info 等
    """
    # TODO: 真实实现需要调用区块链浏览器 API
    # 这里返回占位成功
    return {
        "verified": True,
        "tx_hash": tx_hash,
        "to": expected_wallet,
        "amount": "N/A (待接入区块链 API)",
        "confirmations": "N/A (待接入)",
        "note": "v1 demo：未真实验证，需要接入 Trongrid / Etherscan API"
    }


if __name__ == "__main__":
    # 自测
    o = create_crypto_order("PD-001", 9.9, "USDT-TRC20")
    print(json.dumps(o, ensure_ascii=False, indent=2))