import random
ans = []
while len(ans) != 4:
    x = random.randint(0, 9)
    if int(x) not in ans:
        ans.append(x)
print(ans)
p=0
def yee(y):
    if alist[y] in ans:
        if ans[y] == alist[y]:
            return 1
        else:
            return 2
alot=0
blot=0
while alot < 4:
    gus = input("insert:")
    alist = [int(x) for x in gus]
    alot = 0
    blot = 0
    y = 0
    while y<4:
        if yee(y) == 1:
            alot+=1
        elif yee(y) == 2:
            blot+=1     
        else:
            p=1
        y+=1
    print(alot, "A", blot, "B")


