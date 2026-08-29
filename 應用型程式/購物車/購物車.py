things = []
prices = []
while True:
    t = (input("輸入商品:"))
    if t == " ":
        break
    
    p = int(input(f"輸入{t}的價格:"))
    things.append(t)
    prices.append(p)
    
for index, t in enumerate(things):

    print(f"第{index+1}商品是{t},價格是{prices[index]:.2f}")
total = sum(prices)
print(f"總價格為{total}元!!")