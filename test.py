#!/usr/bin/env python3
"""
PromptDrop 健康检查 + BDD 验收脚本
用法：python3 test.py
"""
import urllib.request
import urllib.error
import sys
import re
from pathlib import Path

BASE = "http://localhost:8765"

PASS = "\033[92m✅ PASS\033[0m"
FAIL = "\033[91m❌ FAIL\033[0m"
INFO = "\033[94mℹ️  INFO\033[0m"


def check(name, fn):
    try:
        result = fn()
        print(f"{PASS}  {name}: {result}")
        return True
    except AssertionError as e:
        print(f"{FAIL}  {name}: {e}")
        return False
    except Exception as e:
        print(f"{FAIL}  {name}: {type(e).__name__}: {e}")
        return False


def main():
    print("=" * 60)
    print("PromptDrop BDD 验收")
    print("=" * 60)

    all_pass = True

    # 1. 健康检查
    def t_health():
        with urllib.request.urlopen(f"{BASE}/health", timeout=5) as r:
            assert r.status == 200, f"status {r.status}"
            data = r.read().decode()
            assert "ok" in data, f"bad body: {data}"
            return "health endpoint 200"
    all_pass &= check("健康检查", t_health)

    # 2. 落地页可访问
    def t_landing():
        with urllib.request.urlopen(f"{BASE}/index.html", timeout=5) as r:
            assert r.status == 200
            html = r.read().decode()
            assert "PromptDrop" in html
            assert "立即购买" in html
            return "landing page OK"
    all_pass &= check("落地页可访问", t_landing)

    # 3. 5 个 SKU 都在
    def t_skus():
        with urllib.request.urlopen(f"{BASE}/index.html", timeout=5) as r:
            html = r.read().decode()
        skus = re.findall(r"PD-\d{3}", html)
        assert len(set(skus)) >= 3, f"only found {set(skus)}"
        return f"{len(set(skus))} SKUs visible"
    all_pass &= check("SKU 数量 ≥ 3", t_skus)

    # 4. 订单页可访问
    def t_order():
        url = f"{BASE}/order.html?id=PD-001&title=test&price=9.9"
        with urllib.request.urlopen(url, timeout=5) as r:
            assert r.status == 200
            html = r.read().decode()
            assert "订单确认" in html
            assert "客服" in html
            return "order page OK"
    all_pass &= check("订单页可访问", t_order)

    # 5. 移动端 viewport
    def t_mobile():
        with urllib.request.urlopen(f"{BASE}/index.html", timeout=5) as r:
            html = r.read().decode()
        assert "viewport" in html and "width=device-width" in html
        return "viewport meta present"
    all_pass &= check("移动端适配", t_mobile)

    # 6. 5 个 SKU 文件都存在
    def t_prompts():
        prompt_dir = Path(__file__).parent / "prompts"
        files = list(prompt_dir.glob("pd-*.md"))
        assert len(files) >= 5, f"only {len(files)} prompt files"
        return f"{len(files)} prompt files"
    all_pass &= check("SKU 文件齐全", t_prompts)

    print("=" * 60)
    if all_pass:
        print(f"{PASS}  全部通过，MVP 可发布")
        return 0
    else:
        print(f"{FAIL}  有失败项，先修复")
        return 1


if __name__ == "__main__":
    sys.exit(main())