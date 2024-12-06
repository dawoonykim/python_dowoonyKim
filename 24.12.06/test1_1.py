def fibo(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibo(n-2)+fibo(n-1)
    return memo[n]


# print(fibo(300))
memo = {}
print(fibo(300))
