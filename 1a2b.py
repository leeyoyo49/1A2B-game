import random
ans = []
while len(ans) != 4:
    x = random.randint(0, 9)
    if int(x) not in ans:
        ans.append(x)
print(ans)
alot = []
blot = []

def gusmod(*onetofour):
    for gusnm in onetofour:
      if guslist[gusnm] in ans:
            if ans[gusnm] == guslist[gusnm]:
                alot.append(gusnm)
            else:
                blot.append(gusnm)
while len(alot) < 4:
    gus = input("insert:")
    guslist = [int(x) for x in gus]
    print(guslist)
    alot = []
    blot = []
    gusmod(0,1,2,3)
    print(len(alot), "A", len(blot), "B")
