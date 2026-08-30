Markdown
# 簡易販賣機 / 點餐系統 (Vending Machine CLI)

這是一個使用 Python 撰寫的命令列介面（CLI）販賣機點餐系統。使用者可以瀏覽菜單、重複選擇餐點並進行金額累加，最後輸出總金額進行結帳。

---

## 📌 功能特色

* **菜單展示**：自動列出所有可供選擇的餐點及其價格[cite: 1]。
* **動態點餐**：採用迴圈機制，可連續輸入品項[cite: 1]。
* **錯誤處理**：若輸入不在菜單上的品項，會跳出警示並請使用者重新輸入[cite: 1]。
* **自動計算**：即時將點選的品項記錄至購物車並累加總金額[cite: 1]。

---

## 🛠️ 菜單項目 (Menu)

| 餐點名稱 | 價格 (NTD) |
| :--- | :--- |
| 可樂 | $35[cite: 1] |
| 雪碧 | $35[cite: 1] |
| 摩卡冰沙 | $45[cite: 1] |
| 爆米花 | $100[cite: 1] |
| 熱狗堡 | $75[cite: 1] |
| 吉拿棒 | $65[cite: 1] |
| 起司 nacho | $85[cite: 1] |
| 雞米花 | $55[cite: 1] |
| 薯條 | $49[cite: 1] |
| MM | $55[cite: 1] |

---

## 🚀 使用說明

1. **執行程式**：
   在終端機（Terminal）執行以下指令：
   ```bash
   python 販賣機.py
點餐流程：

程式將印出完整菜單[cite: 1]。

依提示輸入想要購買的餐點名稱（如：可樂）[cite: 1]。

若要結束點餐，請直接按下空白鍵後按下 Enter[cite: 1]。

結束後系統將印出最終應付總金額[cite: 1]。

💻 程式碼邏輯與解析
Python
# 1. 初始化資料結構：使用字典 (Dictionary) 儲存商品與價格，列表 (List) 記錄購物車
menu = { ... }[cite: 1]
cart = [][cite: 1]
total = 0[cite: 1]

# 2. 顯示菜單
for item, price in menu.items():[cite: 1]
    print(f"{item}:{price}元")[cite: 1]

# 3. 主點餐迴圈
while True:[cite: 1]
    a = input("輸入您想要的餐點:")[cite: 1]
    if a == " ":  # 輸入空白鍵跳出迴圈
        break[cite: 1]
    elif menu.get(a) is None:  # 防呆機制：品項不存在
        print("沒有此商品")[cite: 1]
    else:  # 成功點餐，加入購物車並累加金額
        cart.append(a)[cite: 1]
    	total += menu.get(a)[cite: 1]
        print(a, end=" ")[cite: 1]

# 4. 結帳輸出
print(f"共{total}元!!刷卡or付現!!")[cite: 1]
💡 未來優化方向 (Roadmap)
結束條件優化：改為按下 Enter（空字串 ""）或輸入 q 即可結束，避免使用者誤解空白鍵的作用。

購物車明細：結帳時可額外輸出 cart 內容，讓使用者確認購買品項清單。

數量統計：可支援重複輸入相同商品時，自動統計數量（例如：可樂 x2）。