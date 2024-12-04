# 프로그래머스 접미사 배열

def solution(my_string):
    answer = []
    # 반복문 실행 글자 수 만큼 반복
    for i in range(len(my_string)):
        # 문자열 뒤에서부터 시작해서 리스트에 값을 하나씩 추가
        answer.append(my_string[-i:])
    # 리스트 정렬
    answer.sort()
    return answer


print(solution("banana"))
print(solution("programmers"))
