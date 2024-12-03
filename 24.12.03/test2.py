num = int(input("정수 n을 입력하세요. "))

sum_v_all = 0 # 모든 정수의 합 구하기
sum_v_odd = 0 # 정수 중 홀수의 합 구하기
for i in range(num+1):
    if i % 2 != 0:
        sum_v_odd += i # 홀수일때만 정수 더하기
    sum_v_all += i # 모든 정수 더하기

print(f"입력한 수까지의 합은 {sum_v_all}입니다.")
print(f"입력한 수까지  홀수의 합은 {sum_v_odd}입니다.")
