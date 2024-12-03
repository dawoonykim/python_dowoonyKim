list = list(map(int, input("숫자 여러 개 입력 : ").split()))
# print(list)

max_value = max(list)
min_value = min(list)
list.remove(max_value)
list.remove(min_value)

count = len(list)
sum = sum(i for i in list)

print(f"가장 큰 값 : {max_value}\n가장 작은 값 : {min_value}\n나머지 값의 평균 : {sum/count}")
