def fib(n):
    if n < 0:
        print ("Invalid input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:   
        return fib(n-1) + fib(n-2)



def factorial(n):
    sum = 1
    for i in range(1, n+1):
        sum = sum * i
    return sum