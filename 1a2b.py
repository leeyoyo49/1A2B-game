import random
(w1)=int(random.uniform(1,10))
(w2)=int(random.uniform(1,10))
(w3)=int(random.uniform(1,10))
(w4)=int(random.uniform(1,10))

ans=[w1,w2,w3,w4]
print(ans)
g1=g2=g3=g4=0


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