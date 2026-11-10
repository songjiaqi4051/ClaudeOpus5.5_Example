# ClaudeOpus5.5_Example

收集各种开源案例。

## 收录概况

截至 **2026-11-10**，本仓库收录 **11 个 GitHub Star 严格大于 500**、且有明确 **Claude Opus 5.5 制作依据**的浏览器项目，包含网页游戏、交互式 3D 场景、可视化与代码动画。HTML、Canvas、SVG、WebGL、WebGPU 中运行的代码动画也作为浏览器案例收录。

每个项目放在独立的 `examples/<作者>__<仓库>/` 目录，保留上游源码、素材、README 与许可证。Star 是检索当日的快照；每份副本对应的完整提交、Git 树、文件数、大小和模型依据均记录在 [catalog.json](catalog.json)。

## 项目目录

| 来源仓库 | Star | 类型 | 本仓库副本 |
|---|---:|---|---|
| [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) | 14,238 | 代码动画风格库 | [lemomo-ai__lemo-opuscar](examples/lemomo-ai__lemo-opuscar/) |
| [mexicat/pdoom-video](https://github.com/mexicat/pdoom-video) | 3,856 | Three.js音乐动画 | [mexicat__pdoom-video](examples/mexicat__pdoom-video/) |
| [Vincentwei1021/mg-styles-15](https://github.com/Vincentwei1021/mg-styles-15) | 3,376 | 动态图形与展示网页 | [Vincentwei1021__mg-styles-15](examples/Vincentwei1021__mg-styles-15/) |
| [JohnHeibel/PDoomVideo](https://github.com/JohnHeibel/PDoomVideo) | 2,895 | p5.js音乐动画 | [JohnHeibel__PDoomVideo](examples/JohnHeibel__PDoomVideo/) |
| [JohnHeibel/ClaudeAnimationBase](https://github.com/JohnHeibel/ClaudeAnimationBase) | 2,821 | p5.js角色动画 | [JohnHeibel__ClaudeAnimationBase](examples/JohnHeibel__ClaudeAnimationBase/) |
| [feichao93/battle-city](https://github.com/feichao93/battle-city) | 1,881 | React/PixiJS浏览器游戏 | [feichao93__battle-city](examples/feichao93__battle-city/) |
| [dgreenheck/tidewater](https://github.com/dgreenheck/tidewater) | 1,447 | WebGPU海岛钓鱼游戏 | [dgreenheck__tidewater](examples/dgreenheck__tidewater/) |
| [riba2534/claude-opus-5-5-demo](https://github.com/riba2534/claude-opus-5-5-demo) | 1,255 | Three.js网页游戏合集 | [riba2534__claude-opus-5-5-demo](examples/riba2534__claude-opus-5-5-demo/) |
| [Noniv/web-ocean](https://github.com/Noniv/web-ocean) | 1,015 | WebGPU海面可视化 | [Noniv__web-ocean](examples/Noniv__web-ocean/) |
| [adunext/adu-motion-video](https://github.com/adunext/adu-motion-video) | 796 | DOM/Canvas动效案例 | [adunext__adu-motion-video](examples/adunext__adu-motion-video/) |
| [Leonxlnx/athenaion](https://github.com/Leonxlnx/athenaion) | 696 | Three.js古希腊世界 | [Leonxlnx__athenaion](examples/Leonxlnx__athenaion/) |

### 从哪里开始看

- **想看游戏：** `battle-city` 是坦克大战；`tidewater` 是海岛钓鱼；`claude-opus-5-5-demo` 包含鹈鹕骑行、运输船 FPS 和赛车三个独立游戏。
- **想看 3D 与渲染：** `web-ocean` 集中展示写实海面；`athenaion` 展示程序化古希腊城市、神庙、植被和水体。
- **想看动效和页面表现：** `mg-styles-15` 有 15 种动态图形；`lemo-opuscar` 有 66 种风格及各自源码；`adu-motion-video` 保留图文讲解、手绘和 3D 模板。
- **想看完整代码动画：** 两个不同作者的 `PDoomVideo` / `pdoom-video` 分别使用 p5.js 与 Three.js；`ClaudeAnimationBase` 更适合查看角色、表情和短动画的实现。

`battle-city` 的 Opus 5.5 制作依据具体对应 **0.4.0 全面重写版本**，原项目的历史早于这一模型。

## 入口与运行方式

先进入相应 `examples/<作者>__<仓库>/` 目录，再按下表执行。每条命令单独运行；依赖版本和完整导出流程以该项目随附 README 为准。

| 项目 | 入口 / 操作 | 启动方式 |
|---|---|---|
| lemo-opuscar | `styles/watercolor/demo/index.html`；风格目录 `styles/` | `python3 -m http.server 8000`，打开上述路径；[在线画廊](https://lemomo-ai.github.io/lemo-opuscar/) |
| mexicat/pdoom-video | `app/index.html` | 进入 `app/`，依次 `bun install`、`bunx vite`，访问 `http://localhost:5173` |
| mg-styles-15 | `harness/preview.html?demo=01-flat-vector` | 依次 `npm install`、`python3 -m http.server 8000`；[在线展示](https://vincentwei1021.github.io/mg-styles-15/) |
| JohnHeibel/PDoomVideo | `studio.html` | 依次 `npm install`、`python3 -m http.server 8000`，打开 `http://localhost:8000/studio.html` |
| ClaudeAnimationBase | `studio.html`；可加 `?loop=emotions` / `?loop=views` | 依次 `npm install`、`python3 -m http.server 8000`，打开 `http://localhost:8000/studio.html` |
| battle-city | 根目录 `index.html` | 依次 `pnpm install`、`pnpm dev`；[在线游戏](https://battle-city.js.org) |
| tidewater | 根目录 `index.html` | 依次 `npm install`、`npm run dev`，访问 `http://127.0.0.1:5189`；[在线游戏](https://dgreenheck.github.io/tidewater/) |
| claude-opus-5-5-demo | `pelican-bike/`、`cf-transport-ship/`、`qq-speed/` | 任选一个子目录，依次 `npm install`、`node build.mjs`，打开生成的 `dist/index.html` |
| web-ocean | `ocean.html` / `ocean.min.html` | 可直接打开；开发时依次 `npm install`、`npm start`；[在线场景](https://ocean-noniv.vercel.app/) |
| adu-motion-video | `examples/handdrawn-continuity.html`；`examples/gallery/index.html` | `python3 -m http.server 8000`，打开上述路径；[在线画廊](https://adunext.github.io/adu-motion-video/examples/gallery/) |
| athenaion | `index.html` | 依次 `npm install`、`node tools/serve.mjs`，访问 `http://localhost:8080/?shot=1&quality=preview` |

WebGPU 项目需要支持 WebGPU 的浏览器与 GPU。部分动画源码需要单独生成音频或下载上游 Releases 中的成片；`lemo-opuscar` 的完整影片画廊可先从在线入口观看。`mg-styles-15` 的离线配乐/渲染还使用 Python，3D Render 示例需要 Blender；其他视频导出依赖见各项目说明。

## 来源与许可

每个副本沿用原作者的许可和素材声明。代码、音乐、字体与演示影片的授权范围可能不同，具体对应关系、制作证据及筛选记录集中在 [sources/README.md](sources/README.md)。

## 版本与完整性

本次保存 **11 个项目、5,130 个上游文件，共 934,000,174 字节（约 934 MB）**。每个项目目录的 Git 树 SHA 均已与对应上游固定版本核对一致，源码、素材与文件模式完整保留。[导入校验记录](sources/import-report.json) 列出逐项目的结果。
