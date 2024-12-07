# 프로그래머스 - 문자열이 몇 번 등장하는지 세기

def solution(myString, pat):
    count = 0  # 얼마나 반복하는지 확인하는 변수
    start = 0  # 시작 위치를 옮기기 위해 사용하는 변수
    while True:
        start = myString.find(pat, start)  # 0부터 pat를 찾기 위해 사용하는 변수
        print(start)
        if start == -1:  # pat가 없다면 -1을 반환
            break
        count += 1  # pat 횟수 1 증가
        start += 1  # start 값을 1 증가
    return count


print(solution("banana", "ana"))
print(solution("aaaa", "aa"))
