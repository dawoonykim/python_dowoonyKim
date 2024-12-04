# # 셋 만들기
# numbers1 = {1, 2, 3, 4, 5}
# numbers2 = set([1, 2, 3, 4, 5, 5])  # {1, 2, 3, 4, 5}
# print(numbers2)
# apple = set("apple")

# # 값 in 셋
# print(1 in numbers1)

# # 값 not in 셋
# print("c" in apple)

# # 요소 추가
# numbers1.add(6)
# print(numbers1)

# # 요소 삭제
# numbers1.remove(1)
# print(numbers1)

# # 임의의 요소 삭제
# print(numbers1.pop())  # 랜덤이라서 값이 FIFO으로 동작
# print(numbers1)

# # 모든 요소 삭제
# numbers1.clear()
# print(numbers1)

# # 셋은 중복을 허용하지 않으며, 순서 정렬을 하지 않는 특수한 리스트
# set3 = set("apple")
# print(set3)

# while len(set3) > 0:
#     a = set3.pop()
#     print(a, end=" ")

# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}

# # 교집합
# print(s1 & s2)
# print(s1.intersection(s2))

# # 합집합
# print(s1 | s2)
# print(s1.union(s2))

# # 차집합
# print(s1-s2)
# print(s2-s1)
# print(s1.difference(s2))

name = ["흥부", "콩쥐", "놀부", "콩쥐"]

dupl_name = set()
print(dupl_name)

n = len(name)
print(n)
for i in range(0, n-1):
    for j in range(i+1, n):
        if name[i] == name[j]:
            dupl_name.add(name[i])

print(f"중복 이름 : {dupl_name}")
a = []

set_name = ["1", "2", "3", "2"]
for i in range(len(set_name)):
    if set_name.count(set_name[i]) > 1:
        # set_name.remove(set_name[i]) # 중간에 돌다가 삭제하게 되면 에러가 발생
        a.append(set_name[i])  # 값을 어디 저장을 해놓고서 나중에 삭제를 해야된다

name_set = set(set_name)
print(name_set)
name_list = list(name_set)
name_list.sort()
print(name_list)
