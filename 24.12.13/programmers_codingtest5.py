# 프로그래머스 - 등수 매기기

def solution(score):

    avg = [sum(i)/2 for i in score]
    s_avg = sorted(avg, reverse=True)
    answer = []
    print(avg)
    print(s_avg)
    for i in avg:
        answer.append(s_avg.index(i)+1)
    return answer


print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
print(solution([[80, 70], [70, 80], [30, 50], [
      90, 100], [100, 90], [100, 100], [10, 30]]))
