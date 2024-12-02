num1 = 472
num2 = "385"

first = num1*int(num2[2])
second = num1*int(num2[1])
third = num1*int(num2[0])

result_list = [first, second, third]
for i in result_list:
    print(i)
    
result = first+second*10+third*100

print(result)

# 문자열도 리스트처럼 사용할 수 있음을 기억하자
