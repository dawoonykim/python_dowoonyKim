n = 5
factorial1 = 1
for i in range(1, n+1):
    factorial1 *= i
print(factorial1)


def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

print(factorial(5))
