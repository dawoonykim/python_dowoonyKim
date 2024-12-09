# 프로그래머스 - 배열의 길이에 따라 다른 연산하기

def solution(arr, n):
    answer = arr
    length = len(answer)
    for i in range(length):
        if length % 2 == 0:  # 짝수일 때 => 홀수 인덱스에 n 더하기
            if i%2==1:
                answer[i] = answer[i]+n
        elif length % 2 == 1:  # 홀수일 때 => 짝수 인덱스에 n 더하기
            if i%2==0:
                answer[i] = answer[i]+n
    return answer


print(solution([49, 12, 100, 276, 33], 27))
print(solution([444, 555, 666, 777], 100))
