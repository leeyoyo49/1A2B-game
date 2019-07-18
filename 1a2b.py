import random
ans=[]
while len(ans)!=4:
    x=random.randint(1,9)
    if int(x) not in ans:
        ans.append(x)
print(ans)

a=0
b=0
while a<4:
    gus=input("incert:")
    alist=[int(x) for x in gus]
    a=0
    b=0
    if alist[0] in ans:
        if w1 == alist[0]:
            a+=1
        else:
            b+=1
    if alist[1] in ans:
        if w2 == alist[1]:
            a+=1
        else:
          b+=1    
    if alist[2] in ans:
        if w3 == alist[2]:
            a+=1
        else:
            b+=1
    if alist[3] in ans:
        if w4 == alist[3]:
            a+=1
        else:
            b+=1
    print(a,"A",b,"B")
    
    
print("4A0B")