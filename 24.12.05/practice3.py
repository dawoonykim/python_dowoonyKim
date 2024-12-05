def times(l):
    l2 = [i*2 for i in l]
    return l2


v2 = times([1, 2, 3, 4, 5])
print(v2)


def sum_mul(a, b):
    sum = a+b
    mul = a*b
    return sum, mul

s, m = sum_mul(2, 3)
print(s,m)