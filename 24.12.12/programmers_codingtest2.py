# 프로그래머스 - 영어가 싫어요

def solution(numbers):
    answer = ""
    temp = ""
    for i in numbers:
        temp += i
        if temp == "one":
            temp = ""
            answer += "1"
        elif temp == "two":
            temp = ""
            answer += "2"
        elif temp == "three":
            temp = ""
            answer += "3"
        elif temp == "four":
            temp = ""
            answer += "4"
        elif temp == "five":
            temp = ""
            answer += "5"
        elif temp == "six":
            temp = ""
            answer += "6"
        elif temp == "seven":
            temp = ""
            answer += "7"
        elif temp == "eight":
            temp = ""
            answer += "8"
        elif temp == "nine":
            temp = ""
            answer += "9"
        elif temp == "zero":
            temp = ""
            answer += "0"

    return int(answer)


print(solution("onetwothreefourfivesixseveneightnine"))
print(solution("onefourzerosixseven"))
