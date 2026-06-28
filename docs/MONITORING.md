# 子 Agent 监控方案

## 目的
主 agent 在长任务中可能调用 API 超时，导致赚钱链路中断。子 agent 周期性：
1. 健康检查（站点是否 200）
2. 状态汇报（写入 STATE.md）
3. 卡死告警（如发现连续 3 次异常，通知主 agent 自愈）

## 方案 A：Hermes Cron（推荐）
- 用 `cronjob` 工具创建定时任务
- 每 30 分钟执行一次
- prompt: 检查站点 + 检查 STATE.md + 必要时告警

## 方案 B：后台进程
- `terminal(background=true)` 起一个 watcher 进程
- 简单但需要 session 存活

## 选型
**默认走方案 A（cron）**。原因：
- 会话关闭也能跑
- 输出可投递到 telegram/本地
- 自带 deliver 通道

## 监控检查清单（每次 tick）
- [ ] 落地页 HTTP 200？
- [ ] 收款码图片可访问？
- [ ] STATE.md 在过去 1h 内被更新过？
- [ ] 今日是否有新成交？
- [ ] 公网域名 DNS 正常？

## 异常处理
- 落地页 5xx → 告警 + 自动尝试重启
- STATE.md 超过 2h 未更新 → 告警"主 agent 可能卡死"
- 连续 3 次告警无人响应 → 写入 ESCALATION.md