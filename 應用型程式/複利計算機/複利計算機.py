a=0
b=0
c=0
while a<=0:
    a=int(input("輸入您的本金:"))

while c<=0:

    c=int(input("輸入您要存多久:"))
    if c<=0:
        print("你怎麼這麼窮，連利息都拿不到。哈哈哈~")
while c<=0:
    c=int(input("輸入您要存多久:"))
    if c<=0:
        print("不可小於等於0")

total=int(a * (1+(b/100))** c)
#print(f"您在{c}年後可以拿到{total}元")
#print(f"你的利息有{total-a}元")
print(f"您在{c}年後可以拿到{total:,}元")
print(f"你的利息有{total-a:,}元")