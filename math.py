import time
def Fibonacci_sequence(n):
    int(n)
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1       
    else:
        return Fibonacci_sequence(n-1) + Fibonacci_sequence(n-2)  



st = time.time()
print(Fibonacci_sequence(40))
et = time.time()
print(et-st)
