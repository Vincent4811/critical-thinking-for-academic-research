# Evidence labels and question maps

## E/A/U: knowledge labels, not scores

| Label | Meaning | Minimum record |
| --- | --- | --- |
| E | Traceable observation or source report | Source ID, locator, actual report, access/check scope, publication status |
| A | Assumption, interpretation/inference, or hypothesis | Subtype, premise, why plausible, what would challenge it |
| U | Missing fact or unresolved question | What is unknown, why consequential, next way to check |

An E node records that a source reports something, not that the reported effect is true. An author's mechanistic interpretation can be E as a **reported interpretation**, while adopting that mechanism as your explanation is A. Make the distinction explicit. A user report is attributed to the user and not upgraded to independently verified evidence.

Source checking and scientific validity are separate. A faithfully extracted sentence in a retracted article remains a traceable report; its retraction prevents using that report to establish the substantive effect. Unsupported details remain U even when nearby details are verified.

## Source record

Use a compact ledger, expanded only as needed:

| ID | Claim/report | E/A/U and subtype | Source and locator | Access / checking | Publication status | Relation to question | Limit / next check |
| --- | --- | --- | --- | --- | --- | --- | --- |

Useful access values: full text, abstract only, supplied excerpt, user report, metadata only, unavailable. Useful checking descriptions: excerpt checked, methods/table checked, metadata/status checked, participant data checked, not checked in this run. Publication status: published, preprint, corrected, expression of concern, retracted, not applicable, or unknown. Preserve applicable details and dates rather than forcing multiple statuses into one word.

Source ID and page/section/table/figure/paragraph make the entry recoverable. Record PDF page numbers separately from printed page numbers. An inaccessible full text limits the inference; it does not require discarding a usable abstract-level answer.

## Numerical and causal boundaries

- Keep the measured outcome, proxy outcome, population/model, comparator, time, and unit of analysis distinct.
- Track who/what entered the study and who/what entered each analysis. Missing observations are not automatically zero; a measured zero is not missing. State the target population and denominator of an estimate.
- Preserve mean, median, range, SD, SE, and interval labels. A difference of displayed medians is not a difference of means. A p-value does not supply an effect estimate or its confidence interval.
- Distinguish allocation by alternation from random assignment. A non-significant baseline comparison does not establish exchangeability.
- Distinguish association, intervention effects under a design's assumptions, and mechanism. Sufficiency under specified experimental conditions is not necessity in the native system or a complete mechanism.
- Keep effect size, precision, selection, multiplicity, and applicability separate from statistical significance. Unsupported probabilities or likelihood ratios stay unestimated.
- A retraction changes evidential use, not the truth value of every possible related hypothesis. Search independent evidence when a substantive conclusion still matters.

## AI discovery and conflicting evidence

AI summaries and retrieval displays are leads until a material source claim is checked. Mark the substantive claim U while recording the display separately as an attributed report; do not upgrade it to a verified empirical finding. If the research object is an AI system, documented outputs may themselves be observations about it. Compare design/context, shared datasets and selection before combining findings. A support percentage is neither a pooled effect nor an evidence-certainty score. See [AI judgment](ai-judgment.md) for proportionate source checks and method boundaries.

## Formal five-branch map

Central node: one complete provisional research question, or the original broad question explicitly marked as not yet focused.

1. **Problem:** construct, importance, population/model, factor, comparison, observable outcome and context.
2. **Evidence:** source reports and the actual scope of support.
3. **Key unknown:** the most consequential unresolved uncertainty.
4. **Other explanations:** credible alternatives and their different predictions.
5. **Next evidence:** the observation, source, comparison, or design that could change the judgment.

Give important nodes stable IDs when linking maps, ledgers, alternatives, and revisions. Put E/A/U on substantive nodes; headings need no epistemic tag. A proposed question/test is A-proposal; a missing result is U. Do not call a proposed next experiment E.

Use a Mermaid `mindmap` for hierarchy. Hierarchical nesting does not assert causation. For a specific evidence chain, add a small `flowchart` with edges labeled **observed association**, **causal hypothesis**, or **unverified link**. A proposed design can be described beside the diagram; arrows do not prove identification.

## Four-branch introductory map

The course's introductory view uses **Define, Evidence, Alternatives, Next checks**:

| Introductory branch | Formal branch |
| --- | --- |
| Define | Problem |
| Evidence | Evidence |
| Alternatives | Other explanations |
| Next checks: what remains uncertain | Key unknown |
| Next checks: where/how to check it | Next evidence |

The introductory [H] label becomes A-hypothesis/proposal and [?] becomes U. E is retained with source status attached. This is a documented normalization, not a claim that the original slides used one notation throughout.

## Revision record

Keep: original question/judgment; feedback or new evidence; owner; Accepted / Partly accepted / Not accepted / Need verification; reason; revised question or justified retention; next check. In analyze mode these are the researcher's or analyst's stated decisions, labeled by owner. In coach mode learner decisions are recorded only after the learner supplies them.
