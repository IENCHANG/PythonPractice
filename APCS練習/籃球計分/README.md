# 兩回合比賽計分系統 (Match Score Calculator)

這是一個 Python 程式，用於計算兩組對決（共四隊/四局）的總分，並依據勝場數判斷最終的比賽結果（獲勝、落敗或平手）。

---

## 程式碼內容

```python
score = []

# 輸入 4 次資料，計算每次輸入數字的總和並存入列表
for i in range(4):
    a = list(map(int, input().split()))
    score.append(sum(a))

win1, win2 = 0, 0

# 第一場對決：比較第 1 隊 (score[0]) 與第 2 隊 (score[1])
if score[0] > score[1]:
    win1 += 1
else:
    win2 += 1

# 第二場對決：比較第 3 隊 (score[2]) 與第 4 隊 (score[3])
if score[2] > score[3]:
    win1 += 1
else:
    win2 += 1

# 輸出兩場對決的比分
print("{:d}:{:d}".format(score[0], score[1]))
print("{:d}:{:d}".format(score[2], score[3]))

# 根據累積勝場數判斷最終結果
if win1 > win2:
    print("Win")
elif win1 < win2:
    print("Lose")
else:
    print("Tie")
```

---

## 邏輯與運作說明

1. **分數計算**：程式會進行 4 次輸入，每次輸入可包含多個整數（以空格分隔），程式會自動計算該次輸入的所有數字總和。
2. **兩對決判定**：
   - 第一回合：比較 `score[0]` 與 `score[1]`。
   - 第二回合：比較 `score[2]` 與 `score[3]`。
3. **勝負統計**：
   - 若 `win1` 勝場較多，輸出 `Win`。
   - 若 `win2` 勝場較多，輸出 `Lose`。
   - 若兩隊勝場數相同，輸出 `Tie`。

---

## 輸入與輸出範例

### 範例輸入
```text
10 20
15 5
30 10
20 20
```

### 範例輸出
```text
30:20
40:40
Tie
```

---

## 使用方法

1. 確保已安裝 [Python 3](https://www.python.org/)。
2. 將程式碼儲存為 `match_score.py`。
3. 開啟終端機或命令提示字元並執行：
   ```bash
   python match_score.py
   ```
4. 依序輸入 4 行數字，每行數字間以空格隔開，輸入完成後即可查看比分與結果。
