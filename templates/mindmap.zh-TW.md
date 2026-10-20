# 帶有證據標記的研究問題圖

將引號內的範例文字換成當前問題與短句。標記、來源狀態、關係線及分枝對照統一見 [map rules](../references/evidence-and-maps.md)。

## 正式五分枝

```mermaid
mindmap
  root["我的暫定研究問題"]
    Problem["Problem 問題"]
      P1["A-proposal：對象、因素、比較、結果"]
    Evidence["Evidence 證據"]
      E1["E-report：來源與位置；另列核對及發表狀態"]
    Unknown["Key unknown 關鍵未知"]
      U1["U：最會影響判斷的未知"]
    Alternatives["Other explanations 其他解釋"]
      A1["A-hypothesis：合理替代解釋與不同預測"]
    Next["Next evidence 下一項證據"]
      N1["A-proposal：能改變判斷的查核"]
```

分枝只整理概念，不證明因果關係；真正的觀察、推論與提案仍要分別標示。

## 重要關係另畫並標示

```mermaid
flowchart LR
  E1["E-report：觀察到的測量"] -->|"觀察到的關聯"| E2["E-report：測得的結果"]
  A1["A-hypothesis：提出的機制"] -.->|"因果假說"| E2
  U1["U：尚未測量的連結"] -.->|"待確認連結"| A1
```

圖旁附來源 ID、核對範圍與發表狀態，或連到證據表。完全假設性的情境以 A/U 取代 E-report，不偽裝成觀察結果。

## 四分枝入門練習

```mermaid
mindmap
  root["我的原始問題"]
    Define["Define 定義"]
      D1["對象、因素、可觀察的結果"]
    Evidence["Evidence 證據"]
      E1["來源實際報告與限制"]
    Alternatives["Alternatives 其他解釋"]
      A1["另一種解釋及其不同預測"]
    Checks["Next checks 下一項查核"]
      U1["什麼還不知道"]
      N1["去哪裡、如何查核"]
```

進階時，把 Next checks 分成 Key unknown 與 Next evidence；Define 對應 Problem，Alternatives 對應 Other explanations。入門標記 [H] 對應 A-hypothesis/proposal，[?] 對應 U。
