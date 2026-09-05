from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))
p = 0
pdif=defaultdict(list)
dif = 0
for i in range(n):
    p += a[i]
    dif += 1 if a[i]&1 else -1
    pdif[dif].append(p)
if k > p:
    k=p
while pdif[0] and pdif[0][-1]>k:
    pdif[0].pop
ans =pdif[0][-1]
ssum = 0 
sdif = 0  
for i in range(n-1, 0, -1):
    ssum += a[i] 
    sdif += 1 if a[i]&1 == 0 else -1 
    if abs(sdif) > 2000: continue  
    cand = pdif[sdif]  
    if not cand: continue 
    while cand and ssum + cand[-1] > k: cand.pop() 
    if cand: ans = max(ans, ssum + cand[-1]) 
print(ans)  