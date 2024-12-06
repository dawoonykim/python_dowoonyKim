# 프로그래머스 - 1로 만들기

def solution(num_list):
    answer = 0
    while len(num_list) > 0:
        temp = []
        for i in num_list:
            if i > 1:
                if i % 2 == 0:
                    temp.append(i / 2)
                else:
                    temp.append((i-1)/2)
                answer += 1
        num_list = [x for x in temp if x > 1]

    return answer


print(solution([12, 4, 15, 1, 14]))
