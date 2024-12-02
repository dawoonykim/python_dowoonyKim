# print("오늘은 12월 %d일 입니다." % 2)
# print("오늘은 %d월 %d일 입니다." % (12, 2))
# print("오늘은 %d%s %d일 입니다." % (12, "월", 2))
# print("오늘은 %d%s %d%s 입니다." % (12, "월", 2, "일"))

# print(f"오늘은 {12}{"월"} {2}{"일"} 입니다.")
# print("오늘은 " + str(12)+"월 "+str(2)+"일 입니다.")
# print("오늘은 ", 12, "월 ", 2, "일 입니다.", sep="")

# print(len("바나나"))
# print(len("Hello, world!"))

# print("Hello".upper())
# print("Hello".lower())

# print("코딩온. 저는 코딩온입니다.".find("코딩온"))
# print("코딩온. 저는 코딩온입니다.".rfind("코딩온"))

friends = "존 루나 제리"
print(friends.split(" "))  # default가 띄어쓰기
print(friends.split())

email = "jerry@spreatics.com"
print(email.split("@"))

sentence = "{}월 {}일".format(12, 2)
print(sentence)

b = "   111   222   "
print(b.strip())
print(b.split())

print(b.replace("111", "222"))
