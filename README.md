# flclash-UI

FlClash 配置页 UI 定制的源码镜像，与构建管线实际输入保持一致：
本仓库 `lib/views/profiles/profiles.dart` 即构建工程覆盖使用的同名文件。

## 定制内容

### 标题「配置」交互（ScrollTitle）

| 动作 | 行为 |
|---|---|
| 点击 | 选中卡片在屏上 → 回顶部；在当前筛选列表里但不在屏上 → 两阶段定位到卡片（先粗跳让懒加载网格建出目标项，再逐帧收敛到卡片上缘）；**回顶部永远优先** |
| 已在顶部再点击 | 才提示定位不可用原因（卡片被筛选条件隐藏 / 还没有选择配置） |
| 长按 0.5 秒 | 直接滚动到列表底部 |

定位与回顶逻辑内联在网格状态类（`handleTitleTap` / `scrollToBottom`），
动画 = `animateTo` + `Curves.easeOutCubic`（Flutter 官方写法）。

### 配置卡片三个点按钮

- **纯触发按钮**：点击 = 在按钮位置打开与长按相同的官方上下文菜单；
- 菜单走官方 `CommonPopupRoute`（`belowPoint` 从点位展开 + 避开卡片矩形 +
  官方 `CommonPopupMenu`），二级「更多」展开与收回占位均由官方逻辑处理；
- 官方长按入口 `ContextMenuRegion` 保持原样，两个入口共用同一条菜单代码路径；
- 按钮 48×48 命中区，与选中徽章右缘对齐、中心同轴（`_profileRowInset` 数学）。

## 集成方式

覆盖 FlClash 工程 `lib/views/profiles/profiles.dart` 同名文件即可；
本仓库文件与工程内文件逐字节一致后推送。

## 构建管线（说明）

统一工作流在客户端工程仓库执行，本仓库不参与构建：

1. 校验活动文件（UI 镜像、协议校验脚本、内核挂载点）；
2. 检出协议内核（工作流入参指定引用，缺省为内核默认分支）；
3. `dart format` / `flutter analyze` / 定向 widget 测试 / Go wrapper 测试；
4. Android（arm64 / arm）与 Windows（amd64）打包；
5. 产物协议标记校验；
6. 上传制品并发布预发布版本。

本仓库仅作源码维护与同步基准，不记录版本基线与构建历史。
