# PromptDrop BDD 详细场景

## Feature: 落地页转化

### Scenario: 访客首屏看到价值主张
- **Given** 用户从搜索引擎/社交媒体点击进入
- **When** 页面加载完成（LCP < 2.5s）
- **Then** 首屏可见：
  - 一句话价值主张（≤ 12 字）
  - 至少 3 个 SKU 卡片（标题 + 价格 + 一句话卖点）
  - 一个明确的 CTA 按钮
- **And** 无需注册/登录

### Scenario: 移动端可读
- **Given** 用户使用手机访问
- **When** 视口宽度 ≤ 375px
- **Then** SKU 卡片纵向单列，CTA 按钮全宽可点

## Feature: 支付流程

### Scenario: 用户点击购买
- **Given** 用户在某个 SKU 卡片上看到价格
- **When** 用户点击"立即购买"
- **Then** 弹出 modal 或跳转订单页，显示：
  - 订单号（自动生成，时间戳后 6 位）
  - 二维码图片（微信 + 支付宝 二选一或都给）
  - 客服微信号
  - "付款后请截图发送给客服"提示

### Scenario: 客服人工发货（v1）
- **Given** 用户已支付并截图
- **When** 客服在 10 分钟内确认收款
- **Then** 通过微信发送下载链接
- **And** 记录到 docs/DAILY.md

## Feature: 数据埋点

### Scenario: 每日复盘
- **Given** 一天结束
- **When** 运营者打开 docs/DAILY.md
- **Then** 当日记录包含：
  - PV / UV
  - 加购数（按钮点击数）
  - 订单数
  - GMV
  - 转化率 = 订单数 / UV
  - 客单价
  - 渠道来源分布

## Feature: 持续可用性

### Scenario: 站点 7x24 可访问
- **Given** 任何时间
- **When** 任意用户访问
- **Then** 返回 200 状态码
- **And** 首屏 < 2.5s
- **And** 子 agent 每 30 分钟 ping 一次，发现 5xx 自动告警