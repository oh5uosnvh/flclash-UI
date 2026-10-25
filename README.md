# flclash-UI

FlClash 配置页 UI 定制：**连体按钮（筛选|排序）** 与 **标题「配置」的定位/回顶/到底交互**。
本仓库是这套 UI 改动的源码、交互规格说明与构建管线镜像。

## 交互规格（标题「配置」二字）

| 动作 | 行为 |
|---|---|
| 点击 | 选中配置卡片在屏上 → 回顶部；在当前筛选列表里但不在屏上 → 定位到该卡片；**回顶部永远优先**：选中卡被筛选隐藏/未选择时，第一次点击仍先回顶部 |
| 已在顶部再点击 | 才提示定位不可用原因（「当前配置被筛选条件隐藏了」/「还没有选择配置」） |
| 长按 0.5 秒 | 直接滚动到列表底部 |

定位实现为两阶段：先按卡片在列表中的相对位置粗跳（让懒加载网格把它建出来），
再逐帧修正并收敛到卡片上缘对齐内容区（`ProfilesLocator`，最多 10 次尝试、
有界不空转）。动画 = `animateTo` + `Curves.easeOutCubic`（Flutter 官方写法）。

## 连体按钮（筛选|排序）

`ProfilesHeaderControls`：两半共用一个圆角胶囊。筛选半区打开
默认 / 订阅 / 本地 列表；排序半区翻转订阅/本地的日期排序（默认模式下可见但
不生效，因为默认保持手动排序）。与标题是**独立命中区**——点 pill 永远不会
被识别成点标题（历史上修过穿透问题）。

## 文件与集成点

| 文件 | 内容 |
|---|---|
| `lib/views/profiles/profiles.dart` | 页面状态：标题回调（点击/长按逻辑）、筛选/排序状态、身体与头部接线 |
| `lib/views/profiles/profiles_header_controls.dart` | `ProfilesTitle`（标题手势区，RawGestureDetector 精确 500ms 长按）+ `ProfilesHeaderControls` 连体按钮 |
| `lib/views/profiles/profiles_locator.dart` | `ProfilesLocator`：reveal 两阶段定位、toTop/toBottom、isAtTop |

集成方式：覆盖 FlClash 工程 `lib/views/profiles/` 同名文件，并在
`lib/l10n/intl/messages_*.dart` 增加 `profilesLocateHidden` /
`profilesLocateNone` 两条文案（各语言值见 flclash-private 工程）。

## 构建联动

本仓库是 UI 源码与交互规格的维护仓库。发布构建由
`oh5uosnvh/flclash-private` 统一执行；构建前会校验 UI 活动文件、协议活动仓库和内核来源，构建后执行源码测试、静态分析、平台打包与协议标记校验。

UI 集成范围：

- `lib/views/profiles/` 配置页交互与标题定位；
- 配置卡片菜单、延迟测试状态和弹窗交互由客户端活动源码维护；
- 归档目录仅供历史查阅，不参与构建。

## 相关仓库

- `oh5uosnvh/flclash-private` — 最终客户端与统一构建入口；
- `oh5uosnvh/clash-meta-mods` — 协议内核；
- `oh5uosnvh/flclash-MG` — 协议源码镜像、测试与构建资料。
