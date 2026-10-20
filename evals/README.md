# Reproduce the checks

## Structural release check

Run from the package root using Python 3.10+:

```sh
python scripts/validate_package.py
```

This does not contact services or run a model. It checks packaging and obvious private-data contamination, not scientific correctness. The included CSV files are blank worksheets with headers, not datasets.

To check that the validator rejects real packaging defects:

```sh
python evals/test_validator.py
```

The six negative tests mutate only newly created temporary copies. They deliberately retain those copies for inspection. An optional `--scratch` directory must be outside this package.

Version 0.2.0 also checks the bilingual lesson schedules, optional-game timing and symbolic game logic:

```sh
python evals/test_lesson_design.py
```

These are arithmetic/consistency checks on the designed activities, not a test of real behavior or learning efficacy. B13–B16 add teacher-facing design scenarios, distinct from live learner coaching.

## Diagram check

Collect every fenced `mermaid` block in the Markdown files and parse/render it using Mermaid in an isolated development environment; record the exact version. Inspect representative English and Traditional Chinese maps and the labeled-link diagram for readable branches, preserved Unicode, and edge labels. The skill itself has no JavaScript or Mermaid runtime dependency; GitHub can display Mermaid source, although its renderer/version can differ from the tested environment.

## Behavioral check

Give an evaluator the skill and only [prompts.json](prompts.json), in a fresh context when possible. For each case, request the actual response using the skill, not a prediction of what the skill would do. Keep responses distinct and let multi-turn coaching fixtures retain only their supplied context. Do not provide the expected answers to the responding agent.

After responses exist, judge them against [expectations.json](expectations.json) and [rubric.md](rubric.md). Record failures before changing the skill, and rerun affected cases only if a change addresses an observed problem. Any external evaluation tool requires its own authorization; this package does not require a paid API or connector.

The [validation report](validation-report.md) records the checks actually completed for this release and their limitations. Readers should not infer general effectiveness from a single evaluated run.
