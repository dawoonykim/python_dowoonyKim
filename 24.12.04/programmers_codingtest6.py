# 프로그래머스 배열 만들기 5
def solution(intStrs, k, s, l):
    # answer = []
    # for i in intStrs:
    #     if int(i[s:s+list]) > k:
    #         answer.append(int(i[s:s+l])
    # return answer

    answer = []
    for i in intStrs:
        num = int(i[s:s+l])
        # num 변수를 사용함으로써 재사용하기 때문에 안정성이 높아짐
        if num > k:
            answer.append(num)
    return answer


print(solution(["0123456789", "9876543210", "9999999999999"], 50000, 5, 5))
