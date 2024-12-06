list = [2, 4, 1, 4, 6]
list.sort()
print("list", list)

list2 = [2, 4, 1, 4, 6]
print("sorted(list2)", sorted(list2))
print("list2", list2)

# 오름 차순으로 정렬했을 때 3 번째로 작은 인덱스를 구하라
list3 = [1, 6, 8, 5, 7]
# 정렬하고 그 값을 원본에서 찾으면 됨
list_copy = list3
list_copy.sort()
num = list_copy[2]
print(num)
print(list3.index(6))

print(eval("1+2*2"))
# 문자열의 계산이 가능
num = eval("1+2*2")
print(type(num))
print()

# 반올림하는 간단한 방법(함수 사용 X)

num1 = 4.6
print("int(num1)\t: ", int(num1))
print("int(num1+0.5)\t: ", int(num1+0.5))
print("round(num1)\t: ", round(num1))
print("round(4.5)\t: ", round(4.5))
print("int(4.4+0.5)\t: ", int(4.4+0.5))
# print(num1)

print()
print(round(2.547))
print(round(2.547, 1))
print(round(2.547, 2))
print(round(127, -1))
print(round(127, -2))
print(round(127))

print()
print(2**3)
print(pow(2, 3))
