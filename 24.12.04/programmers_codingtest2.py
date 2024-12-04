# 프로그래머스 간단한 논리 연산
def solution(x1, x2, x3, x4):
    answer = True
    if (x1 or x2) and (x3 or x4):
        return True;
    else:
      return False


print(solution(False, True, True, True))
print(solution(True, False, False, False))
