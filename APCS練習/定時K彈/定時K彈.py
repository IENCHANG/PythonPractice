# N, M, K=map(int, input().split())
# a=[i+1 for i in range(N)]
# print(a)
# del a[M-1]
# print(a)
# while True:
#     for h in range(M):
#         print(M-h)
#     del a[M-h]
#     if len(a)<=2:
#         break
N, M, K = map(int, input().split())
a = [i + 1 for i in range(N)]
idx = 0
last_eliminated = None
while len(a) > 1:
    idx = (idx + M - 1) % len(a)
    last_eliminated = a.pop(idx)
winner = a[0]
print(winner)