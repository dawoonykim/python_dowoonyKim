# 프로그래머스 - 다음에 올 숫자

def solution(common):
    answer = 0
    num1 = common[1]-common[0]
    num2 = common[2]-common[1]
    print(num1, common[-1])
    if num1 == num2:
        answer = num1+common[-1]
    else:
        answer = num2//num1*common[-1] # => num1만 했을 경우 등비인지 아닌지 확인할 수 없어
    return answer


print(solution([1, 2, 3, 4]))
print(solution([2, 4, 8]))
