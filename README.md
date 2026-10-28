# cianppt

把“**先组织研究主线＋大复合图主导＋图外论点框＋一图一程序**”沉淀成可安装的 Codex skill。适用于研究汇报、课程展示、数据分析和技术演示，也可用于修改已有 PPT。

## 它会怎样组织 PPT

- **先理研究主线**：根据研究方向明确核心命题，再组织案例、文献、框架、方法、结果和应用，避免辅助变量替代主题。
- **一个大主体**：主要证据占据页面大部分区域，内部用有主次、相互补充的分图组织信息。
- **图外两三个论点框**：小标题、醒目圆点、加粗论点和简短说明，解释证据与意义。
- **紧凑但有主次**：避免整页四等分、主体过小或图侧大片空白；保持正文克制、图表详细。
- **布局有变化**：按叙事交替安排左右位置，不让整套演示始终文字在同一侧。
- **科学图表与文献详解**：支持Python复合图、详细表格、关键论文原图与研究脉络解读；图内不放解释段落，图例默认放下方图外。
- **一个图一个程序**：在`figurecode/`维护可单独运行的绘图程序、PNG/SVG与逐图索引，支持直接修改原程序和组合分图。
- **学术陈述与统一样式**：默认中文微软雅黑、英文及数字Times New Roman；术语和类别颜色一致，公式与标签避开数据和置信带。
- **按范围完成**：整套制作关注渲染效果，单图修改只更新对应代码与输出，不默认新增哈希、反复核查或重打包流程。

具体主题、模板、页数、时长与当前用户要求优先。本技能不包含某个课题的数据、机构模板、字体文件或示例论文图。

## 安装到其他电脑

### 方法一：GitHub 安装

在目标电脑的 Codex 中发送：

```text
请使用 $skill-installer，从 https://github.com/Cian301/cianppt 安装仓库根目录的技能，名称设为 cianppt。
```

公开仓库：[Cian301/cianppt](https://github.com/Cian301/cianppt)。如果以后改为私有仓库，目标电脑需要具有相应访问权限。

### 方法二：下载 ZIP 后本地安装

下载或复制整个仓库，解压，进入包含 `install.py` 的目录，执行：

```bash
python install.py
```

需要 Python 3.9 或更新版本，仅使用标准库，无需安装额外依赖。Windows 也可使用 `py install.py`，macOS/Linux 可使用 `python3 install.py`。

脚本默认安装到 `~/.agents/skills/cianppt`；这是当前官方文档中的用户级技能目录。若你的 Codex 使用其他目录，可指定**技能父目录**：

```bash
python install.py --dest ~/.codex/skills
```

也可以先查看目标，不写入文件：

```bash
python install.py --dry-run
```

已有同名目录时脚本会停止，避免覆盖本地修改。更新时可先把旧目录移出技能扫描目录，再安装新版。

不使用脚本时，将 `SKILL.md`、`agents/`、`references/` 放到目标技能目录下的 `cianppt/` 文件夹即可。项目级安装也可使用项目内的 `.agents/skills/cianppt/`。

技能发现路径与刷新方式以目标环境的[官方技能文档](https://learn.chatgpt.com/docs/build-skills)为准。安装后在新对话或下一轮调用；若未发现，重启客户端。

## 使用

```text
$cianppt 帮我制作这份研究汇报：采用大复合图和图外独立论点框，保留模板，按叙事交替安排左右布局，并逐页渲染检查。
```

```text
$cianppt 优化现有 PPT：仅调整第 6、8 页过空的图件区域，并改变部分页面的图文左右位置，保留其余内容。
```

这是制作方法和检查流程的技能，需要由支持技能的助手执行。实际生成与渲染 PPT 仍需目标环境提供相应工具；字体、模板、数据和论文图件由具体任务提供，不会随安装自动下载。

## 仓库结构

```text
cianppt/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── layout-recipes.md
│   ├── figures-and-literature.md
│   ├── research-storyline.md
│   └── figurecode-workflow.md
├── install.py
└── README.md
```

`SKILL.md`是入口，四个参考文件分别提供版式配方、图表与文献处理、研究主线、独立绘图程序与索引。安装脚本复制这六个技能文件，不安装README、脚本本身或Git历史。

## 上传到自己的 GitHub

新建名称为 `cianppt` 的仓库，将本目录文件直接放在仓库根目录，确保根目录可见 `SKILL.md`，而不是再套一层 `cianppt/`。不要上传旧课题文件、数据、模板或账号信息。

如果使用 Git，且本地目录已经初始化并提交，在 GitHub 创建空仓库后运行：

```bash
git remote add origin https://github.com/Cian301/cianppt.git
git push -u origin main
```

本地已经配置 `origin` 时，可跳过 `git remote add`。如发布到其他账号，替换仓库地址。公开仓库方便分享；私有仓库需要授权才能下载。仓库可见性与再分发许可由维护者自行选择。
