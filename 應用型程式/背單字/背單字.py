import random

# 單字庫（英文:中文）
words = {
    "conclusion": "結束",
    "conclude": "做結論",
    "collection": "蒐集物",
    "collect": "蒐集",
    "collective": "共同",
    "collector": "收藏家",
    "inform": "通知",
    "informative": "有內容的",
    "information": "消息",
    "elect": "選舉",
    "select": "挑選",
    "election": "選舉(比較長的)",
    "eletive": "選舉的",
    "option": "選修科目",
    "signal": "號誌",
    "sign": "表示",
    "signature": "簽訂",
    "gesture": "手勢",
    "civil": "國內的",
    "civilize": "教化",
    "civilized": "文明的",
    "civilization": "文明",
    "civilian": "平民的",
    "scary": "可怕的",
    "scare": "嚇",
    "afraid": "害怕的",
    "edit": "編輯",
    "editor": "編者",
    "edition": "版本",
    "editorial": "社論",
    "editor-in-chief": "總編輯",
    "governor": "州長",
    "govern": "統治",
    "government": "政府",
    "expressive": "表示",
    "express": "表達",
    "expression": "表達(ion)",
    "apple": "蘋果",
    "banana": "香蕉",
    "coffee": "咖啡",
    "duck": "鴨子"
}

score = 0

print("=== 英文單字測驗 ===")
print("共 40 題，每題 2.5 分")

questions = random.sample(list(words.items()), 10)

for i, (english, chinese) in enumerate(questions, start=1):
    print(f"第 {i} 題")
    answer = input(f"{chinese} 的英文是：")

    if answer.lower() == english.lower():
        print("答對了！")
        score += 10
    else:
        print(f"答錯了！正確答案是 {english}")

print("=== 測驗結束 ===")
print(f"你的總分：{score} 分")

if score == 100:
    print("滿 分 ！ 太 厲 害 了 ！")
elif score >=80:
    print("差 一 點 就 滿 分 了 ! ! !")
elif score >= 60:
    print("不 錯 喔 ， 繼 續 加 油 ！ ! !")
else:
    print("You failed ，要 多 背 幾 次 單 字 喔 ！ ! !")