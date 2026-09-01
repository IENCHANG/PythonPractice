score=[]
for i in range(4):
    a = list(map(int, input().split()))
    score.append(sum(a))
win1, win2=0, 0
if score[0]>score[1]:
    win1+=1
else:
    win2+=1
if score[2]>score[3]:
    win1+=1
else:
    win2+=1
print("{:d}:{:d}".format(score[0], score[1]))
print("{:d}:{:d}".format(score[2], score[3]))
if win1>win2:
    print("Win")
elif win1<win2:
    print("Lose")
else:
    print("Tie")