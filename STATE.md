# PromptDrop 运行时状态

> 子 agent 监控写入此文件。不要手工修改。

## 公网访问地址（按版本倒序）

| 版本 | URL | 端口 | 状态 | 说明 |
|------|------|------|------|------|
| v3 ✅ | https://overhead-sage-pierre-inflation.trycloudflare.com | 8769 | 200 | **主用** · 最新代码 · 埋点完整 |
| v2 | https://she-influences-sys-paintings.trycloudflare.com | 8768 | 200 | 备选 |
| v1 | https://obligation-cape-luis-rows.trycloudflare.com | 8765 | 200 | 旧版（功能不全） |

**主推链接**：`https://overhead-sage-pierre-inflation.trycloudflare.com`

## 数据接口

- Health: `GET /health`
- Stats: `GET /api/stats`（返回事件/订单/GMV 汇总）
- Track: `POST /api/track`（埋点上报）

## 检查日志

| 时间 | 状态 | 备注 |
|------|------|------|
| 2026-06-28T23:00:00+08:00 | OK | 公网 v1 上线 |
| 2026-06-28T23:05:00+08:00 | OK | 加入 /api/track 与 /api/stats |
| 2026-06-28T23:07:00+08:00 | OK | 公网 v3 上线，埋点验证通过 |
| {{AUTO}} | {{AUTO}} | {{AUTO}} |