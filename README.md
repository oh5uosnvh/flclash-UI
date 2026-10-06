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

## 构建管线

`.github/workflows/manual-build.yaml` 与 flclash-private 工程同款：
workflow_dispatch（platform: android/both/windows，kernel_ref 默认 `mods`），
内核 = `oh5uosnvh/clash-meta-mods@mods`（含 x365 / 黑石 xhttp / anytls /
viewTurbo / oppa 私有协议），构建后自动校验协议标记并发布 Release。

## 相关仓库

- `oh5uosnvh/flclash-private` — 完整可构建工程（本仓库文件的宿主）
- `oh5uosnvh/clash-meta-mods` — 私有协议内核（mods 分支）
- `oh5uosnvh/flclash-MG` — 各协议补丁与归档
