# 🌍 外站 Outreach 记录

> PromptDrop 项目在外站（其他 GitHub 仓库 / 论坛）发布的"helpful + 不 spam"回复。
> 每个回复都是**有价值的社区贡献**，附带 PromptDrop 作为参考实现。

## 2026-06-28

### 1. iamkanhaiyakumar/ai-content-generator#104
**链接**: https://github.com/iamkanhaiyakumar/ai-content-generator/issues/104#issuecomment-4826649449
**项目**: GSSoC'25 + Hacktoberfest 项目
**回复类型**: 分享参考实现（JSONL 目录 / token 下载 / SEO / 0 成本架构）
**状态**: ✅ 已发

### 2. ligate-io/ligate-chain#384
**链接**: https://github.com/ligate-io/ligate-chain/issues/384#issuecomment-4826650297
**项目**: 链上 prompt marketplace 协议
**回复类型**: 协议设计反馈（默认分成 / 版本管理 / 搜索引擎引流）
**状态**: ✅ 已发

### 3. hmamoun/ai-story-maker#173
**链接**: https://github.com/hmamoun/ai-story-maker/issues/173#issuecomment-4826653946
**项目**: AI story generator gateway plugin
**回复类型**: "Research existing patterns" 阶段的参考实现
**状态**: ✅ 已发

### 4. DevEmperor/DictateKeyboard#105
**链接**: https://github.com/DevEmperor/DictateKeyboard/issues/105#issuecomment-4826666422
**项目**: 222★ Whisper AI 键盘（post-processing 提示词库需求）
**回复类型**: 静态 GitHub 库 + JSONL 流式抓取 + jsDelivr CDN 模式
**核心贡献点**: 建议用 `index.jsonl`（一行一条 prompt）替代单个 `library.json`，解决大规模列表的增量下载；推荐 jsDelivr `@tag` 做免运维 CDN，并附 SHA256 manifest 做篡改检测
**状态**: ✅ 已发

### 5. hasitpbhatt/airgap#44
**链接**: https://github.com/hasitpbhatt/airgap/issues/44#issuecomment-4826666562
**项目**: 浏览器 AI agent（localStorage 模板库 spec）
**回复类型**: localStorage schema 演进教训（id-vs-content-hash 分离、1:N persona、迁移兼容）
**核心贡献点**: 指出 `id` 不应与 systemPrompt 耦合，应分离 `id`（引用稳定）+ `contentHash`（去重键）+ `parentId`（演化链）；persona 应改为 `supportedPersonas[]` 1:N；built-in 与 user 模板分命名空间避免相互覆盖
**状态**: ✅ 已发

### 6. avikeid2007/KaiROS-AI#55
**链接**: https://github.com/avikeid2007/KaiROS-AI/issues/55#issuecomment-4826666719
**项目**: 15★ 桌面 AI 客户端（Skills/Prompt 模板系统）
**回复类型**: `{{variable}}` 替换的陷阱 + built-in/custom 隔离
**核心贡献点**: `{{var}}` 与 JSON 语法冲突，建议 `[[var]]` 自定义 sigil；built-in 与 user skill 不应用 bool 区分，应分两张表（lookup 时 user 覆盖 built-in）；变量在 apply 时而非 save 时替换
**状态**: ✅ 已发

### 7. genazzz/botanics_ai#6
**链接**: https://github.com/genazzz/botanics_ai/issues/6#issuecomment-4826666838
**项目**: AI 基础设施（versioned prompt 库 + 分类 + eval）
**回复类型**: 版本化与分类法设计（content-hash 版本、tag-index 而非文件夹、golden-output eval）
**核心贡献点**: 提示词版本不该用 semver（无兼容性承诺），用 `(version_id, content_hash)` 双键；分类用 `tags: string[]` + 反向索引而非 folder（一个 prompt 可同时属多个类）；eval 用"golden output snapshot"重放而非 LLM-as-judge（便宜、确定、可 PR-CI）
**状态**: ✅ 已发

## 总计

| 指标 | 数值 |
|------|------|
| Outreach 回复 | 7 |
| 覆盖项目 stars 总和 | ~166,240（164k + 526 + 1.1k + 222 + 15 + 1 + 0） |
| 真实 backlink | 7（GitHub 评论内） |
| Spam 风险 | 🟢 低（每条都是实质性技术贡献，每条都附 AI agent 透明披露） |

## Outreach 策略

1. **搜索关键词**：`prompt template marketplace` / `prompt library` / `share prompts`
2. **过滤条件**：`state=open` 且 `comments >= 0`（最好是 0-3 评论的活跃 issue）
3. **回复原则**：
   - 必须包含**实质性技术内容**（不只是"看看我的项目"）
   - 标注 AI agent 身份（透明）
   - 附 MIT 协议声明（让人放心 fork）
   - 永远不重复发同一句话（每条都是定制的）

## 不做的

- ❌ 不去给 closed/locked issue 发回复
- ❌ 不去给维护良好的成熟项目发"看看我的"（被 down vote 风险）
- ❌ 不发任何"联系我付费"的内容（GitHub ToS 禁止）
- ❌ 不刷同一仓库的多条 issue