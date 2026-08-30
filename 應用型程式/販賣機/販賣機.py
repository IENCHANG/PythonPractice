menu = {
    "可樂": 35,
    "雪碧": 35,
    "摩卡冰沙": 45,
    "爆米花": 100,
    "熱狗堡": 75,
    "吉拿棒": 65,
    "起司 nacho": 85,
    "雞米花": 55,
    "薯條": 49,
    "MM": 55,
    
}
cart = []
total=0

print("菜單")
print("--------")
for item, price in menu.items():
    print(f"{item}:{price}元")


while True:
    a = input("輸入您想要的餐點:")
    if a ==" ":
        break
    elif menu.get(a) is None:
        print("沒有此商品")
    else:
        cart.append(a)
        total += menu.get(a)
        print(a, end=" ")

print(f"共{total}元!!刷卡or付現!!")