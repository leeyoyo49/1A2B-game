import random
anslot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(anslot)
del anslot[4:10]
onetofour = [0,1,2,3]
dictans=dict(zip(onetofour,anslot))
print(dictans)

a=0
b=0
gus=input("insert")
gusdict=dict(zip(onetofour,[int(x) for x in gus]))
print(gusdict)
if a<4:
    n=0
    while n<4:
        if gusdict[n] in dictans.values():
            if gusdict[n]==dictans[n]:
                a+=1
            else:
                b+=1
            n+=1
    print(a,"A",b,"B")