list_num = input("숫자 여러 개 입력 : ")

list_n = list_num.split()
for i in list_n:
    list_num.append(int(i))
print(list_num)

max_value = max(list_num)
min_value = min(list_num)
list_num.remove(max_value)
list_num.remove(min_value)


sum = 0
count = len(list_num)
for i in list_num:
    sum += i

print(f"가장 큰 값 : {max_value}\n가장 작은 값 : {min_value}\n나머지 값의 평균 : {sum/count}")
