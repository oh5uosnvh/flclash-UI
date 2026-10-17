# Bettbox v1.19.6 适配

- 最新正式基线：appshubcc/Bettbox v1.19.6，提交 9582976d537176d2ffd682e98723160a04800bfd。
- 用户 fork：https://github.com/oh5uosnvh/Bettbox
- 适配分支：agent/mg-ui-v1196。
- UI/MG 配套分支：integrations/bettbox-v1196。
- Bettbox 使用 package:bett_box 和完整 Grid，不能直接套用 FlClash 0.9.0 页面。
- 保留 Bettbox 布局和原生编辑功能；增加标题长按后 500ms 平滑到底、标题点击回顶/定位、新增配置布局后到底。
- Android 安装 ID：com.appshub.bettbox.qiyiguo112，与 Bettbox 官方及 FlClash 独立。
- 内核使用 Bettbox 内置 core/Clash.Meta，复用 FlClash-MG 私有协议增量与 VT module replace，不替换整颗上游内核。

本地 core、私有协议、VT 测试通过。CI 源码分析通过。完整 Flutter 测试 288 个事件中有 7 个失败事件；对同一个正式标签、同一 SDK 独立运行也得到相同失败集合（文件夹初始化/文件迁移、连接图标、放大字体 chip），新增失败集合为空。此为差异门禁通过，不表示所有上游测试通过。

CI：https://github.com/oh5uosnvh/Bettbox/actions/runs/39016058450

配置导入、VPN 连接与多平台观感仍需真机实测。当前 APK 沿用上游 Debug 签名回退，不保证与官方或其他构建覆盖安装。
