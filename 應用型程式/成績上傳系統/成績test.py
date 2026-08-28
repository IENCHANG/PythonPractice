class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print(f"{self.name}:")
        print(f"年級：{self.grade}")


class Student1(Student):
    def __init__(self, name, grade, Etest, Ctest, Mtest, Htest, 地test, 公test):
        super().__init__(name, grade)
        self.Etest = Etest
        self.Ctest = Ctest
        self.Mtest = Mtest
        self.Htest = Htest
        self.地test = 地test
        self.公test = 公test

class Student2(Student):
    def __init__(self, name, grade, Etest, Ctest, Mtest, Htest, 地test, 公test):
        super().__init__(name, grade)
        self.Etest = Etest
        self.Ctest = Ctest
        self.Mtest = Mtest
        self.Htest = Htest
        self.地test = 地test
        self.公test = 公test

class Student3(Student):
    def __init__(self, name, grade, Etest, Ctest, Mtest, Htest, 地test, 公test):
        super().__init__(name, grade)
        self.Etest = Etest
        self.Ctest = Ctest
        self.Mtest = Mtest
        self.Htest = Htest
        self.地test = 地test
        self.公test = 公test

s1 = Student1("周挽", 9, 96, 98, 90, 96, 94, 85)
s2 = Student2("陸西驍", 9, 95, 60, 58, 85, 77, 99)
s3 = Student3("姜彥", 9, 100, 100, 95, 65, 99, 98)
while True:
 print("您是什麼科的老師？")
 teacher = input()
 if teacher == "社會":
     print("ok,收到")
 elif teacher == "導師":
     print("呃，請重新輸入")
 else:
     break
 while True:
    print("現在成績在導師手上，請問您要向導師索取嗎？")
    get = input()

    if get == "no":
        print("已離開!!")
        break

    elif get == "yes":
        print("------成績登記表------")
        s1.introduce()
        print(f"English test：{s1.Etest}")
        print(f"Chinese test：{s1.Ctest}")
        print(f"Math test：{s1.Mtest}")
        print(f"History test：{s1.Htest}")
        print(f"地理 test：{s1. 地test}")
        print(f"公民 test：{s1.公test}")
        print()
        s2.introduce()
        print(f"English test：{s2.Etest}")
        print(f"Chinese test：{s2.Ctest}")
        print(f"Math test：{s2.Mtest}")
        print(f"History test：{s2.Htest}")
        print(f"地理 test：{s2. 地test}")
        print(f"公民 test：{s2.公test}")
        print()
        s3.introduce()
        print(f"English test：{s3.Etest}")
        print(f"Chinese test：{s3.Ctest}")
        print(f"Math test：{s3.Mtest}")
        print(f"History test：{s3.Htest}")
        print(f"地理 test：{s3. 地test}")
        print(f"公民 test：{s3.公test}")
        print()
        break

    else:
        print("請重新輸入!!")
 class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print(f"{self.name}:")
        print(f"年級：{self.grade}")
 break
#數學老師成績登記錯誤+5
print()
print()
print("Line 一則訊息 5s前")
print()
print("老師，不好意思，數學老師登記錯誤了，還請老師幫忙改正一下")
while True:
    print("要不要幫忙改一下?")
    q = input()
    if q == "好":

        print("------成績登記表------")
        s1.introduce()
        print(f"English test：{s1.Etest}")
        print(f"Chinese test：{s1.Ctest}")
        print(f"Math test：{s1.Mtest}+5")
        print(f"History test：{s1.Htest}")
        print(f"地理 test：{s1. 地test}")
        print(f"公民 test：{s1.公test}")
        print()
        s2.introduce()
        print(f"English test：{s2.Etest}")
        print(f"Chinese test：{s2.Ctest}")
        print(f"Math test：{s2.Mtest}+5")
        print(f"History test：{s2.Htest}")
        print(f"地理 test：{s2. 地test}")
        print(f"公民 test：{s2.公test}")
        print()
        s3.introduce()
        print(f"English test：{s3.Etest}")
        print(f"Chinese test：{s3.Ctest}")
        print(f"Math test：{s3.Mtest}+5")
        print(f"History test：{s3.Htest}")
        print(f"地理 test：{s3. 地test}")
        print(f"公民 test：{s3.公test}")
        print()
        print("非常感謝!!")
        break
    elif q == "不要"or"no":
        print("你這個沒良心的畜生!!")
        break
    else:
        print("請重新輸入!!!")