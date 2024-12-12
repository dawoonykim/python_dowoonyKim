# 프로그래머스 - 영어가 싫어요

def solution(numbers):
    answer = ""
    temp = ""
    dic = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
           "six": "6", "seven": "7", "eight": "8", "nine": "9", "zero": "0"}
    for i in numbers:
        temp += i
        # print(temp)
        if temp in dic:
            answer += dic[temp]
            temp = ""

    return int(answer)


print(solution("onetwothreefourfivesixseveneightnine"))
print(solution("onefourzerosixseven"))
