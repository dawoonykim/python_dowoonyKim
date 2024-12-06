# 프로그래머스 - 홀수 vs 짝수

def solution(num_list):

    count = 1
    odd = 0
    even = 0
    for i in num_list:
        if count % 2 == 1:
            odd += i
        else:
            even += i
        count += 1

    if odd > even:
        return odd
    else:
        return even


print(solution([4, 2, 6, 1, 7, 6]))
print(solution([-1, 2, 5, 6, 3]))
