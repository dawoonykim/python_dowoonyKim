# def calc_avg(*numbers):
#     print(type(numbers))
#     sum_v = 0
#     for i in numbers:
#         sum_v += i
#     average = sum_v/len(numbers)
#     return average

# avg1=calc_avg(1,2)
# print(avg1)
# avg2=calc_avg(1,2,3,4,5)
# print(avg2)

def calc_avg(numbers):
    print(type(numbers))
    sum_v = 0
    for i in numbers:
        sum_v += i
    average = sum_v/len(numbers)
    return average


avg1 = calc_avg((1, 2))
print(avg1)
avg2 = calc_avg((1, 2, 3, 4, 5))
print(avg2)
