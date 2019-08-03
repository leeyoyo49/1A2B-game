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
num = input("insert your number:")
print("the",num,"number of Fibonacci_sequence is ",Fibonacci_sequence(int(num)))
et = time.time()
print('it took',et-st,'second for the algorythm to solve out')
