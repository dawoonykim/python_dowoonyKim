# 프로그래머스 - 전국 대회 선발 고사

def solution(rank, attendance):
    answer = 0
    dic = dict(zip(rank, attendance))
    li = []
    index = []
    i = 1
    while len(li) < 3:
        if dic[i] == True:
            li.append(i)
        i += 1

    for i in li:
        index.append(rank.index(i))
    print(index)
    return 10000*index[0]+100*index[1]+index[2]


print(solution([3, 7, 2, 5, 4, 6, 1], [
      False, True, True, True, True, False, False]))
print(solution([1, 2, 3],	[True, True, True]))
print(solution([6, 1, 5, 2, 3, 4], [True, False, True, False, False, True]))
