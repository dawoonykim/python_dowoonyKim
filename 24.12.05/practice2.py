def sun_n(n):
    sum_v = 0

    for i in range(1, n+1):
        sum_v += i

    return sum_v


def sun_n2(n):

    sum_v = (n*(n+1)//2)

    return sum_v


print(sun_n(10))
print(sun_n2(10))
