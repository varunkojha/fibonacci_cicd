
def Fib(n):
    p, q = 0, 1

    while(p < n):
        yield p
        p, q = q, p + q

x = Fib(10)
#it = iter(x)
for i in range(0, 11):
    print(next(x))
    #print(next(it))

