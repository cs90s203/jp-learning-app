# 日語學習 App — 版本記錄

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
