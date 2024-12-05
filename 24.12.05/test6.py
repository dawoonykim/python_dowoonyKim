def get_times(n):
    # global count # 전역 변수를 제거하게 되면
    count = 0 # 지역 변수의 값은 증가하겠지만, 함수가 종료되면 지역 변수의 값이 소멸이 되기 때문에 값이 전달이 안됨
    for i in range(1, 31):
        if i % n == 0:
            print(i, end=" ")
            count += 1
    # return count


count = 0
n = 3
get_times(n)
print(f'\n{n}의 배수의 개수: {count}')
