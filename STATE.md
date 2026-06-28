# PromptDrop 运行时状态

> 子 agent 监控写入此文件。

## 公网访问地址（按版本倒序）

| 版本 | URL | 端口 | 状态 | 说明 |
|------|------|------|------|------|
| **v6 ✅** | https://palmer-benz-col-jim.trycloudflare.com | 8772 | 200 | **主用** · IndexNow 24h 限频 + JSON-LD |
| v5 | https://query-dividend-transparent-nominated.trycloudflare.com | 8771 | 200 | 备选 |
| v4 | https://obituaries-invest-hose-trend.trycloudflare.com | 8770 | 200 | 备选 |
| v3 | https://overhead-sage-pierre-inflation.trycloudflare.com | 8769 | 200 | 备选 |
| v2 | https://she-influences-sys-paintings.trycloudflare.com | 8768 | 200 | 备选 |
| v1 | https://obligation-cape-luis-rows.trycloudflare.com | 8765 | 200 | 旧版 |

**主推链接**：`https://palmer-benz-col-jim.trycloudflare.com`

## 数据接口

- Health: `GET /health`
- Stats: `GET /api/stats`（事件/订单/GMV 汇总）
- Track: `POST /api/track`（埋点）
- Ping: `GET /api/ping`（主动推送 IndexNow · 24h 限频）
- SEO-Meta: `GET /api/seo-meta`
- Robots: `GET /robots.txt`
- Sitemap: `GET /sitemap.xml`

## 检查日志

| 时间 | 状态 | 备注 |
|------|------|------|
| 2026-06-28T23:00:00+08:00 | OK | 公网 v1 上线 |
| 2026-06-28T23:05:00+08:00 | OK | 加入 /api/track 与 /api/stats |
| 2026-06-28T23:07:00+08:00 | OK | 公网 v3 上线，埋点验证 |
| 2026-06-28T23:09:00+08:00 | OK | 公网 v4 上线，SEO 完整 |
| 2026-06-28T23:12:00+08:00 | OK | 公网 v5 上线，IndexNow 推送 202 |
| 2026-06-28T23:15:00+08:00 | OK | 公网 v6 上线，IndexNow 24h 限频 |
| {{AUTO}} | {{AUTO}} | {{AUTO}} |