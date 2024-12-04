# bread = 30 # 빵 30개
# people = 4 # 사람 4명

# result = bread // people
# rest = bread % people

# print(f"빵의 개수 : {result}\n남은 빵의 개수 : {rest}")

# score = [10, 20, 30, 40]
# print("배열의 크기 : ", len(score))

# score[1] = 50
# print(score)

# del score[2]
# print(score)


# season = ["봄", "여름", "가을", "겨울"]
# print(season[0])
# print(season[-1])
# print(season)
# print(type(season))
# print(season[0:3])
# print(season[:3])
# print(season[2:4])
# print(season[2:])

# for i in season:
#     print(i)

# number = [1, 5, 3, 4, 8, 2, 3]
# print(number[3])
# print(number[::-1])


# shop = ["반팔", "청바지", "이어폰", "키보드"]

# # 인덱싱
# print(shop[0])  # Output : "반팔"

# # 슬라이싱
# print(shop[0:2])  # Output : ["반팔", "청바지"]

# # 리스트 안에 리스트에서 인덱싱
# my_shop = ["반팔", "청바지", "이어폰", ["무선 키보드", "유선 키보드", "기계식 키보드"]]
# print(my_shop[3])  # Output : ["무선 키보드", "유선 키보드", "기계식 키보드"]
# print(my_shop[-1]) # Output : ["무선 키보드", "유선 키보드", "기계식 키보드"]
# print(my_shop[2:4]) # Output : ["이어폰", ["무선 키보드", "유선 키보드", "기계식 키보드"]]


# shop = ["반팔", "청바지", "이어폰", "키보드"]

# shop[0] = "무지 반팔"
# print(shop) # Output : ["무지 반팔", "청바지", "이어폰", "키보드"]

# shop[100] = "신발"
# print(shop) # Output : IndexError

# shop = ["반팔", "청바지", "이어폰", "키보드"]

# # 리스트 삭제
# # del shop[2] # 이어폰 삭제
# del shop[2:4]  # 이어폰, 키보드 삭제
# print(shop) # Output : ["반팔", "청바지"]

# a = [1, 2, 3]
# b = [4, 5]

# print(a+b) # Output : [1, 2, 3, 4, 5]
# print(a*2) # Output : [1, 2, 3, 1, 2, 3]
# print(len(a)) # Output : 3
# print(len(b)) # Output : 2

# num = [3, 1, 5, 2]
# num.sort()
# print(num)  # Output : [1, 2, 3, 5]

# alphabet = ["b", "c", "a", "d"]
# alphabet.sort()
# print(alphabet)  # Output : ["a", "b", "c", "d"]

# korean = ["강", "이", "박", "최"]
# korean.sort()
# print(korean)  # Output : ["강", "박", "이", "최"]

# alphabet = ["b", "c", "a", "d"]
# alphabet.reverse()
# print(alphabet)  # Output : ["d", "a", "c", "b"]

# korean = ["강", "이", "박", "최"]
# korean.reverse()
# print(korean)  # Output : ["최", "박", "이", "강"]

# shop = ["a", "b", "c", "d"]
# shop.append("e")
# print(shop) # Output : ["a", "b", "c", "d", "e"]

# shop = ["a", "b", "c", "d"]
# shop.append("e")
# shop.remove("b")
# print(shop) # Output : ["a", "c", "d", "e"]


# shop = ["a", "c", "d", "e"]
# shop.insert(1, "b")
# print(shop)  # Output : ["a", "b", "c", "d", "e"]

# shop = ["반팔", "청바지", "이어폰", "키보드"]
# shop.pop(1)
# print(shop)  # Output : ["반팔", "이어폰", "키보드"]
# shop.pop()
# print(shop)  # Output : ["반팔", "이어폰"]

# shop = ["a", "b", "c", "d", "e"]

# del shop[1]
# print(shop)  # Output : ["a", "c", "d", "e"]


# shop = ["a", "b", "c", "d", "e"]

# del shop[1:3]
# print(shop)  # Output : ["a", "d", "e"]

# shop = ["a", "b", "c", "d", "e"]

# print(shop.index("c"))  # Output : 2
# print(shop.index("없는값"))  # Output : Value Error

# a = ["a", "b", "c", "b"]
# print(a.count("b")) # Output : 2

d = ["강남", "강북", "서", "asdf", "서", "서"]
first_item = d.index("서")+1
print(first_item+d[first_item:].index("서"))
