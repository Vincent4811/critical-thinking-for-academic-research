# Critical Thinking for Academic Research

[English](README.md) · 版本 0.2.1

Evidence-aware reasoning, student coaching, and teaching design.

這套可攜式研究思考 Skill，以 Vincent 的 **Critical Thinking for Academic Research** 課程為核心，協助個人研究分析、學生指導與可操作的 Critical thinking 課程活動設計。

**初始判斷 → Challenge → Define → Evidence → Alternatives → Revise → 下一項證據。**

目標是形成可回答的研究問題、清楚的證據界線，以及可能改變判斷的下一步。判斷有根據時可以保留原題，不必為了「修訂」而改寫。

## 開始使用

讓支援 Agent Skills 的助理讀取 [SKILL.md](SKILL.md)，或將整個資料夾放入該工具支援的技能位置。保留 references 與 templates 的相對位置，不要只複製入口檔。

```text
用 critical-thinking-for-academic-research 分析這個研究問題與我提供的論文。
區分論文實際報告、我的假設、尚未確認的未知，提出下一項有判別力的證據。
```

```text
用 critical-thinking-for-academic-research 指導學生。先保留他的原始問題與理由，
每輪只問一個關鍵問題，最後由學生決定是否修訂。
```

實際互動預設繁體中文與臺灣術語，英文術語、標識符及來源引文保留原文。可明確要求英文輸出。使用本 Skill 不需要執行程式、付費 API、connector 或其他已安裝技能；需要查核來源時，使用所在環境已授權的讀取與搜尋工具，無法取得的內容明確標示。

## 三種模式

| 模式 | 使用時機 | 交付 |
| --- | --- | --- |
| `analyze` | 研究者要求分析、聚焦研究問題或檢視論證 | 直接完成有依據的分析，列出暫定判斷及缺少的證據 |
| `coach` | 實際指導學生、現場練習、Research Question Clinic | 保存學生最初判斷，每輪問一個問題，修訂由學生決定 |
| `design-lesson` | 教師要求備課、活動、工作坊、學習單或評量設計 | 完整時間表、材料與規則、預備提問、學生產物、修訂與 exit assessment |

依使用意圖選擇模式，不增加模式訪談；明確指定時依指定模式執行。要求完整示範時，清楚標示為示範，不偽造學生回答。

教師備課優先使用 `design-lesson`，不是現場 `coach`；可一次備妥整組教師提示，一次一問的限制只適用於實際學生對話。

```text
用 critical-thinking-for-academic-research 設計 120 分鐘 Critical thinking 課程活動，
包含可操作規則、個人思考、同儕挑戰、研究問題圖、修訂與 exit ticket。
```

## 文件與範本

- [完整方法，繁體中文](docs/method.zh-TW.md) / [English](docs/method.en.md)
- [研究分析範本](templates/analysis.zh-TW.md) / [English](templates/analysis.en.md)
- [MindMap 與關係線範本](templates/mindmap.zh-TW.md) / [English](templates/mindmap.en.md)
- [學生指導紀錄](templates/coach-session.zh-TW.md) / [English](templates/coach-session.en.md)
- [三組範例與證據界線](examples/README.md)
- [120 分鐘工作坊及 50 分鐘縮短版](teaching/lesson-120.zh-TW.md) / [English](teaching/lesson-120.en.md)
- [六張教師活動卡](teaching/activity-cards.zh-TW.md) / [English](teaching/activity-cards.en.md)
- [課程活動設計範本](templates/lesson-plan.zh-TW.md) / [English](templates/lesson-plan.en.md)
- [個人學習單](templates/classroom-worksheet.zh-TW.md) / [English](templates/classroom-worksheet.en.md)
- [課程頁碼、研究來源與改寫紀錄](references/source-map.md)

正式 MindMap 採五分枝與 E/A/U。E 代表有可追溯來源的報告，不代表該主張已確立；來源取得程度、核對範圍與撤稿狀態分開記錄。四分枝圖保留為入門練習，並對照到正式版本。

## 驗證與發布

套件結構檢查使用 Python 3.10+：

```sh
python scripts/validate_package.py
```

此檢查涵蓋連結、metadata、發布內容、來源紀錄與明顯的私密路徑污染；Mermaid 與代理實際行為另依 [驗證說明](evals/README.md) 檢查。結構檢查通過不等於研究推理正確，也不代表已測得能力提升。

五步循環、遊戲與學生修訂自主性來自課程；部分思考機制改寫自 [cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills)，版本固定於 [UPSTREAM.json](UPSTREAM.json)。原創套件採 [MIT](LICENSE)，上游授權與署名保留於 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。原始 PDF、第三方圖像、學生作業、未公開資料及本機來源路徑不在公開套件中。

這是研究思考與教學輔助框架，尚非經驗證的測量工具，也不取代完整研究設計、統計方法或倫理審查。
