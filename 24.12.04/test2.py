dic = {
    "비트": "0이나 1의 값을 가지는 컴퓨터 데이터의 최소 단위",
    "변수": "어떤 1개의 자료를 저장하기 위한 메모리 할당 공간",
    "리스트": "여러 개의 연속적인 자료를 저장하는 자료구조"
}


print("★ 컴퓨터 사전 ★")
word = input("검색할 단어를 입력하세요: ")

# for i in dic.keys():
#   if word == i:
#     print(f'{word}: {dic[word]}')
#   else:
#     print("정의된 단어가 없습니다.")
#     continue

# if word=="비트":
#   print(f'{word}: {dic[word]}')
# elif word=="변수":
#   print(f'{word}: {dic[word]}')
# elif word=="리스트":
#   print(f'{word}: {dic[word]}')
# else:
#   print("정의된 단어가 없습니다.")

# 방법 1
value=dic.get(word)
if value:
  print(f'{word}: {dic[word]}')
else:
  print("정의된 단어가 없습니다.")

# 방법 2
if word in dic:
  print(f'{word}: {dic[word]}')
else:
  print("정의된 단어가 없습니다.")