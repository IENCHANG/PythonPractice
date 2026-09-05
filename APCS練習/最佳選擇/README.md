# 🎯 最佳選擇 (The Ultimate Choice)

> **「人生就是一連串的選擇，但這裡的選擇不能超過 K，而且奇數偶數還要平衡！」** 🤪

歡迎來到 **最佳選擇** 解題專案！這是一個讓你同時考驗數學敏感度、演算法極限以及對 `defaultdict` 愛不釋手的 Python 解題方案。

---

## 📜 題目梗概 (Story)

你面前有一排數字（前綴和與奇偶數的修羅場）。
你的任務是從中挑選出最佳的子陣列/組合，使得：
1. **奇偶平衡**：選出來的奇數與偶數數量剛好抵消或滿足特定邊界條件（`dif == 0` 或對應的 `sdif`）。
2. **不爆預算**：總和不能超過上限 $K$ ($sum \le K$)。
3. **壓榨最大值**：在不超過 $K$ 的前提下，拿到**最大的總和**！

---

## 💡 解題亮點 (Highlights)

* ⚡ **前後夾擊 (Prefix & Suffix Combination)**：從前綴（`p` & `dif`）與後綴（`ssum` & `sdif`）雙向奔赴，尋找最完美的契合點。
* 🗂️ **哈希地圖的神力 (`defaultdict`)**：使用 `defaultdict(list)` 紀錄每一種奇偶差值下的所有前綴和，找解快如閃電！
* ✂️ **剪枝與貪婪單調性 (`pop()`)**：超過 $K$ 的答案直接 `.pop()` 砍掉，不留一絲情面。
* 🛡️ **神秘防禦剪枝 (`abs(sdif) > 2000`)**：超過 2000 的差值？`continue`！給效率留一條活路！

---

## 🛠️ 程式碼一覽 (Code)

```python
from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

p = 0
pdif = defaultdict(list)
dif = 0

# 前綴預處理
for i in range(n):
    p += a[i]
    dif += 1 if a[i] & 1 else -1
    pdif[dif].append(p)

# 如果 K 比總和還大，直接下修 K
if k > p:
    k = p

# 處理前綴恰好平衡的情況
while pdif[0] and pdif[0][-1] > k:
    pdif[0].pop()

ans = pdif[0][-1] if pdif[0] else 0

# 後綴搜尋與對應前綴匹配
ssum = 0 
sdif = 0  
for i in range(n - 1, 0, -1):
    ssum += a[i] 
    sdif += 1 if a[i] & 1 == 0 else -1 
    if abs(sdif) > 2000: 
        continue  
    cand = pdif[sdif]  
    if not cand: 
        continue 
    while cand and ssum + cand[-1] > k: 
        cand.pop() 
    if cand: 
        ans = max(ans, ssum + cand[-1]) 

print(ans)
```

---

## 🚀 如何執行 (Usage)

1. 確保你的電腦安裝了 Python 3 (不需要額外安裝外掛套件，內建 `collections` 搞定一切！)。
2. 在終端機執行：

```bash
python 最佳選擇.py
```

3. 輸入測試資料（例如）：

```text
5 10
1 2 3 4 5
```

4. 享受輸出的最佳解！ 🎉

---

## ⚠️ 小小吐槽與除錯提醒 (Troubleshooting)

* ⚠️ **`pdif[0].pop` 記得加括號！**  
  原始碼中的 `pdif[0].pop` 是函式物件，如果沒加上小括號 `()`，它是不會真正執行彈出操作的喔！建議改為 `pdif[0].pop()`。
* ⚠️ **邊界防護**：若 `pdif[0]` 為空時，直接取 `pdif[0][-1]` 可能會觸發 `IndexError`，記得加個預設值！

---

<p center="align">
  <i>Made with ❤️ and Python algorithms. Happy Coding!</i>
</p>
