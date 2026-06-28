#!/usr/bin/env python3
"""
PromptDrop NOWPayments 加密支付集成模块（v1 — 待激活）

接入步骤：
1. 邮箱注册 https://nowpayments.io/payment-tools/api （无需 KYC）
2. 在 dashboard 获取 API key
3. 把 API key 填到环境变量 NOWPAYMENTS_KEY
4. 重启 server.py

API 文档：https://documenter.getpostman.com/view/7907941/2s93JusNJt
"""
import os
import json
import time
import urllib.request
import urllib.error

NOWPAYMENTS_API_KEY = os.environ.get("NOWPAYMENTS_KEY", "")
NOWPAYMENTS_URL = "https://api.nowpayments.io/v1"


def is_configured():
    return bool(NOWPAYMENTS_API_KEY)


def api_request(path, data=None, method="GET"):
    """统一 NOWPayments API 调用"""
    url = f"{NOWPAYMENTS_URL}{path}"
    headers = {"x-api-key": NOWPAYMENTS_API_KEY} if NOWPAYMENTS_API_KEY else {}
    if data:
        data = json.dumps(data).encode()
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return {"ok": True, "data": json.loads(r.read())}
    except urllib.error.HTTPError as e:
        return {"ok": False, "error": f"HTTP {e.code}: {e.read().decode()}"}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def create_invoice(sku_id, price_cny, buyer_email=None):
    """创建加密货币支付 invoice"""
    if not is_configured():
        return {"ok": False, "error": "NOWPAYMENTS_KEY not set"}
    order_id = f"PD-{sku_id}-{int(time.time())}"
    payload = {
        "price_amount": price_cny,
        "price_currency": "cny",
        "order_id": order_id,
        "order_description": f"PromptDrop {sku_id}",
    }
    if buyer_email:
        # NOWPayments 支持 buyer_email 字段（部分版本）
        payload["buyer_email"] = buyer_email
    return api_request("/invoice", data=payload, method="POST")


def get_minimum_amount(currency="usdttrc20"):
    """查询指定币种的最低支付金额"""
    if not is_configured():
        return {"ok": False, "error": "NOWPAYMENTS_KEY not set"}
    return api_request(f"/min-amount?currency={currency}")


def verify_webhook(payload, signature):
    """验证 NOWPayments IPN 回调签名（v1: 占位，需 IPN secret key）"""
    # 真实实现：用 HMAC-SHA256 验证
    # 文档：https://documenter.getpostman.com/view/7907941/2s93JusNJt#af42a76d-3df3-4d6e-be54-1ad22e93ca8b
    return {"ok": True, "note": "verify not implemented in v1"}


def status():
    """返回当前集成状态"""
    return {
        "configured": is_configured(),
        "endpoint": NOWPAYMENTS_URL,
        "ready": is_configured(),
        "missing": ["NOWPAYMENTS_KEY"] if not is_configured() else []
    }


if __name__ == "__main__":
    print(json.dumps(status(), indent=2))