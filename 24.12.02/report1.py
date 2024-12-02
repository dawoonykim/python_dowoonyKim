num = int(input("정수 n을 입력하세요. : "))

num_list = []
for i in range(num):
    num_list.append(i+1)

print("만들어진 리스트 출력 ", num_list)

print("홀수 : ", num_list[0::2])
print("짝수 : ", num_list[1::2])
