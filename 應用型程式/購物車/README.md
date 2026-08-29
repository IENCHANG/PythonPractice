# 商品價格記錄器 (Product Price Recorder)

一個簡單的 Python 命令列工具，用於輸入多筆商品名稱與價格，並自動計算總金額與輸出詳細清單。

## 核心功能

* **動態輸入**：透過迴圈連續輸入商品名稱與對應價格。
* **結束機制**：當商品名稱輸入**空白字元（一個空格 `" "`）**時，即終端輸入並開始計算。
* **格式化輸出**：使用 `enumerate()` 印出項次，並將價格格式化為保留兩位小數的金額。
* **總價計算**：自動統計所有輸入商品的總金額。

---

## 程式碼說明 (Code Analysis)

```python
things = []
prices = []

# 步驟 1: 資料收集迴圈
while True:
    t = (input("輸入商品:"))
    if t == " ":
        break
    
    p = int(input(f"輸入{t}的價格:"))
    things.append(t)
    prices.append(p)

# 步驟 2: 清單輸出與格式化
for index, t in enumerate(things):
    print(f"第{index+1}商品是{t},價格是{prices[index]:.2f}")

# 步驟 3: 計算總金額
total = sum(prices)
print(f"總價格為{total}元!!")
```

---

## 使用說明 (Usage)

### 執行環境需求
* **Python 版本**：Python 3.6 或以上（因為使用了 f-string 語法）

### 執行步驟

1. **執行程式**：
   ```bash
   python main.py
   ```

2. **輸入商品與價格**：
   依提示輸入商品名稱及整數價格。

3. **結束輸入**：
   當提示 `輸入商品:` 時，**按下一次空白鍵再按 Enter**（輸入包含空格的字串 `" "`），即可停止輸入並印出結算結果。

---

## 執行範例 (Example)

```text
輸入商品:蘋果
輸入蘋果的價格:30
輸入商品:香蕉
輸入香蕉的價格:15
輸入商品: 
第1商品是蘋果,價格是30.00
第2商品是香蕉,價格是15.00
總價格為45元!!
```

---

## 改善建議 (Improvement Suggestions)

1. **防呆與例外處理 (Exception Handling)**：
   * 目前價格輸入使用 `int()` 轉型，若使用者輸入非數字（如英文字母或中文），會引發 `ValueError` 導致程式中斷。可加入 `try-except` 進行防呆處理。
2. **結束條件調整**：
   * 目前需輸入「一個空格 `" "`」才會結束，若使用者直接按 Enter（空字串 `""`）則無法結束。建議改為 `if not t.strip():`，這樣無論是直接按 Enter 或是輸入純空白都能順利結束。
3. **資料結構優化**：
   * 使用兩個獨立的平行列表（`things` 與 `prices`）較容易因為索引維護不當產生誤差。建議改用字典 `dict` 或元組列表 `list of tuples` 來儲存商品資訊。
