import random

n=int(input())
k=0
while range(n):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if x**2+y**2<=1:
        k+=1
print(k/n)