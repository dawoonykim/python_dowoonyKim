# 프로그래머스 - 그림 확대

def solution(picture, k):
    answer = []

    for i in range(len(picture)):
        for _ in range(k):
            answer.append(picture[i].replace(".", "."*k).replace("x", "x"*k))

    return answer


print(solution([".xx...xx.",
                "x..x.x..x",
                "x...x...x",
                ".x.....x.",
                "..x...x..",
                "...x.x...",
                "....x...."], 2))
print(solution(["x.x",
                ".x.",
                "x.x"], 3))
