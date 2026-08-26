import random

class Gopher:
    def __init__(self):
        self.show = False

    def jump(self):
        self.show = True
        print("地鼠跳起來了！")

    def drilling(self):
        self.show = False
        print("地鼠鑽下去了！")

class Person:
    def catch(self, gopher):
        if gopher.show:
            if random.randint(1, 100) <= 50:
                print("打中了！")
                return 1
            else:
                print("揮空了！")
                return 0
        return 0

score = 0

gopher = Gopher()
person = Person()

print("=== 無限打地鼠 ===")

running = True

while running:
    if random.choice([True, False]):
        gopher.jump()

        action = input("打地鼠(y) 不打按Enter / 離開(空白)：")

        if action.lower() == "y":
            score += person.catch(gopher)
        elif action.lower() == " ":
            running = False

        gopher.drilling()

    else:
        print("沒有地鼠出現！")

        action = input("繼續(Enter) / 離開(空白)：")
        if action.lower() == " ":
            running = False

print(f"遊戲結束！總分：{score}")