class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f"{self.name}：{self.price}元")

class Drink(Food):
    def __init__(self, name, price):
        super().__init__(name, price)

    def category(self):
        return "飲料"


class Snack(Food):
    def __init__(self, name, price):
        super().__init__(name, price)

    def category(self):
        return "點心"

menu = {
    "可樂": Drink("可樂", 35),
    "雪碧": Drink("雪碧", 35),
    "摩卡冰沙": Drink("摩卡冰沙", 45),
    "爆米花": Snack("爆米花", 100),
    "熱狗堡": Snack("熱狗堡", 75),
    "吉拿棒": Snack("吉拿棒", 65),
    "起司nacho": Snack("起司nacho", 85),
    "雞米花": Snack("雞米花", 55),
    "薯條": Snack("薯條", 49),
    "MM": Snack("MM", 55)
}

cart = []
total = 0

print("===== 菜單 =====")
for item in menu.values():
    item.show_info()

while True:
    a = input("輸入您想要的餐點(按 Enter 結束)：")

    if a == "":
        break

    if a not in menu:
        print("沒有此商品")
    else:
        cart.append(menu[a])
        total += menu[a].price
        print(f"已加入：{menu[a].name} ")

print("===== 購物車 =====")
for item in cart:
    print(f"{item.name} - {item.price}元")

print(f"總金額：{total}元")

pay = input("刷卡 or 付現：")

if pay == "刷卡":
    print(" 刷 卡 成 功！")
elif pay == "付現":
    money = int(input("請輸入金額："))
    if money >= total:
        print(f"找您 {money - total} 元")
    else:
        print(f"金額不足，還差 {total - money} 元")
else:
    print("付款方式錯誤")