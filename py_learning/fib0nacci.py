# def fibonacci(n):
#     cache = {0: 0, 1: 1}
#     print(cache)
#     if n in cache:
#         return cache[n]
#     else:
#         cache[n] = fibonacci(n-1) + fibonacci(n-2)
#         return cache[n]

# print(fibonacci(10))

def fibonacci(n):
    a=0
    b=1
    for _ in range(n):
        a,b = b,a+b
    return a

print(fibonacci(10))