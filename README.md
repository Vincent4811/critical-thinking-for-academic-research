# Academic Research Thinking

[繁體中文](README.zh-TW.md) · Version 0.2.0

A portable research-reasoning skill built from Vincent's **Critical Thinking for Academic Research** course. It helps researchers refine questions, students make their own evidence-based revisions, and teachers design executable critical-thinking lessons.

**First judgment → Challenge → Define → Evidence → Alternatives → Revise → Next evidence.**

The outcome is an answerable question, an explicit evidence boundary, and a next check that can change the judgment. Agreement, novelty, and rewriting are not success requirements.

## Start here

Point an Agent Skills-compatible assistant at [SKILL.md](SKILL.md), or copy this entire directory into the skill location supported by your agent. Keep the references and templates beside it. Do not copy only SKILL.md.

Examples of requests:

```text
Use academic-research-thinking to analyze this question and the supplied paper.
Distinguish what the paper reports from what my proposed study assumes.
```

```text
用 academic-research-thinking 指導學生。先保留他的原始問題與理由，
每輪只問一個有助判斷的問題，不要先給改寫答案。
```

Default interaction language is Traditional Chinese. Request English when needed. The skill needs no code execution, model API, connector, or other installed skill to perform reasoning over supplied material. Source verification uses whichever authorized reading/search tools the host provides; unavailable access is disclosed.

## Three modes

| Mode | Use | Result |
| --- | --- | --- |
| `analyze` | Researcher asks for analysis, question refinement, or appraisal | Supported analysis now, with provisional statements and missing evidence identified |
| `coach` | Actual learner guidance, live classroom practice, Research Question Clinic | Learner's first view, one consequential question per turn, learner-owned revision |
| `design-lesson` | Teacher asks for a lesson, activity, workshop, worksheet or assessment design | Complete agenda, materials/rules, prompts, learner outputs, revision and exit assessment |

No mode-selection interview is required. An explicit request wins; otherwise infer the mode from intent. A worked demonstration is labeled as a demonstration.

For teacher preparation, `design-lesson` takes precedence over live `coach`. It can prepare the full set of teacher prompts at once; the one-question-per-turn rule applies when actually coaching a learner.

```text
用 academic-research-thinking 設計 120 分鐘 Critical thinking 課程活動，
包含可操作規則、個人思考、同儕挑戰、研究問題圖、修訂與 exit ticket。
```

## Read and reuse

- [Method, English](docs/method.en.md) / [方法，繁體中文](docs/method.zh-TW.md)
- [Analysis template, English](templates/analysis.en.md) / [繁體中文](templates/analysis.zh-TW.md)
- [MindMap, English](templates/mindmap.en.md) / [繁體中文](templates/mindmap.zh-TW.md)
- [Coaching record, English](templates/coach-session.en.md) / [繁體中文](templates/coach-session.zh-TW.md)
- [Examples and their evidence boundaries](examples/README.md)
- [120-minute workshop and 50-minute adaptation](teaching/lesson-120.en.md) / [繁體中文](teaching/lesson-120.zh-TW.md)
- [Six teacher activity cards](teaching/activity-cards.en.md) / [繁體中文](teaching/activity-cards.zh-TW.md)
- [Lesson-planning template](templates/lesson-plan.en.md) / [繁體中文](templates/lesson-plan.zh-TW.md)
- [Individual learner worksheet](templates/classroom-worksheet.en.md) / [繁體中文](templates/classroom-worksheet.zh-TW.md)
- [Course and research provenance](references/source-map.md)
- [Upstream adaptations](references/thinking-tools.md)

The formal map has five branches and E/A/U labels. E identifies a traceable report, not a guarantee that a finding is valid. The four-branch classroom map is an introductory view; see the map templates for its correspondence to the formal map.

## Validate the package

Python 3.10+ is needed only for the package checker, not for using the skill:

```sh
python scripts/validate_package.py
```

The checker verifies relative links, metadata, release contents, upstream records, JSON/CSV files, and obvious private-path or credential contamination. Mermaid parsing/rendering and actual agent responses require the separate checks described in [evals/README.md](evals/README.md). Passing structural checks is not proof of good reasoning or a measured improvement in research quality.

## Provenance and license

The five habits, games, learner ownership, and question-map design come from the supplied course materials. Selected mechanisms are adapted from [TJ Boudreaux's cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills), pinned in [UPSTREAM.json](UPSTREAM.json). This package does not install the upstream catalog.

Original package material is under [MIT](LICENSE), credited to Vincent. Retained third-party terms and adaptation details are in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Scientific papers remain under their own rights. Source PDFs, third-party slide images, identifiable learner work, unpublished data, and local source paths are not distributed.

This is a reasoning aid and teaching framework. It is not a validated assessment instrument, a complete study protocol, or evidence that the chosen thinking tools improve research outcomes.
