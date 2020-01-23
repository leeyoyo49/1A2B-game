#for x in range(1,10):
#    for y in range(1,10):
#        print(x,"X",y,"=",x*y,"  ",end="")
#    print("\n")

#for i in range(1,10):
#    for j in range(1,10):
#        print("{}x{}={} ".format(i,j,i*j),end="")
#    print("                                                                                                                  ")

f=0
s=1
while f<10:
    f+=1
    s=f
    while s<10:
        print('{}x{}={} '.format(f,s,f*s),end="")
        s+=1
    print("")
    
