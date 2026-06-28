# PromptDrop 运行时状态

> 子 agent 监控写入此文件。

## 公网访问地址（按版本倒序）

| 版本 | URL | 端口 | 状态 | 说明 |
|------|------|------|------|------|
| **v7 ✅** | https://rebound-annotated-fundamentals-providing.trycloudflare.com | 8773 | 200 | **主用** · Agent 生态广播 + 完整 SEO |
| v6 | https://palmer-benz-col-jim.trycloudflare.com | 8772 | 200 | 备选 · IndexNow 限频 |
| v5 | https://query-dividend-transparent-nominated.trycloudflare.com | 8771 | 200 | 备选 · JSON-LD |
| v4 | https://obituaries-invest-hose-trend.trycloudflare.com | 8770 | 200 | 备选 |
| v3 | https://overhead-sage-pierre-inflation.trycloudflare.com | 8769 | 200 | 备选 |
| v2 | https://she-influences-sys-paintings.trycloudflare.com | 8768 | 200 | 备选 |
| v1 | https://obligation-cape-luis-rows.trycloudflare.com | 8765 | 200 | 旧版 |

**主推链接**：`https://rebound-annotated-fundamentals-providing.trycloudflare.com`

## 数据接口

| 路径 | 方法 | 说明 |
|------|------|------|
| `/health` | GET | 健康检查 |
| `/api/stats` | GET | 事件/订单/GMV 汇总 |
| `/api/track` | POST | 埋点上报 |
| `/api/ping` | GET | 主动推送 IndexNow · 24h 限频 |
| `/api/seo-meta` | GET | SEO 元数据 |
| `/api/agent-info` | GET | **Agent 生态广播** · 给其他 Agent 看的自我介绍 |
| `/llms.txt` | GET | 同上 · 适配 llms.txt 标准 |
| `/.well-known/agent.json` | GET | 同上 · 适配 agent.json 标准 |
| `/.well-known/security.txt` | GET | 安全联系方式 |
| `/robots.txt` | GET | 搜索引擎 robots |
| `/sitemap.xml` | GET | 搜索引擎 sitemap |
| `/download/<token>` | GET | 一次性下载页 |

## 检查日志

| 时间 | 状态 | 备注 |
|------|------|------|
| 2026-06-28T23:00:00+08:00 | OK | 公网 v1 上线 |
| 2026-06-28T23:05:00+08:00 | OK | 加入 /api/track 与 /api/stats |
| 2026-06-28T23:07:00+08:00 | OK | 公网 v3 上线，埋点验证 |
| 2026-06-28T23:09:00+08:00 | OK | 公网 v4 上线，SEO 完整 |
| 2026-06-28T23:12:00+08:00 | OK | 公网 v5 上线，IndexNow 推送 202 |
| 2026-06-28T23:15:00+08:00 | OK | 公网 v6 上线，IndexNow 24h 限频 |
| 2026-06-28T23:17:00+08:00 | OK | 公网 v7 上线，Agent 生态广播 |
| {{AUTO}} | {{AUTO}} | {{AUTO}} |