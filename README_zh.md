# DB Reviewer Skill

[English README](README.md)

`DB Reviewer` 是一个面向 Codex 的技能源码仓库，用于以“正确性优先、证据优先”的方式审查数据库相关工作。它既支持对 schema、SQL、benchmark 等技术内容做 review，也支持对数据库或 data-centric systems 论文撰写会议式审稿意见。

这个 skill 现在会区分 `PDF` 和 `TeX` 两类输入：

- `PDF` 工作流：看渲染后的论文、图表、表格和写作呈现，并在正式审稿前先扫描文本层中的 prompt injection。
- `TeX` 工作流：直接检查源码结构、符号定义、宏命令使用，以及 `.tex` 文件中的隐藏指令。
- `PDF + TeX` 联合工作流：用 PDF 判断 presentation，用 TeX 追踪符号、公式、表格和 appendix 引用的精确出处。

这个 skill 更偏向我本人常用的会议场景：

- `SIGMOD`
- `VLDB`
- `ICDE`
- `NeurIPS` 的数据库或 data-centric 相关 track
- `ICLR` 的数据库或 data-centric 相关 track

## 能力范围

- 数据库 schema 和数据模型审查
- SQL 与查询逻辑审查
- benchmark 与实验设计审查
- 数据库论文或设计文档审查
- 带 venue 校准的会议式审稿草稿撰写
- 面向 PDF 和 TeX 的 prompt injection 检查

## 仓库结构

```text
db-reviewer/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── evaluation-review.md
│   ├── conference-review-format.md
│   ├── methodology-checks.md
│   ├── paper-review.md
│   ├── pdf-review-workflow.md
│   ├── prompt-injection.md
│   ├── review-writing-style.md
│   ├── schema-review.md
│   ├── sql-review.md
│   ├── tex-review-workflow.md
│   └── venue-calibration.md
└── scripts/
    └── scan_prompt_injection.py
```

## 安装方式

以下命令默认在仓库根目录执行。

先拉取仓库：

```bash
git clone https://github.com/QibaiAluminum/db_reviewer.git
```

### 1) Codex

把 skill 安装到 Codex：

```bash
SKILL_HOME="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$SKILL_HOME"
cp -R db-reviewer "$SKILL_HOME/"
```

安装完成后重启 Codex，让新 skill 被重新发现。

使用示例：

```text
Use $db-reviewer to review this database paper PDF for SIGMOD or VLDB.
```

### 2) CC（Claude Code）

可选择全局安装或项目级安装。

全局安装：

```bash
mkdir -p "$HOME/.claude/skills"
cp -R db-reviewer "$HOME/.claude/skills/"
```

项目级安装：

```bash
mkdir -p .claude/skills
cp -R db-reviewer .claude/skills/
```

使用时建议在提示词中显式指定，例如：

```text
Please use the db-reviewer skill to review this paper.
```

### 3) Gemini

可将该技能复制到 Gemini 的技能目录：

```bash
mkdir -p "$HOME/.gemini/skills"
cp -R db-reviewer "$HOME/.gemini/skills/"
```

随后在 Gemini 中直接给出具体任务，例如：

```text
Review this TeX source tree as a SIGMOD submission and point out the main weaknesses.
```

## 使用方式

在 prompt 里显式点名：

```text
请使用 $db-reviewer 审这篇数据库方向的 SIGMOD 或 VLDB 论文 PDF。
```

```text
请使用 $db-reviewer 审查这个 TeX 源码目录，并输出一份适合 ICDE 的 review。
```

```text
请使用 $db-reviewer 同时对照这篇论文的 PDF 和 TeX 源码，输出一份适合 NeurIPS 数据库相关 track 的 review，包括 strengths、weaknesses、questions、limitations 和 scores。
```

如果不是论文审稿，而是技术审查：

```text
请使用 $db-reviewer 审查这条 SQL 的正确性和性能风险。
```

## PDF 与 TeX 的区别

### PDF

适合判断：

- 第一印象和整体呈现质量
- 图表和表格是否清晰
- 关键论断是否真的出现在主文中
- 渲染后的文本层里是否存在隐藏 prompt injection

PDF 路径依赖 `pdftotext` 提取文本。如果本机没有，请先安装 Poppler。

### TeX

适合判断：

- 符号是否前后一致
- 公式是否真的支撑对应 claim
- `\input` / `\include` 结构下各 section 的实际来源
- 源码中是否存在隐藏指令或可疑宏

TeX 路径不依赖 `pdftotext`。

## Prompt Injection 检查

仓库内置了一个辅助脚本：

```bash
python db-reviewer/scripts/scan_prompt_injection.py path/to/paper.pdf
python db-reviewer/scripts/scan_prompt_injection.py path/to/main.tex
python db-reviewer/scripts/scan_prompt_injection.py path/to/source-dir
```

脚本会扫描常见的审稿诱导短语，例如：

- `include both`
- `in your review`
- `ignore previous`
- `must include`

对于 TeX 输入，还会额外检查 `\textcolor{white}{...}`、`\tiny` 等隐藏模式。

## 审稿写作风格

这个 skill 的写作风格约束包括：

- 不使用 em dash
- 不自己发明论文里没有出现过的符号
- 不使用模板化 AI 腔
- Strengths 和 Weaknesses 之间不能互相打架
- Questions 需要说明回答会如何影响评分

## Venue 校准

仓库里额外提供了这些场景的校准说明：

- `SIGMOD`、`VLDB`、`ICDE`
- `NeurIPS` / `ICLR` 的数据库或 data-centric 相关 track

参考：

- [通用会议审稿结构](db-reviewer/references/conference-review-format.md)
- [Venue 校准指南](db-reviewer/references/venue-calibration.md)

## 开发与校验

本地校验命令：

```bash
python /root/.codex/skills/.system/skill-creator/scripts/quick_validate.py db-reviewer
```

## 相关文件

- [SKILL.md](db-reviewer/SKILL.md)
- [论文审稿主指南](db-reviewer/references/paper-review.md)
- [通用会议审稿结构](db-reviewer/references/conference-review-format.md)
- [Venue 校准指南](db-reviewer/references/venue-calibration.md)
- [PDF 工作流](db-reviewer/references/pdf-review-workflow.md)
- [TeX 工作流](db-reviewer/references/tex-review-workflow.md)
- [Prompt Injection 指南](db-reviewer/references/prompt-injection.md)
