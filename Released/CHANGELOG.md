# 日語學習 App — 版本記錄

## v0.14.17 — 2026-06-23

**拍照 OCR 流程改為手動觸發**
- 選完圖後先顯示預覽，不再自動送出 API
- 預覽下方出現「開始辨識」按鈕，使用者確認後才呼叫 Google Vision
- 新增「重新選圖」按鈕可回到選擇畫面
- 辨識完成後「開始辨識」再次出現，可重試同一張圖

---

## 0.14.17 — 2026-06-23

拍照OCR改為手動觸發：選圖→預覽→確認辨識，新增重新選圖按鈕

---

## v0.14.16 — 2026-06-23

**設定頁：CSV 匯入單字本**
- 資料區新增「匯入單字本」按鈕，選取 CSV 檔案後自動解析
- 與現有單字合併：已存在的單字保留原有熟悉度，不覆蓋
- 支援從本 App 匯出的 CSV 格式（單字/讀音/羅馬拼音/中文/熟悉度/加入日期）
- 匯入完成後 toast 顯示新增與跳過數量

---

## 0.14.16 — 2026-06-23

設定頁：新增 CSV 匯入單字本功能，與現有資料合併不覆蓋

---

## v0.14.15 — 2026-06-23

**設定頁功能調整**
- 學習強度「熟記定義」可調整：點擊循環 10/12/14/16/18/20 次，對應 vocabLevel 熟悉門檻
- 移除三個無功用的顯示設定：羅馬拼音、Furigana顯示、中文備注預設
- 語言 > 目前等級：等級 chips 預設折疊，點擊目前等級格才展開
- 開發工具新增「初始化使用者」：清空所有資料並重置等級為 N5-（新手狀態）
- 開發工具新增「老手模擬」：填入過去 7 天完整學習紀錄 + 20 個熟悉單字

---

## v0.14.14 — 2026-06-23

**試題頁等級獨立修正**
- `selectQuizDate` 改為優先讀取 studyLog 中該日期存的等級，與文章頁邏輯一致
- 若該等級檔案不存在，自動 fallback 到 n5（修復切換文章等級後試題頁其他日期無法載入的問題）
- 試題每天獨立，文章等級的變更不會影響已完成的試題紀錄

---

## 0.14.14 — 2026-06-23

試題頁等級獨立：讀per-date level+n5 fallback，不再受文章等級切換影響

---

## v0.14.13 — 2026-06-23

**月曆三修**
- **Bug #1**：月曆日期展開面板不顯示文章標題 → `selectArticleDate` 現在一併儲存 `articleTitle` 到 studyLog
- **Bug #2**：今日（23號）及後續日期不顯示 → 根本原因：`selectArticleDate` 建立了無 `tasks` 欄位的 entry，`countDone(undefined)` 報錯中斷 `renderCalendar` → 補上 `tasks` 初始化與 `countDone` 防護
- **Bug #3**：月底最後一週尾端空白 → 補上下個月首幾日（灰色），讓每行都滿 7 格

---

## 0.14.14 — 2026-06-23

vocab查詢補surface_form fallback；生成prompt強化key一致性與自我檢查

---

## v0.14.12 — 2026-06-23

**等級選擇 sheet 按鈕修正**
- `N5⁻` 上標字元改為普通 `N5-`，"-" 不再縮小看不清
- 所有 chip 統一固定寬高（56×36px），上下兩排完全對齊

---

## 0.14.13 — 2026-06-23

toast：半透明磨砂效果（0.38不透明+blur16px）；位置nav上116px

---

## 0.14.13 — 2026-06-23

toast：半透明磨砂效果（0.38不透明+blur16px）；位置nav上116px

---

## 0.14.12 — 2026-06-23

等級chip：-符號改普通字元；固定寬高上下對齊

---

## v0.14.11 — 2026-06-23

**等級選擇 sheet UI 重排**
- 10 個等級改為兩排置中：上排 N5→N1，下排 N5⁻→N1⁻
- 背景遮罩不透明度 0.35 → 0.45，並加入 `backdrop-filter: blur(6px)` 打霧效果

---

## v0.14.10 — 2026-06-23

**電腦版文章等級長按修正**
- 桌面長按等級標籤無法開啟選擇框 → 改用 `pointerdown`/`pointerup`/`pointerleave` 取代 touch-only 事件，觸控與滑鼠通用

---

## v0.14.9 — 2026-06-23

**每篇文章獨立等級 + 難度評分修正**
- 文章難度星星評分改寫入當前瀏覽日期（原本固定寫入今天）
- 每篇文章有獨立的等級記憶：長按等級切換後，該日期會記住選擇（存入 studyLog）
- 從月曆/週欄跳轉到過去文章，優先讀取該日上次的等級，若檔案不存在自動 fallback 到 n5（修復 22 號「無法存取」）
- `reloadArticleWithLevel` 不再更改全局 CURRENT_LEVEL，只更新當日等級

---

## v0.14.8 — 2026-06-23

**進度即時更新全修**
- 新增 `refreshProgressUI()` 統一呼叫首頁大環 + 月曆 + 週欄三個 render
- 文章進度（scroll/朗讀）、跟讀、試題、單字卡完成後現在即時更新全部 UI，不需跳頁
- 單字卡進度原本只在首頁時才更新，改為隨時更新
- 清空今日紀錄與清空全部資料後也即時重繪

---

## 0.14.8 — 2026-06-23

進度即時更新：refreshProgressUI統一三環，不再需要跳頁才更新

---

## v0.14.7 — 2026-06-23

**文章頁週欄三修**
- **Bug #1**：從月曆點日期跳轉文章頁，週欄沒跟著切換到目標週 → `selectArticleDate` 更新 `weekBarOffset` 後現在立即呼叫 `renderWeekBar()`
- **Bug #2**：18–22 日在週欄被淡化、無進度環 → `hasContent` 改為同時檢查 `contentDateSet`，有文章的日期一律顯示進度環軌道與亮色文字
- **Bug #3**：22 日進度未反映到週欄 → 同 #2 修法，週欄現在與 `contentDateSet` 一致

---

## v0.14.6 — 2026-06-23

**月曆進度環未顯示 bug 修正**
- 文章有部分進度（如 30%）但月曆仍顯示大點而非進度環 → 根本原因：`countDone` 只計算「完全完成」的任務，article 30% 回傳 0 → 改為判斷「任何任務有任何進度」即顯示進度環

---

## v0.14.5 — 2026-06-23

**月曆三修（二）**
- **Bug**：18–22 日有文章卻無小點 → 根本原因是 `ARTICLES_WITH_CONTENT` hardcode 只到 6/21；改為啟動時從 `index.json` 動態讀取日期填入 `contentDateSet`，並以此判斷是否顯示點
- **UI**：小點與日期數字都不置中 → `.cal-d-num` 改為 `top:50%;left:50%;transform:translate(-50%,-50%)` 絕對置中；小點從 17px 放大至 22px
- **UI**：月曆選中圓再縮小 10px → `outline-offset: -3px → -8px`

---

## v0.14.4 — 2026-06-23

**月曆三項修正**
- **Bug**：過去日期（如18–22號）即使有文章也點不出下拉頁 → 所有非未來日期現在皆可點擊，`openDay` 移除「無學習紀錄就忽略」的早期返回
- **UI**：被選中日期的橘色圓圈縮小 5px（`outline-offset: 2px → -3px`）
- **UI**：月曆小底點改為「有學習紀錄或今日才顯示」，尺寸從 7px 放大至 17px；過去無紀錄的日期不再顯示點

---

## v0.14.3 — 2026-06-23

**Code review 後 8 個 bug 全修**
- **Bug #1**：`openArticleFromCalendar` 全新安裝時，從月曆點今日開啟文章，兩條載入路徑同時被封鎖（`articleRendered=true` + `selectArticleDate` 同日 early-exit），導致顯示 demo 假資料 → 現在判斷是否已載入，未載入時強制觸發 `selectArticleDate`
- **Bug #2**：`reloadArticleWithLevel` 切換等級後 `renderArticle` 被呼叫兩次（`applyContentPack` 內一次 + 外面一次），導致閃爍 → 移除外層多餘的 render
- **Bug #3**：`openDay` 今日無學習紀錄時，等級欄位永遠顯示硬寫的「N5」，無視 `CURRENT_LEVEL` → 改從 `LEVEL_OPTIONS` 查詢正確 label
- **Bug #4**：`cycleFollowDb` 若 localStorage 存有非 options 陣列內的值（如舊版 -45），`indexOf` 回 -1 導致靜默跳至 -30 → 改為 -1 時 fallback 到預設值 -40
- **Bug #5**：測驗週欄仍使用 `getAvailableArticleDates()` 判斷有無內容，與文章週欄（改用 log entry）邏輯不同，同日顯示不一致 → 統一改用 log entry 邏輯
- **Bug #6**：設定頁變更等級後，文章頁顯示的內容不會重載，無任何提示 → 若目前在文章頁則顯示 toast 提示
- **Bug #7**：`reloadArticleWithLevel` 重複 `setUserLevel` 的三行邏輯 → 改直接呼叫 `setUserLevel(key)`
- **Bug #8**：月曆切換到歷史月份後，離開再回首頁，月曆仍停在上次切的月份 → 切回首頁時自動 reset 到今月

---

## 0.14.3 — 2026-06-23

code review 全修：月曆開文章空白、等級切換雙重render、N5硬寫、dB循環、週欄不一致等8個bug

---

## v0.14.2 — 2026-06-23

**文章頁等級標籤：長按切換難度（新功能）**
- 文章頁頂部等級標籤（如 N5⁻）長按 600ms → 彈出底部 sheet，顯示 10 個等級 chip
- 選擇後重新以該等級載入同日文章，同步更新 `CURRENT_LEVEL` 及 localStorage
- 桌面開發：右鍵點擊等級標籤也可觸發 sheet（方便測試）
- 等級標籤改為從 LEVEL_OPTIONS 對應 label（N5⁻/N5/N4⁻...），不再顯示原始 key
- Sheet 以 backdrop + slide-up 動畫呈現，點背景或選完關閉

---

## 0.14.2 — 2026-06-23

文章頁等級標籤長按 → 底部 sheet 切換難度

---

## v0.14.1 — 2026-06-23

**今日頁月曆與文章頁週曆多項互動 bug 修正**
- 月曆新增月份切換按鈕（‹ / ›），可瀏覽歷史月份；不允許切換至未來月份
- 修正今日無學習紀錄時，月曆 23 號無法點擊展開的問題
- `openDay` 今日無 entry 時仍展開 panel，顯示「今日文章 / N5」佔位文字
- `openArticleFromCalendar` 改為永遠呼叫 `selectArticleDate`，修正從月曆跳轉今日文章卻顯示舊文章的問題
- `selectArticleDate` 新增自動調整 `weekBarOffset`，確保跳轉文章後週曆同步顯示目標日期所在週
- `renderWeekBar` 移除 `ARTICLES_WITH_CONTENT` hardcode：改為有學習紀錄或今日的日期顯示進度環，所有非未來日期皆可點擊，載入失敗由 `loadContentForDate` toast 處理

---

## v0.14.0 — 2026-06-23

**10 階等級系統上線（新功能）**
- 等級從 N5/N4/N3/N2/N1（5 級）擴充為 N5⁻/N5/N4⁻/N4/N3⁻/N3/N2⁻/N2/N1⁻/N1（10 級）
- `CURRENT_LEVEL` 改從 localStorage（`userLevel`）讀取，重啟後保留
- 設定頁「語言」卡新增 10 個 level chip，點選即切換並即時存入 localStorage
- 文章頁/週曆點擊/試題頁載入：從 hardcoded `'n5'` 改為依 `CURRENT_LEVEL` 動態取對應 JSON
- Dev dashboard 等級按鈕更新為 10 個（N5⁻ ～ N1），切換時同步 localStorage 與設定頁 UI
- 排程任務（daily-jp-content）已更新為每天生成 10 份 JSON（n5_lite ～ n1）

---

## v0.13.1 — 2026-06-23

**逐句跟讀靜音偵測：預設調整 + 設定頁可調（bug fix + 小功能）**
- 靜音門檻預設 -50dB → -40dB，靜音持續時間 2s → 1s，更貼近自然說話節奏
- 設定頁新增「跟讀設定」卡，提供兩個可點擊循環調整的項目：
  - 靜音門檻：-30 / -40 / -50 / -60 dB
  - 靜音持續時間：0.5 / 1.0 / 1.5 / 2.0 秒
- 設定值存入 localStorage（`followSilenceDb` / `followSilenceSec`），重啟後保留

---

## 0.13.1 — 2026-06-23

逐句靜音偵測預設 -40dB/1s；設定頁可調門檻與時間

---

## v0.13.0 — 2026-06-23

**試題頁：句子判斷 / 句子排列 兩大題型正式上線（新功能）**
- 解鎖試題頁「句子判斷」與「句子排列」Tab，全客戶端動態生成，不依賴 GitHub 端額外產物
- **句子判斷**：取文章句子 + translations 翻譯，隨機抽 50% 正確、50% 錯誤（換用其他句翻譯），使用者判斷 ✓ 正確 / ✗ 錯誤；答錯時顯示正確翻譯
- **句子排列**：從 tokens 按句子分組，去除標點、打亂詞序成 chip 池；使用者點選 chip 依序放入排列區，排錯可點回收，全部放完才可確認
- 抽取共用 helper `splitTokensIntoSentences()`，`generateFillInQuestions` 同步使用
- 題目數量皆受 `getModeVocabPct()` 控制（easy/normal/focus），難度自適應
- `saveQuizResults` 已支援 judge / order 存入 quiz log（不計入首頁任務環，留待後續擴充）
- 結果頁答錯回顧支援四種題型格式

---

## 0.13.0 — 2026-06-23

句子判斷 / 句子排列 兩題型上線

---

## v0.12.0 — 2026-06-23

**逐句跟讀：靜音偵測自動結束錄音窗口（新功能）**
- 以 Web Audio API（AudioContext + AnalyserNode）取代固定計時器，每 100ms 取一次 RMS 音量
- 音量低於 -50dB 持續 2 秒（連續 20 次靜音）→ 自動結束當句跟讀、播下一句
- 最長 30s 硬上限兜底（AudioContext 不可用時也有效）
- 狀態列改顯示秒數上數（不再倒數），更直覺反映「唸完就停」的感受
- AudioContext 不可用時降級無聲運行，不阻斷流程
- `_cleanFollowDetection()` 統一清理 AudioContext 與 poll，在完成/中途停止時呼叫

---

## 0.12.0 — 2026-06-23

逐句跟讀：靜音偵測（-50dB 持續 2s）自動結束錄音窗口

---

## v0.11.2 — 2026-06-22

**文章頁漏字修正：所有詞彙皆可長按**
- 修正：`renderArticle` 只有 vocab dict 中的詞才有互動，造成 AI 生成內容中未收錄到 vocab 的詞無法長按、無法加入單字本
- 改為以正規表示式判斷是否含日文/英文字元，凡含字元的 token 皆渲染為可互動 `tok-word`，純標點符號才走 `tok-plain`
- `openWordPanel` 已有 fallback `{ meaning: '（尚無中文翻譯）' }`，不影響顯示
- 同步更新 `content/SCHEDULED_TASK_PROMPT.md`，強調 vocab 必須收錄所有名詞/動詞/形容詞/副詞 token

---

## 0.11.2 — 2026-06-22

文章頁漏字修正：所有詞彙皆可長按

---

## v0.11.1 — 2026-06-22

**月曆點擊文章跳轉錯誤修正（bug fix）**
- 修正呼叫不存在的 `switchArticleDate`（改為正確的 `selectArticleDate`）
- 修正 race condition：非今天日期時先設 `articleRendered = true`，阻止 `switchPage` 非同步載入今日文章，再由 `selectArticleDate` 獨立載入指定日期內容

---

## 0.11.1 — 2026-06-22

fix：月曆點文章跳轉錯誤（selectArticleDate + race condition）

---

## v0.11.0 — 2026-06-22

**逐句跟讀：TTS 播放期間不錄音（新功能）**
- 改用 `MediaRecorder.pause()` / `.resume()` 控制錄音窗口：start 後立即 pause，僅在跟讀窗口 resume，TTS 播放聲音不再混入音檔
- 流程：start（pause）→ TTS → resume（跟讀計時）→ pause → TTS → … → stop
- 仍維持單一連續 blob，無需合併
- 完成/中途停止的判斷同步更新為 `state === 'recording' || state === 'paused'`

---

## 0.11.0 — 2026-06-22

逐句跟讀：TTS 期間 pause 錄音，跟讀窗口才 resume

---

## v0.10.3 — 2026-06-22

**逐句跟讀：中途停止保留錄音 + 跟讀窗口加長（bug fix）**
- 修正中途停止不存檔：移除 `_stopFollowMode` 中覆蓋 onstop 的丟棄邏輯，改為直接呼叫 `stop()`，讓原 save handler 執行並存入槽位
- 時長估算改以實際完成的句子數（`_followIdx`）計算，避免中途停止時高估
- 跟讀窗口乘數 1.3 → 1.6（每句跟讀時間更充裕）

---

## 0.10.3 — 2026-06-22

逐句中途停止保留錄音；跟讀窗口 1.6x

---

## v0.10.2 — 2026-06-22

**一般錄音 iOS Safari 存檔修正（bug fix）**
- 修正跟讀錄音按鍵停止後音檔未存入槽位：`mediaRecorder.start(1000)` 加入 timeslice，確保 iOS Safari `ondataavailable` 穩定觸發，避免 `recordedChunks` 為空導致不存檔

---

## 0.10.2 — 2026-06-22

fix：一般錄音 iOS Safari timeslice，修正槽位未存檔

---

## v0.10.1 — 2026-06-22

**逐句跟讀 iOS Safari 相容修正（bug fix）**
- 修正 TTS 靜音：`async _startFollowMode` 在 `await getUserMedia` 前先以 volume=0 的 warm-up utterance 觸發 iOS 語音權限，避免手勢上下文丟失後 TTS 被靜默阻擋
- 修正錄音不存：`_followMR.start(1000)` 加入 timeslice，每秒定期觸發 `ondataavailable`，確保 iOS Safari 收得到 chunks

---

## 0.10.1 — 2026-06-22

逐句跟讀 iOS fix：TTS warm-up + MediaRecorder timeslice

---

## v0.10.0 — 2026-06-22

**逐句跟讀模式（新功能）**
- 跟讀工具列新增「逐句」按鈕，點擊後進入逐句跟讀流程
- 流程：TTS 播放第 N 句 → 自動進入跟讀計時窗口（TTS 時長 × 1.3，最短 1.5 秒）→ 自動播下一句，直到全部結束
- 錄音為一條連續 blob（整段逐句共用同一 MediaRecorder），完成後存入當前槽位
- iOS Safari 相容：`onend` 不觸發時以估算時長（chars/sec × rate）+ 500ms 作為 fallback
- 狀態列即時顯示「播放第 N/M 句」/「跟讀第 N/M 句（Xs）」
- 活躍時「逐句」按鈕變紅顯示「停止」，一般錄音鍵暫時禁用；中途停止不儲存

---

## 0.10.0 — 2026-06-22

逐句跟讀模式：TTS播一句→自動計時錄一句，循環至段落結束

---

## v0.9.18 — 2026-06-22

**今日頁三項修正**
- 大環中央 5/5 數字垂直置中修正：`top: 38%` → `top: 96px`（精確對齊 152px SVG 的幾何中心）
- 月曆文章標題顯示修正：`logTodayArticle()` 完成後若 detail panel 已開啟，即時刷新標題（修正 async fetch 早於使用者開啟面板的競態問題）；`switchArticleDate()` 切換回今日時亦同步儲存標題
- 月曆點擊文章 → 跳轉文章頁：`.detail-article` 加入 `openArticleFromCalendar()`，關閉 detail panel 並切換到文章頁；若選取的非今日，自動載入該日文章

---

## 0.9.18 — 2026-06-22

今日頁：5/5置中、月曆文章標題修正、點文章跳轉文章頁

---

## v0.9.17 — 2026-06-22

**週曆錄音 badge 位置修正**
- `cx=30,cy=8` → `cx=33,cy=5,r=3`：點移到環外側，不再與弧環重合

---

## 0.9.17 — 2026-06-22

週曆錄音badge位置修正：移到環外側右上角

---

## 0.9.17 — 2026-06-22

週曆錄音badge位置修正：移到環外側右上角

---

## v0.9.16 — 2026-06-22

**週曆錄音 badge 修正**
- 錄音小點移入 SVG 右上角（badge 形式），不再佔 layout 空間 → 高度跳動問題消失
- 移除 `e.preventDefault()` + 改 `passive:true` → 短按可正常觸發 `selectArticleDate`（之前 preventDefault 壓制了 click 事件導致有錄音的日期無法選取）

---

## 0.9.16 — 2026-06-22

週曆錄音badge修正：小點移右上角SVG、修短按無法選日期bug

---

## v0.9.15 — 2026-06-22

**文章週曆圓圈 3 項更新**
- 上下半弧：上半弧 = 文章閱讀進度（橘），下半弧 = 跟讀進度（紫），各自獨立顯示
- 長按不再觸發系統選字：`.awb-day` 加 `-webkit-user-select:none; -webkit-touch-callout:none`
- 週曆高度一致：無錄音日期也渲染小點容器（`visibility:hidden`），消除切換時的跳動

---

## 0.9.15 — 2026-06-22

週曆上下半弧：上橘=文章/下紫=跟讀；修長按選字；修小點跳動

---

## v0.9.14 — 2026-06-22

**跟讀錄音管理 2 項修正**
- 週曆長按有錄音的日期（600ms）→ 直接跳出「確認清除此日錄音」對話框
- 設定頁「跟讀錄音管理」section 加展開/收合按鈕（▼/▲），預設收合，防止音檔多時頁面過長

---

## 0.9.14 — 2026-06-22

跟讀管理：週曆長按清除此日錄音、設定頁section收合

---

## 0.9.14 — 2026-06-22

跟讀管理：週曆長按清除此日錄音、設定頁section收合

---

## v0.9.13 — 2026-06-22

**Onboarding 三頁文案 + SVG 視覺修正**
- 頁1 文案更新：強調朗讀引導與沈浸式學習
- 頁2 文案更新：明列四大功能（文章輔助、SRS 單字、跟讀輔助、快捷測驗）
- 頁2 SVG 顏色統一：四個功能卡片顏色改為對應今日頁任務指標色（#D85A30 / #1D9E75 / #378ADD / #7F77DD）
- 頁2 SVG 圖示縮小：耳機、麥克風縮小至與書本、單字卡相同大小（~22px）
- 頁3 文案分段：說明拆成兩行，「五個練習都完成，今天就圓滿了！」獨立第二段
- 頁3 SVG 比例調整：環整體下移 2px 改善垂直置中、5/5 合為單行文字（size 15）、指標點縮小（r=4）、標籤放大（size 10）、底部留白收緊

---

## 0.9.13 — 2026-06-22

Onboarding 三頁文案更新 + 頁2顏色統一 + 圖示縮小 + 頁3 SVG 比例修正

---

## v0.9.12 — 2026-06-22

**跟讀錄音按日期儲存**
- IndexedDB key 由純 slot 數字改為 `{date}-{slot}`（DB schema v2，舊錄音自動清除）
- 切換文章週曆日期時，跟讀三個槽位自動切換至當天的錄音（舊 blob URL 釋放）
- 補錄歷史日期時，進度寫入那天的 studyLog（而非固定寫今天）
- 文章週曆：有跟讀錄音的日期下方顯示橘色小點
- 設定頁新增「跟讀錄音管理」section：列出有錄音的日期，可逐日刪除或全清

---

## 0.9.12 — 2026-06-22

跟讀錄音按日期儲存：切換週曆日期自動切換槽位、週曆顯示錄音點、設定頁管理錄音

---

## v0.9.11 — 2026-06-22

**Page 3 Onboarding SVG 重設計（第二版）**
- 完全重做：以「今日頁大環 + 五項練習指標」為視覺主軸
- 環使用與 buildRing 完全相同的 stroke-dasharray 算法（cr=43, sw=14, circumference=270.18）
- 五個色段全填滿，呈現「今日完成」理想狀態
- 環中心顯示「5/5」表示五項全完成
- 下方五個彩色圓點 + 對應標籤（文章/單字/聽力/填空/跟讀），顏色與環段一致
- 標題改為「每天五個任務」，說明改為「大環代表今天的進度。五個練習都完成，今天就圓滿了！」

---

## 0.9.11 — 2026-06-22

Page 3 重設計：今日環 + 五項任務指標

---

## v0.9.10 — 2026-06-22

**4 項 Bug 根本原因修正**
- 聽力播放無聲：`JSON.stringify` 產生雙引號破壞 onclick 屬性解析，改用 `data-word` attribute + `this.dataset.word`
- 填空結果框：改為有色底框（綠/紅背景 + 深色文字），確保亮暗模式下均清晰可見
- 試題載入中：加 `AbortController` 8 秒 timeout，防止 fetch 在 iOS 上永久 hang
- 長按觸發系統選取：`e.preventDefault()` 移至 touchstart 立即執行（原在 setTimeout 回呼已來不及攔截）

---

## 0.9.10 — 2026-06-22

4項bug根本原因修正：播放無聲/填空結果框/試題timeout/長按選字

---

## v0.9.9 — 2026-06-22

**Page 3 SVG 視覺重設計**
- 舊設計：文字寫在圓圈內部與圖示重疊，兩條曲線箭頭交叉
- 新設計：4 步驟水平排列（今日任務→文章閱讀→練習答題→今日完成），3 條直線箭頭向右
- 文字全部放圓圈外下方，圖示與文字完全分離
- 背景細橫條作為視覺軌道，第 4 步圓圈更大更深為視覺重點

---

## 0.9.9 — 2026-06-22

Page 3 SVG 重設計，水平四步驟，文字移到圓圈外

---

## v0.9.8 — 2026-06-22

**修正 obNext() 永遠跑 finishOnboarding 的根本原因**
- 診斷確認：`_obTotal` 在 iOS Safari 執行時為 `undefined`（原因不明，可能是 iOS Safari var hoisting 邊界情況）
- 結果：`1 < undefined` → `false` → 每次按下一步直接呼叫 `finishOnboarding()`，onboarding 消失
- 修法：`obNext()` 內部改用 `var OB_TOTAL = 3`（local const），完全不依賴外部 `_obTotal` var
- `devRestartOnboarding()` 迴圈也改為直接用 `3`
- slides 2、3 DOM 已確認存在（v0.9.6 SVG 修正有效），此版修完後三頁應可正常切換

---

## 0.9.8 — 2026-06-22

修正 obNext 永遠跑 finishOnboarding，OB_TOTAL 改 local var

---

## v0.9.7 — 2026-06-22

**Onboarding 診斷工具 + 防呆**
- `obNext()` 加 try/catch，元素 null 時顯示 `alert('[OB] ob-slide-N 找不到')` 而非靜默失敗
- `showSplash()` 將結果寫入 `sessionStorage._obSplashResult`（shown / skipped:reason）
- 開發工具新增「診斷」按鈕，呼叫 `devDiagOnboarding()`，alert 出完整 DOM 狀態、localStorage 值、slide active 狀態、children 數量

---

## 0.9.7 — 2026-06-22

Onboarding 診斷工具，obNext 防呆 alert

---

## v0.9.6 — 2026-06-22

**Onboarding SVG 修正（頁2、頁3無法顯示的根本原因）**
- 頁2、頁3 SVG 內含 `<text>emoji</text>` 元素（📖🃏🎧🎤☀️✏️🎯）
- iOS Safari 渲染 SVG `<text>` 內的 emoji 會失敗，導致整個 SVG 損壞、slide 無法顯示
- 全數換成純幾何形狀：book（rect+spine）、flashcard（rect+rotate）、headphones（arc path+rect）、microphone（rect+path）、sun（circle+line rays）、pencil（rect+polygon）、star（polygon path）
- `<text>` 保留只用於中文標籤（「文章閱讀」「今日完成！」等，無 emoji）

---

## 0.9.6 — 2026-06-22

修正 onboarding 頁2頁3 SVG emoji 導致無法顯示

---

## v0.9.5 — 2026-06-22

**開發工具對齊修正（根本原因）**
- 開發工具 section 掉在 `.sec` 外面（`.sec` 在 Google Vision API 區塊後就關閉了）
- 移回 `.sec` 內，標題和卡片自動獲得正確的 16px 左右內縮

---

## 0.9.5 — 2026-06-22

開發工具移入 .sec，修正左右對齊

---

## v0.9.4 — 2026-06-22

**Onboarding 4 項修正**
- `finishOnboarding()` 改為移除 `.visible` class，不再設 `display:none`，解決第二次 `showOnboarding()` 失效的問題
- Dev「重新啟動教學」：先重播 splash animation（2.4s），再顯示 onboarding，可無限重複使用
- Splash JS timer 從 2500ms 調整為 2600ms，與 CSS 2.4s animation 保持 200ms buffer
- 幻燈片換頁邏輯維持正確（修根本 display 問題後三頁自然可切換）

---

## 0.9.4 — 2026-06-22

Onboarding 4項修正：display:none → removeClass + 重播 splash

---

## v0.9.3 — 2026-06-22

**開發工具 section-title 對齊修正**
- 改用 `<p class="section-title">` 結構，與其他 section 完全一致
- 移除 `.setting-row` 包覆，消除左右邊距差異

---

## 0.9.3 — 2026-06-22

開發工具 section 對齊修正

---

## v0.9.2 — 2026-06-22

**3 項 Bug 修正**
- 開發工具 section：改為可收合（▼/▲ 切換），樣式與其他 section 一致
- Onboarding 不顯示：splash 結束後顯式 `display:none`；dev「重啟」按鈕直接展開不需重載頁面
- 雲端同步確認框移除：登入後若雲端較新，直接靜默覆蓋，不再跳出 confirm 對話框

---

## 0.9.2 — 2026-06-22

開發工具收合 + Onboarding 修正 + 移除同步確認框

---

## v0.9.1 — 2026-06-22

**Splash screen 修正：改為純 CSS animation**
- 原本靠 JS setTimeout 控制 fade-out，JS 出錯時 splash 永遠卡住
- 改用 CSS `@keyframes splashAnim`，不依賴 JS 即可自動消失
- `pointer-events: none` 確保即使 CSS 卡住也不會阻擋點擊
- JS 只負責 splash 動畫結束後觸發 onboarding

---

## 0.9.1 — 2026-06-22

Splash 改純 CSS animation，不再依賴 JS

---

## v0.9.0 — 2026-06-22

**起始畫面 + Onboarding + 開發工具**
- Splash screen：Bird Hide Learning logo fade-in/fade-out（2.5 秒）
- Onboarding 三頁（僅新使用者首次顯示）：SVG 插圖 + 說明文字 + 點點導航
  - 頁1：用真實文章學日語（書本閱讀插圖）
  - 頁2：四種學習模式（2×2 功能圖示）
  - 頁3：每日學習流程圖（步驟箭頭圖）
- `onboardingDone` localStorage flag，看完或跳過後不再顯示
- 設定頁新增「開發工具」section：重啟教學 / 清除今日 / 完整清空

---

## 0.9.0 — 2026-06-22

Splash + Onboarding + 開發工具

---

## v0.8.10 — 2026-06-22

**7項 Bug 修正**
- 月曆不更新：`switchPage/saveQuizResults/updateSpeakProgress` 補上 `renderCalendar()`
- 跟讀槽位：5個改回3個，進度計算改為 `/3`
- 新用戶文章：加 `getFirstUseDate()`，新用戶只看當天，老用戶從 studyLog 推算
- 試題載入中：區分「fetch 中」與「無內容」，失敗後顯示「今日試題尚未準備好」
- 試題黑框：`qz-next-btn` 改為橘色背景白字
- 聽力播放：改用 `qzPlayWord()` 加視覺回饋（播放中 → 再播放）
- 長按選字：`handleTokenLongPress` 前清除 `window.getSelection()`

---

## 0.8.10 — 2026-06-22

7項 bug 修正

---

## v0.8.9 — 2026-06-22

**自動同步（事件驅動 + visibilitychange）**
- `saveVocabBook()` / `saveStudyLog()` 末尾加 `autoSyncToCloud()`，覆蓋所有資料寫入出口
- `autoSyncToCloud()` debounce 3 秒，避免連續操作重複寫 Firestore
- `visibilitychange → hidden` 時立即同步（關閉 app 或切換分頁前保存）
- 未登入時自動跳過，不影響訪客使用

---

## v0.8.8 — 2026-06-22

**Firestore 雲端同步實作**
- `syncToCloud()`：上傳 vocabBook、studyLog、settings 到 Firestore（batch write）
- `syncFromCloud()`：從 Firestore 拉取資料覆蓋本機
- 登入後自動比較時間戳，雲端較新時提示是否覆蓋本機
- 同步按鈕啟用，顯示上次同步時間
- `_setSyncStatus()` 控制同步列狀態（syncing / done / error）

---

## 0.8.8 — 2026-06-22

Firestore 雲端同步實作

---

## v0.8.7 — 2026-06-21

**Google 登入改用 popup 模式（修正 iOS Safari ITP 問題）**
- `signInWithRedirect` 因 iOS Safari ITP 跨域限制，session 無法回傳 → `onAuthStateChanged` 永遠返回 null
- 改用 `signInWithPopup`，session 直接在同頁面處理，不涉及跨域
- popup 被封鎖時自動退回 redirect（桌面瀏覽器保險）
- 使用者關閉 popup 時恢復登入按鈕

---

## 0.8.7 — 2026-06-22

Google 登入改 popup 模式，修正 iOS Safari ITP 問題

---

## v0.8.6 — 2026-06-21

**帳號 UI 修正：時序競爭 + 已登入介面設計**
- 修正 `authStateKnown` flag，避免 Firebase auth state 尚未確認前顯示登入按鈕
- 登入成功後顯示 toast 提示「已登入：xxx」
- 已登入 UI：頭像 / 姓名 / Email + 登出按鈕（加邊框），下方同步狀態列（暫為 disabled）
- 移除 `signInWithGoogle` debug toast，改為正常錯誤提示

---

## 0.8.6 — 2026-06-21

帳號 UI 修正：authStateKnown + 已登入介面設計

---

## v0.8.5 — 2026-06-21

**Firebase 隔離 + quizOrder bug 修正**
- Firebase 初始化移至獨立 script 標籤，不受主程式例外影響
- updateQuizOrderUI fallback 由 'urgent'（已刪除）改為 'due'
- 這是導致 Firebase 從未初始化（Apps:0）的根本原因

---

## 0.8.5 — 2026-06-21

Firebase 隔離 + quizOrder bug 修正

---

## v0.8.4 — 2026-06-21

**Firebase 錯誤持久顯示 + storageBucket 格式修正**
- storageBucket 由 .firebasestorage.app 改為 .appspot.com（相容 SDK 9.23.0）
- firebaseInitError 變數：init 失敗時 renderAuthUI 顯示錯誤而非登入按鈕

---

## 0.8.4 — 2026-06-21

Firebase 錯誤持久顯示 + storageBucket 修正

---

## v0.8.3 — 2026-06-21

**Firebase 狀態偵錯**
- 點擊登入按鈕時顯示 firebase/fbAuth/apps 狀態

---

## 0.8.3 — 2026-06-21

Firebase 狀態偵錯

---

## v0.8.2 — 2026-06-21

**Firebase 偵錯：錯誤顯示在帳號區塊**
- 初始化失敗時直接在帳號卡片顯示錯誤訊息（不用 toast，不會消失）

---

## 0.8.2 — 2026-06-21

Firebase 偵錯顯示

---

## v0.8.1 — 2026-06-21

**Firebase 初始化偵錯**
- 加入 firebase.apps 重複初始化防護
- catch block 顯示實際錯誤訊息（偵錯用）

---

## 0.8.1 — 2026-06-21

Firebase 初始化偵錯

---

## v0.8.0 — 2026-06-21

**Firebase 初始化修正（TDZ bug）**
- const fbAuth/fbDb 改為 var，並包進 try-catch
- 修正 firebase.initializeApp 失敗時 fbAuth 停在 TDZ 導致後續操作全部 crash 的問題

---

## 0.8.0 — 2026-06-21

Firebase 初始化修正

---

## v0.7.9 — 2026-06-21

**登入錯誤診斷**
- signInWithGoogle 加入 try-catch，失敗時顯示 toast 錯誤訊息並恢復按鈕
- 確認 Firebase 已載入才執行登入
- _authLoginBtnHTML() 抽出為共用函式

---

## 0.7.9 — 2026-06-21

登入錯誤診斷

---

## v0.7.8 — 2026-06-21

**帳號登入按鈕修正**
- 登入按鈕改為直接寫在 HTML（不依賴 Firebase 非同步渲染），確保 iOS 上一定顯示
- 已登入時 renderAuthUI() 才替換為帳號資訊

---

## 0.7.8 — 2026-06-21

帳號登入按鈕修正

---

## v0.7.7 — 2026-06-21

**帳號區塊位置修正**
- 帳號區塊移至設定頁「語言」下方（原位置在 .sec 容器外導致對不齊）
- 切換至設定頁時主動呼叫 renderAuthUI()，修正按鈕不出現的時序問題

---

## 0.7.7 — 2026-06-21

帳號區塊位置修正

---

## v0.7.6 — 2026-06-21

**Firebase Auth 修正 + Firestore SDK**
- 登入改用 signInWithRedirect（修正 iOS Safari 無法彈出視窗問題）
- 加入 getRedirectResult() 處理 Google 回跳
- 加入 Firestore SDK，fbDb 全域變數備用
- 設計決策：訪客模式可用、最後存檔優先、錄音只存本機

---

## 0.7.6 — 2026-06-21

Firebase Auth 修正 + Firestore SDK

---

## v0.7.5 — 2026-06-21

**Firebase Auth：Google 登入**
- 加入 Firebase SDK（compat 版，不需 build system）
- 設定頁新增「帳號」區塊：未登入顯示 Google 登入按鈕，已登入顯示頭像/名稱/登出
- `currentUser` 全域變數供後續 Firestore sync 使用
- 授權網域需在 Firebase Console 加入 `cs90s203.github.io`

---

## 0.7.5 — 2026-06-21

Firebase Google 登入

---

## 0.7.5 — 2026-06-21

Firebase Google 登入

---

## v0.7.4 — 2026-06-21

**首頁五項指標標的重設**
- 文章：移除逐句錄音預留條件，改為捲到底+30%、朗讀1次+30%、朗讀≥3次+40%，總和可達 100%
- 聽力/填空：做完就算完成（不論分數）；原存答對率改為 `Math.max(score, 1)` 確保已完成標記
- 跟讀：槽位從 3 擴展為 5，每個錄音 ≥ 5 秒算有效，5 個全完成 = 100%（每個 +20%）
- 跟讀環形/圖例改為百分比漸進顯示（同文章/單字卡）

---

## 0.7.4 — 2026-06-21

首頁五項指標標的重設

---

## v0.7.3 — 2026-06-21

**設定頁調整 + 學習模式連動試題數量**
- 刪除「每日單字卡上限」與「每日練習時間」設定列
- 學習模式說明改為：輕鬆=複習40%單字・試題輕量、標準=75%・適中、專注=全部・完整
- 學習模式現在儲存至 localStorage（`learnMode`），切換設定頁時自動還原
- 試題聽力/填空題數依模式比例縮放（40% / 75% / 100%）

---

## v0.7.3 — 2026-06-21

設定頁調整・學習模式連動試題數量

---

## v0.7.2 — 2026-06-21

**複習排序：急迫優先 → 複習優先（SRS 到期）**
- 移除「急迫優先（生字先）」
- 新增「複習優先（到期先）」：依 `lastReviewed` + `familiarity` 算出逾期倍率，越久沒複習且熟悉度越低的排越前面
- SRS 間隔：生（0–6）= 1天、普（7–13）= 3天、熟（14–20）= 7天
- `vqRate` 現在會記錄 `lastReviewed` 到 vocabBook

---

## v0.7.1 — 2026-06-21

**朗讀：句間暫停 0.5 秒**
- 改為逐句播放（每句各自一個 `SpeechSynthesisUtterance`），句尾觸發 `setTimeout(500ms)` 後再播下一句
- 暫停/停止鍵同時清除句間計時器（`clearTimeout`），避免停止後仍觸發下一句
- 速度調整中斷播放後，也清除計時器並重建 queue 從頭播放

---

## v0.7.1 — 2026-06-21

試題頁聽力+填空引擎 + 朗讀句間暫停

---

## v0.7.0 — 2026-06-21

**試題頁 Phase 1：聽力 + 填空實作**
- 移除舊 mockup（單字 tab 及全部靜態題目）
- 新增試題週曆列（雙弧圓：上弧=聽力藍 #378ADD，下弧=填空棕 #BA7517）
- 造題引擎：從 n5.json vocab 自動生成聽力選擇題（最多 10 題）；從 tokens 挖空生成填空題（最多 10 題）
- 聽力：TTS 播放單字 → 選正確中文意思（4 選 1，3 個干擾選項來自同篇文章）
- 填空：顯示挖空句子 + 中文提示 → 自由輸入日文（支援輸入法，接受漢字或假名）
- 作答流程：開始畫面 → 逐題作答 → 結果頁（顯示答錯題目）→ 重新作答
- 首次作答永久記錄為基準（studyLog quiz.first）；重考另存 retakes[]
- 試題頁週曆選日期可切換不同日期試題
- 「句子判斷」「句子排列」tab 標示為即將推出（灰色不可點）

---

## v0.6.3 — 2026-06-21

**修正：長按觸發原生文字選取模式**
- `#article-text` 容器加 `-webkit-user-select: none`（根源：父層未設定，iOS 從父層進入選取模式）
- `bindLongPress` 改 `passive: false`，移動 >8px 視為捲動（取消長按計時），靜止 400ms 才觸發
- `article-text` 加 `contextmenu` 事件封鎖（防 Android 長按選單）

---

## v0.6.2 — 2026-06-21

**移除逐句跟讀 toggle**
- 選取點永遠可見，介面更直覺，不需模式切換
- 清除 `.sentence-toggle-row` CSS 及對應 HTML

---

## v0.6.1 — 2026-06-21

**修正：文章頁 UI 細節**
- 逐句跟讀與中文備注標籤對齊：移除 `sentence-toggle-row` 的 `padding: 0 2px`，改為與 `cn-toggle-row` 一致
- 逐句跟讀列上方加 `margin-top: 5px`，與週曆列保持間距
- 刪除「（新手模式）」文字

---

## v0.6.0 — 2026-06-21

**新功能：今日足跡 Dashboard**
- 首頁新增「今日足跡」區塊（任務環上方），三格磁磚顯示當日正向學習數據：
  - **新學單字**：今天加入單字本的詞數
  - **複習單字**：今天 quiz 回答記得的詞數（每次完成 quiz 累加）
  - **完成句子**：依文章進度 × 總句數估算
- 數字 > 0 顯示橘色；= 0 顯示淡灰（不報錯誤，只記正向）
- 新增 `renderDashboard()` 函式，隨 `renderHomeRing()` 一起更新
- studyLog 新增 `wordsReviewed`（quiz 完成時累加）、`sentencesTotal`（文章進度更新時存入）

---

## v0.5.7 — 2026-06-21

**修正：朗讀句子選取完全失效**
- Bug 根因：`resetArticleProgress()` 呼叫 `initSentenceSel()` 沒帶 count → `sentenceCount = undefined` → `buildPlayText()` 判斷 `!sentenceCount` 永遠 true → 無視選取 fallback 到全文
- Fix 1：`resetArticleProgress` 改為 `initSentenceSel(sentenceCount)`，保留 count 只重置選取狀態；切換文章同時呼叫 `stopReadAloud()`
- Fix 2：新增 `SENTENCE_TEXTS[]`（由 `buildSentenceTextsFromTokens(tokens)` 從 token 建立），`buildPlayText` 改用此陣列而非 DOM 查詢，不再有 DOM 為空時意外播全文的問題

---

## v0.5.6 — 2026-06-21

**修正：週曆進度弧顏色實際未生效**
- Bug：`fillStroke = '#D85A30'` 已定義但 template literal 寫死 `stroke:var(--wa)`，變數從未被使用
- Fix：改為 `style="stroke:${fillStroke}"`，進度弧現在正確顯示 `#D85A30`

---

## v0.5.5 — 2026-06-21

**修正：週曆顏色邏輯**
- 進度弧維持 `#D85A30`（與首頁文章環一致）✓
- 選中日 / 今日文字改回 `var(--wa)`（`#C4783A`），避免與進度弧同色難以區分

---

## v0.5.4 — 2026-06-21

**新功能：單字卡發音 + 例句遮擋**
- 複習考卡片：字詞旁新增 TTS 發音按鈕（點擊播音，不觸發翻牌）
- 複習考卡片：顯示例句，與中文一起遮擋（點擊同時揭露）
- 單字本顯示卡：例句也加入遮擋，與中文同步 toggle
- 新增 `findExampleSentence(word)`：加入單字本時自動從當前文章抓取來源句
- 四篇 N5 文章 vocab 全數補入 `example` 例句欄位（共 54 個詞條）

---

## v0.5.3 — 2026-06-21

**修正：週曆UI三項視覺優化**
- 週曆 ring 進度弧改為 `#D85A30`，與首頁文章環顏色一致
- 選中日期改為淺琥珀底（`var(--wa-l)`）+ 橘色文字，不再全橘填色（避免與進度弧重疊難辨）
- `.awb-day-num` 改為 38×38、`.awb-days` 改 `align-items: center`，有圈/無圈日切換不再跳動

---

## v0.5.2 — 2026-06-21

**修正：**
- 新增 content/2026-06-21/n5.json「朝ごはん」（取代舊 N4 hardcoded 公園文章）
- CURRENT_LEVEL 改為 n5（dev dashboard 及 loadTodayContent 統一使用 N5）
- 文章頁初次進入自動載入當日 n5.json；selectArticleDate 今天也走 JSON（fallback demo）
- ARTICLES_WITH_CONTENT 加入 2026-06-21

---

## v0.5.1 — 2026-06-21

**修正：**
- Toast 提示框改為深色半透明背景（暗色模式不再呈現刺眼白色）
- 首頁任務環 track 改用 CSS variable（深色模式下底色自動變暗）
- 文章週曆 SVG circle 改用 `style=` 套用 CSS variable（Safari 相容）

---

## v0.5.0 — 2026-06-21

**新功能：文章週曆導航**
- 文章頁 top-bar 下方新增週曆列（Mon–Sun），可左右翻頁切換上一週
- 有文章的日期顯示 SVG ring 圓圈（橘色，填充比例 = 當天文章完成度）
- 無內容 / 未來日期不顯示圓圈
- 點擊圓圈異步載入該日 content pack（n5.json），切換文章並重置進度
- 下週按鈕自動禁用（不可跳至未來）
- 新增三篇 N5 文章（content/2026-06-18、2026-06-19、2026-06-20）：
  - 2026-06-18「家族」：家族四人介紹
  - 2026-06-19「食堂」：學校食堂午餐
  - 2026-06-20「雨の日」：雨天帶傘上學

---

## v0.4.2 — 2026-06-21

**修正：**
- 複習考：含漢字的單字，漢字本身也一起遮擋（顯示假名，點擊同時揭露漢字＋中文）
- 修正今日環「單字卡複習」百分比不同步：switchPage 切回首頁時重新渲染 ring；exitVocabQuiz 也觸發更新

---

## v0.4.1 — 2026-06-21

**修正：**
- 「開始複習」按鈕移至過濾列（生/普/熟）同一排右側對齊

---

## v0.4.0 — 2026-06-21

**新功能：單字複習考**
- 單字頁頂欄加「開始複習」按鈕，進入全螢幕 quiz overlay
- 每張牌：顯示日文 → 點擊顯示中文 → 選「記得 / 不記得」
- 記得 → familiarity +2，直接下一張；不記得 → 公布答案，按鈕改為「下一張」
- 結果頁顯示記得/不記得張數，手動關閉
- 複習進度（0–100%）即時同步到今日任務環「單字卡複習」段
- 設定頁「學習強度」新增「單字複習排序」：急迫優先 / 隨機 / 最近加入
- 今日環圖例：單字卡複習顯示百分比（同文章段）
- 日曆日期詳情：局部完成顯示 %，深色 badge 標示

---

版本號規則：
- **末位數**（x.x.N）：微調、小修正、視覺細節
- **中位數**（x.N.0）：小功能完成、模組上線
- **首位數**（N.0.0）：穩定版本里程碑，由開發者手動宣告

## v0.3.11 — 2026-06-21

**修正：**
- 跟讀工具列改為單行排版（文字與按鈕同排，與朗讀欄一致）

---

## v0.3.10 — 2026-06-21

**修正：**
- 單字卡中文遮擋改為可重複切換（點一下顯示，再點一下遮回），方便反覆練習

---

## v0.3.9 — 2026-06-21

**修正：**
- 單字卡點擊顯示中文後，blur 殘影問題：改用 `color:transparent + text-shadow` 取代 `filter:blur`，點擊後文字清晰顯現無殘影

---

## v0.3.8 — 2026-06-21

**UI 修正：**
- 工具列（朗讀/跟讀）頂部改為向上漸消，移除分界線
- 夜晚模式補漏：av-bar、難度量表、quiz 按鈕、單字卡過濾列、dict 結果等全部覆寫深色
- 中文備注對齊微調（margin-left 20px）
- 跟讀槽位改版：移除「槽位N尚無錄音」文字；無錄音槽位顯示刪除線，有錄音顯示正常

---

## v0.3.7 — 2026-06-21

**夜晚模式：**
- 設定頁新增「夜晚模式」toggle（設定 → 顯示）
- 完整深色色盤（暖黑底色，保持暖色系調性）
- 卡片、nav bar、word panel、confirm dialog 等均覆寫深色背景
- 偏好儲存於 localStorage；無設定時自動跟隨 prefers-color-scheme

---

## v0.3.6 — 2026-06-21

**文章頁修正：**
- 修正 TTS 重複念漢字（strip furigana `<rt>` 再餵語音引擎）
- 中文備注對齊句子文字起點（margin-left 16px）
- 朗讀/跟讀工具列固定在畫面底部，不隨文章捲動消失
- 難度評分可隨時修改（移除每日鎖定）
- 引入設計 token：--r-card / --r-btn / --r-pill

---

## v0.3.5 — 2026-06-21

**文章頁：句子選取播放**
- 每句句頭加橘色小點，可點擊選取/取消（橘色實心 = 選取，灰色空心 = 不選）
- 文章上方全選列：顯示「全部」或「N / 總數」，點擊一鍵全選/全消
- 朗讀按鈕只播有選的句子
- 進度條件2/3（playedOnce / playCount）僅在全部句子都選取時計入

---

## v0.3.4 — 2026-06-21

**單字頁 UI 修正：**
- 修正左滑刪除按鈕初始即可見問題（content z-index 蓋住 del button）
- Display card 去除外框背景，改為透明（無框列表風格）
- 單字列表上下加漸消遮罩效果
- 「點擊顯示中文」提示只在首次顯示，之後自動隱藏
- 加入單字卡時正確帶入 kana 讀音，列表行顯示假名（無則顯示 romaji）

---

## v0.3.3 — 2026-06-21

**文章頁 + 單字卡：**
- 中文備注開關移至逐句跟讀下方（緊鄰文章）
- 文章下方加入難度量表（★×5），評分後儲存於 studyLog，不允許重複評分
- 單字卡 display card 漢字加 ruby furigana（kana 顯示於漢字正上方）
- 純假名單字維持原樣（kana 顯示於下方）

---

## v0.3.2 — 2026-06-21

**修正 + 單字本功能：**
- 修正文章進度捲到底條件誤觸（改用 scroll event，避免 IntersectionObserver 在短文章立即觸發）
- 單字本列表改為緊湊行列樣式（去除個別外框）
- 單字卡中文遮擋，點擊顯示（切換下一張自動重置）
- 刪除單字前加確認 dialog（單字本列表 + 文章頁移除按鈕）
- 設定頁新增「匯出單字本 CSV」功能（含 UTF-8 BOM，可直接用 Excel 開啟）

---

## v0.3.1 — 2026-06-21

**修正：**
- 單字卡加入/移除按鈕在 iOS Safari 消失（word-panel 移至 .app 頂層，避免被 .page overflow 裁切）

---

## v0.3.0 — 2026-06-21

**新功能：文章閱讀進度追蹤（條件1-3）**
- 捲到底：+20%（IntersectionObserver 偵測最後一個句子）
- 朗讀播完一次：+25%（TTS onend）
- 朗讀播完3次以上：+20%
- 首頁環形圖文章段顯示漸進弧線（非 on/off）
- 圖例顯示百分比文字（如「45%」）
- 條件4（逐句跟讀錄音）預留35%，待後續實作

---

## v0.2.2 — 2026-06-21

**修正：**
- 離開文章頁再返回，單字卡面板不再殘留（switchPage 統一呼叫 closeWordPanel）
- 跟讀列「槽位N尚無錄音」文字改為兩行排版（標籤+狀態在上，按鈕列在下），不再擠出框外

---

## v0.1.1 — 2026-06-20

**修正：**
- 修正 content 路徑錯誤（`./content` → `../content`），GitHub Pages 上文章現在可正常載入

---

## v0.1.0 — 2026-06-20

**整合：**
- 合併單字卡動態渲染、Content Pack 載入系統（來自其他對話的開發成果）
- 設定頁底部加入版本號顯示

---

## v0.0.1 — 2026-06-19

初始版本建立。

**已完成功能：**
- 五頁導覽：今日 / 文章 / 單字卡 / 試題 / 設定
- 文章頁：手動斷詞資料（ARTICLE_TOKENS）、Furigana、可開關中文備注
- 長按互動：單字面板（發音、加入/移除）、助詞語法說明
- 加入單字卡後橘色高亮 + 逐詞中文備注變色
- 朗讀控制：播放/暫停/停止、六段速度調整（0.5x–1.5x）
- 跟讀錄音：三槽位 IndexedDB 持久化、動態 MIME 偵測（Safari/Chrome 相容）
- 首頁五色任務環（SVG）+ 月曆學習紀錄（點擊展開當日詳情）
- 試題頁五個 tab：單字複習、聽力、填空、句子判斷、句子排列（靜態 mockup）
- 單字卡頁（靜態 mockup）
- SRS localStorage 資料結構（熟悉度 0–20，設計完成，尚未接邏輯）

**已知限制（待後續版本解決）：**
- 所有文章資料寫死在程式碼中，無法依日期切換
- 單字卡頁、試題頁尚未接真實資料
- SRS 複習演算法設計完成但未實作

---
