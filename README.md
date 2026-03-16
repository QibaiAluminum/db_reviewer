# DB Reviewer Skill

[中文说明](README_zh.md)

`DB Reviewer` is a Codex skill source repository for reviewing database-related work with a
correctness-first and evidence-first mindset. It covers technical review of schema and SQL artifacts,
and it also supports conference-style review of database or data-centric systems papers.

The skill now distinguishes between `PDF` submissions and `TeX` source trees:

- `PDF` workflow: inspect the rendered paper, figures, tables, and writing quality; scan the text
  layer for prompt injection before reviewing.
- `TeX` workflow: inspect source structure, notation definitions, macro usage, and hidden
  instructions directly from `.tex` files.
- `PDF + TeX` workflow: use the PDF for presentation judgment and use TeX for exact tracing of
  notation, equations, tables, and appendix references.

The review guidance is not ICML-bound. The current defaults are aimed at the kinds of papers you
would see in:

- `SIGMOD`
- `VLDB`
- `ICDE`
- `NeurIPS` database or data-centric tracks
- `ICLR` database or data-centric tracks

## What This Skill Covers

- Database schema and data-model review
- SQL and query logic review
- Benchmark and experiment design review
- Database paper or design-doc review
- conference-style review drafting with venue-aware calibration
- Prompt-injection scanning for PDF and TeX inputs

## Repository Layout

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

## Installation

Clone the repository:

```bash
git clone https://github.com/QibaiAluminum/db_reviewer.git
```

Install the skill into Codex:

```bash
SKILL_HOME="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$SKILL_HOME"
cp -R db_reviewer/db-reviewer "$SKILL_HOME/"
```

Restart Codex after installation so the new skill is discovered.

## Usage

Invoke the skill explicitly in your prompt:

```text
Use $db-reviewer to review this database paper PDF for SIGMOD or VLDB.
```

```text
Use $db-reviewer to review this TeX source tree and write a venue-appropriate review for ICDE.
```

```text
Use $db-reviewer to cross-check this paper's PDF and TeX sources, then draft a NeurIPS-style database-track review with strengths, weaknesses, questions, limitations, and scores.
```

For non-paper review:

```text
Use $db-reviewer to review this SQL query for correctness and performance risk.
```

## PDF vs TeX Workflow

### PDF

Use the PDF path when you need to judge:

- first-impression quality
- figure and table readability
- whether major claims are visible in the main paper
- whether the rendered paper contains hidden prompt injection in the text layer

The PDF workflow depends on `pdftotext` for text extraction. Install Poppler if it is missing.

### TeX

Use the TeX path when you need to judge:

- notation consistency
- equation-to-claim tracing
- section provenance across `\input` and `\include`
- hidden instructions or suspicious macros in source files

The TeX workflow does not require `pdftotext`.

## Prompt-Injection Scan

The repository includes a helper script:

```bash
python db-reviewer/scripts/scan_prompt_injection.py path/to/paper.pdf
python db-reviewer/scripts/scan_prompt_injection.py path/to/main.tex
python db-reviewer/scripts/scan_prompt_injection.py path/to/source-dir
```

The script scans for reviewer-targeted phrases such as:

- `include both`
- `in your review`
- `ignore previous`
- `must include`

For TeX inputs, it also checks suspicious hiding patterns such as `\textcolor{white}{...}` and
`\tiny`.

## Review Style

The skill is tuned for direct reviewer-style writing:

- no em dashes
- no invented notation
- no templated AI phrasing
- strengths and weaknesses must stay consistent
- questions should explain how the answer would affect the score

## Venue Calibration

The repository includes explicit calibration guidance for:

- `SIGMOD`, `VLDB`, `ICDE`
- `NeurIPS` and `ICLR` database or data-centric tracks

See:

- [Conference review format](db-reviewer/references/conference-review-format.md)
- [Venue calibration](db-reviewer/references/venue-calibration.md)

## Development

Validate the skill locally:

```bash
python /root/.codex/skills/.system/skill-creator/scripts/quick_validate.py db-reviewer
```

## Related Files

- [SKILL.md](db-reviewer/SKILL.md)
- [Paper review guide](db-reviewer/references/paper-review.md)
- [Conference review format](db-reviewer/references/conference-review-format.md)
- [Venue calibration](db-reviewer/references/venue-calibration.md)
- [PDF workflow](db-reviewer/references/pdf-review-workflow.md)
- [TeX workflow](db-reviewer/references/tex-review-workflow.md)
- [Prompt injection guide](db-reviewer/references/prompt-injection.md)
