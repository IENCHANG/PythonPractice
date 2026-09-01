a, b, c=map(int, input().split())
if a>b:
    a, b=b, a
if b>c:
    b, c=c,b
if a>b:
    a, b=b,a
print(a, b, c)
if a+b<=c:
    print("NO")
elif a^2+b^2==c^2:
    print("Right")
elif a^2+b^2>c^2:
    print("Acute")
elif a^2+b^2<c^2:
    print("Obtuse")