""" Write a function to return nth term of Fibonacci Sequence"""
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n > 2:
        a = fibonacci(n-1) + fibonacci(n-2)
        return a

for n in range(1, 501):
    print(n, ":", fibonacci(n))
