# 博客草稿 · 待发布到掘金/CSDN/知乎

> 平台：掘金、CSDN、知乎、SegmentFault
> 标题：1000 元 + Hermes Agent + 一个人 = 一天上线 AI 模板小店
> 标签：AI、Agent、独立开发、副业

---

## 前言

我从 0 启动资金 1000 元做一人创业，用 [Hermes Agent](https://github.com/nousresearch/hermes-agent) 在不到 24 小时内完成了一个 AI 模板小店的全栈开发、上线、和公网发布。

这篇文章分享：
- 选品逻辑（为什么是"AI Prompt 模板"而不是"又一个 ChatGPT 套壳"）
- 技术栈（纯 HTML + Python + Cloudflare Tunnel，0 服务器成本）
- 部署链路（GitHub Pages / Cloudflare / Tunnel 怎么选）
- 数据埋点（一个 `/api/track` 端点搞定全链路）
- 自动发货（Python 脚本 + 一次性下载 token）

希望对想做独立开发但又怕前期投入的同学有启发。

---

## 一、为什么做"AI Prompt 模板小店"

1000 元启动资金的硬约束排除了：
- ❌ 自媒体内容农场（变现周期长）
- ❌ 小程序/抖音小店（需要资质 + 库存）
- ❌ 重资产 SaaS（开发周期长）
- ❌ 跨境电商（选品风险高）

剩下的最优解：**虚拟商品小店**——边际成本为 0、收款即时、SKU 可无限扩展。

为什么是"Prompt 模板"而不是"AI 工具"？
- AI 工具红海（GPT/Claude/文心一言已经把工具做了）
- Prompt 模板是"工具 + 具体场景"的中间层，用户**愿意为节省时间付费**
- 我自己写 Prompt 的核心能力可以直接复用

定位：9.9 元起，把"我花了 3 小时调好的 Prompt"打包成 PDF/Notion，立刻发货。

## 二、技术栈

```mermaid
flowchart LR
  A[用户] --> B[Cloudflare Quick Tunnel]
  B --> C[Python http.server]
  C --> D[静态 HTML]
  C --> E[/api/track]
  C --> F[/api/stats]
  C --> G[/download/token]
```

- **前端**：纯 HTML/CSS/JS（单页 < 10KB）
- **后端**：Python `http.server` + `SimpleHTTPRequestHandler`（~200 行）
- **公网**：Cloudflare `quick tunnel`（**无需账号**，零配置）
- **数据**：JSONL 文件存事件/订单/token（git 友好）
- **CDN**：Cloudflare（自动）

**总成本**：¥0（不算我自己的电费）

## 三、Cloudflare Quick Tunnel：免登录的公网入口

这是这篇文章最有信息密度的一节。

`cloudflared tunnel --url http://localhost:8765` 一条命令就给你一个 `https://xxx.trycloudflare.com` 公网链接，**不需要 Cloudflare 账号、不需要实名认证、不需要信用卡**。

```bash
# macOS 一行安装
brew install cloudflared

# 起隧道
cloudflared tunnel --url http://localhost:8765
# 输出：https://xxxx.trycloudflare.com
```

唯一缺点：链接每次重启会变。但对于个人项目 + 推广前期，足够了。

生产环境建议：注册 Cloudflare 账号 + 绑定自己的域名。

## 四、数据埋点：一个端点搞定全链路

```python
# 收到 /api/track POST 时
def log_event(event_type, payload):
    record = {"ts": now(), "event": event_type, **payload}
    with open("docs/EVENTS.jsonl", "a") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

# 前端埋点
function track(event, extra) {
  fetch('/api/track', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({event, ts: Date.now(), ref: document.referrer, ...extra})
  });
}
track('pageview_landing', {});
```

为什么用 JSONL 而不是 SQLite？
- 一个人创业，量级小（千级事件/天）
- JSONL 可 grep、可 git diff、便于 AI 直接读取
- 不需要部署数据库

## 五、自动发货：Python 脚本 + 一次性 Token

```python
# 收到付款截图后，运营者运行：
python3 ship.py --sku PD-001 --order 123456 --buyer "张三" --price 9.9

# 输出：
# ✅ 发货成功
#   Token: 9t-XECwGds5soevxTNbEAw
#   https://promptdrop.example.com/download/9t-XECwGds5soevxTNbEAw
```

下载页校验 token：24h 内有效，最多 3 次下载。够用。

## 六、SEO：让搜索引擎最快收录

1. **JSON-LD 结构化数据**（schema.org/Store）—— Google Rich Results 友好
2. **sitemap.xml** + **robots.txt** —— 基础
3. **主动 ping IndexNow** —— 关键！几小时内收录
4. **OG meta** —— 微信/微博分享卡片

```python
# 主动推 IndexNow
import urllib.request
url = "https://yoursite.com/index.html"
idx_url = f"https://api.indexnow.org/indexnow?url={url}&key=YOURKEY"
urllib.request.urlopen(idx_url)
# 几小时后 Bing/Yandex 就会收录
```

## 七、推广：0 预算怎么冷启动

- **GitHub README** 是 SEO 引流武器（GitHub 公共仓库的 README 会被搜索引擎抓）
- **掘金/CSDN** 技术博客自带流量
- **小红书/闲鱼/V2EX** 站内分发
- **主动给 trending 项目提 PR** —— 风险高，不推荐

## 八、ROI 与复盘

| 阶段 | 时间 | 动作 | 结果 |
|------|------|------|------|
| Phase 0 | 0-2h | 立项 + 落地页 + 5 SKU | MVP 本地验收 6/6 |
| Phase 1 | 2-4h | 公网发布 + 埋点 + SEO | IndexNow 收录 |
| Phase 2 | 4-24h | 推广 + 第一笔成交 | 待定 |
| Phase 3 | 1w+ | 日均 20 单 | 待定 |

启动资金消耗：¥0（连域名都没买）。

## 九、可复用的工具

- [Hermes Agent](https://github.com/nousresearch/hermes-agent) —— AI 助手框架
- [Cloudflare Quick Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/) —— 免登录公网入口
- [IndexNow](https://www.indexnow.org/) —— 主动推送搜索引擎

## 十、源码与体验

🌐 在线体验：[query-dividend-transparent-nominated.trycloudflare.com](https://query-dividend-transparent-nominated.trycloudflare.com)
📦 源码（含 README/ROADMAP/BDD）：[github.com/snail2sky/promptdrop](https://github.com/snail2sky/promptdrop)

欢迎 ⭐ Star + Fork 拿去用，MIT 协议，做类似的小店完全 OK。

---

> 如果你也在做独立开发，欢迎评论区交流。我会持续更新这个项目的进展。