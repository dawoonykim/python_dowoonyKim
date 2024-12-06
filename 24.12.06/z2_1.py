def fibo(n):
    if n in temp:
        return temp[n]
    if n <= 2:
        return 1
    else:
        temp[n] = fibo(n-1)+fibo(n-2)
        return temp[n]


temp = {}
# print(type(temp))
print(fibo(100))
