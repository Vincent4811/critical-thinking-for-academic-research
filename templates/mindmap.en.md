# Evidence-aware question map

Replace the quoted placeholders with the current question and short claims. The authoritative [map rules](../references/evidence-and-maps.md) define labels, evidence status, branch mapping, and edges.

## Formal five branches

```mermaid
mindmap
  root["My provisional research question"]
    Problem
      P1["A-proposal: population, factor, comparison and outcome"]
    Evidence
      E1["E-report: source and locator; checking/status stated"]
    Unknown["Key unknown"]
      U1["U: the most consequential unresolved fact"]
    Other["Other explanations"]
      A1["A-hypothesis: credible alternative and prediction"]
    Next["Next evidence"]
      N1["A-proposal: a check that could change the judgment"]
```

The hierarchy groups ideas; it does not prove a causal chain.

## Label a consequential relationship separately

```mermaid
flowchart LR
  E1["E-report: observed measurement"] -->|"observed association"| E2["E-report: measured outcome"]
  A1["A-hypothesis: proposed mechanism"] -.->|"causal hypothesis"| E2
  U1["U: unmeasured link"] -.->|"unverified link"| A1
```

Add source IDs/status beside the diagram or in its ledger. A hypothetical example with no empirical data uses A/U labels instead of E-report.

## Four-branch entry exercise

```mermaid
mindmap
  root["My original question"]
    Define
      D1["Who or what, factor, observable result"]
    Evidence
      E1["What the source reports and its limit"]
    Alternatives
      A1["Another explanation and differing prediction"]
    Checks["Next checks"]
      U1["What remains unknown"]
      N1["Where or how to check it"]
```

When ready, split Next checks into Key unknown and Next evidence; rename Define to Problem and Alternatives to Other explanations. Normalize introductory [H] to A-hypothesis/proposal and [?] to U.
