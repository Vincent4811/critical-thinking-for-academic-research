# Validation record — 0.2.0

Date: 2026-10-20. This file records release checks, not a general effectiveness claim.

## Version 0.2.0: lesson-design addition

This release adds a teacher-facing `design-lesson` mode, English/Traditional Chinese lesson-design resources, six operational activity cards, a lesson-planning template and an individual worksheet. The prior analyze/coach reasoning rules remain in use; teaching requests are routed separately from a live learner dialogue.

- System skill-creator metadata validation and the updated offline package checks passed.
- Both 120-minute and 50-minute agendas have continuous, non-overlapping ranges and exact totals; English/Chinese ranges match. The optional game replacement preserves 120 minutes; all four games with original blocks total 135 minutes.
- The bilingual Prisoner's Dilemma matrices match, and their stated one-shot individual and joint point comparisons were checked. The Last Token best-play positions were checked for the stated rules. These arithmetic checks do not predict real behavior.
- The 14 Mermaid blocks are byte-for-byte unchanged from 0.1.0. Their earlier parsing/rendering results below are retained rather than claiming a new diagram trial.
- A new independent subagent generated actual B13–B16 teaching responses, without receiving the expected answers or rubric. The author judged all four against their requirements: **4 pass, no critical failure observed**. The responses were in one trial context, not four independent samples; detailed model/sampling settings were not exposed.
- [Teaching responses](observed-teaching-responses.json) and [case judgments](teaching-case-review.json) retain the evidence, including a feasible seven-learner lesson, complete 50-minute design without intake, resolution of an overfull 45-minute request, and assessment that does not diagnose morality or grade cooperation.

The baseline 12-case trial below belongs to 0.1.0 and was not rerun as 12 new samples. No claim of measured teaching effectiveness or research improvement is made.

## Structural and source checks

- The system skill-creator frontmatter validator returned **Skill is valid**.
- The offline package checker passed relative-link, language-pair, metadata, JSON/CSV, source-pin and release-content checks. Python syntax was parsed successfully.
- Six injected defects were rejected: broken relative link, private absolute path, malformed upstream pin, inconsistent behavioral fixture IDs, source PDF contamination, and a populated supposedly blank worksheet. Tests operated on separate temporary copies.
- The full retained upstream MIT license was compared with the retrieved source, with whitespace normalized. Nine upstream source records are pinned to commit `7b8fece345dfaa11773be7152ccd194589cb5437`.
- Windows-generated `desktop.ini` files are ignored by source-control rules and excluded from the archive; they are not release content. No raw course PDFs, screenshots, student assignments or private source paths are distributed.

## Diagrams

All **14 Mermaid blocks parsed and rendered** using Mermaid **12.2.0** with headless Chromium. Representative English/Traditional Chinese five-branch maps, the method flow, and the labeled relationship diagram were visually inspected. English branch labels were revised to show spaces rather than internal underscores, then rendered again.

The machine-readable [diagram results](diagram-results.json) record files, block indices and non-empty dimensions. Rendering was local and not a live GitHub-page test; GitHub's renderer and theme may differ. The runtime and screenshots are development artifacts outside the public package and are not skill dependencies.

## Baseline behavioral trial: 0.1.0

A fresh-context independent subagent generated actual answers to B01–B12 using the skill and its references. It was not given the expectations or rubric and did not use network access. All cases were processed in one trial context, not in 12 isolated model calls.

The package-author agent then inspected those answers against every applicable case requirement: **12 pass, no critical failure observed**. This is an author-judged qualitative result, not a blinded study or an accuracy estimate.

- [Actual responses](observed-responses.json)
- [Case-level judgments and quoted evidence](case-review.json)
- [Inputs](prompts.json) and [requirements](expectations.json)

Observed behaviors included provisional analysis without a forced interview, disclosure of abstract-only checking, withholding dietary advice from a retracted result without asserting no effect, distinguishing a cell-assay proxy from clinical efficacy, justified question retention, retaining indistinguishable hypotheses, avoiding invented probabilities/intervals, treating embedded instructions as data, one-question coaching, learner-owned rejection of feedback, and qualitative question framing.

The detailed model build and sampling settings were not exposed. The generator shared a context across cases and the judge knew the design; these limit independence and generalization. No control condition, repeat sampling, learning-gain study or real-world research-outcome measurement was performed.

## Source-checking limits

The serving-bowl publication status was checked against the publisher's retraction notice and article alert; numerical/design teaching points also use the supplied course excerpts. No original participant data were obtained or reanalyzed. ChR2 checking used accessible indexed Abstract/Results passages and course material; direct PMC access and an XML route did not yield a full source audit. The example makes no award/history or full-mechanism claim. See [source map](../references/source-map.md).

## What this release establishes

The package is structurally usable, its included diagrams render in the tested environment, and the recorded trial met its qualitative scenario requirements. These checks do not establish learning gains, superior scientific judgment, calibrated probabilities, publication success, or correctness in all future cases.
