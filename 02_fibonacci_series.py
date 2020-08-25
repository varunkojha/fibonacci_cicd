# Since the code slows down due to multiple recursion. We will do MEMOIZATION: cached value into dict
cached_dict = {}
def fibonacci(n):
    # Check if nth term is in cache or not 
    if n in cached_dict:
        return cached_dict[n]
    
    # Else we compute nth term
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n > 2:
        a = fibonacci(n-1) + fibonacci(n-2)
        # we are now storing it in cached dictionary then return it
        cached_dict[n] = a
        return a

for n in range(1, 1000):
    print(n, ":", fibonacci(n))
