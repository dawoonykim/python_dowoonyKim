score = int(input("점수를 입력하세요 : "))

if not (0 <= score <= 100):
    print("점수가 0~100 사이가 아닙니다.")
else:
    grade = {10: "A+", 9: "A", 8: "B", 7: "C", 6: "D"}.get(score//10, "E")
    print(grade)

if not (0 <= score <= 100):
  print("점수가 0~100 사이가 아닙니다.")
else:
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("E")

# if score >= 90:
#     if score == 100:
#         print("만점")
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("E")


# if score == 100:
#     print("만점")
# else:
#     if score >= 90:
#         print("A")
#     elif score >= 80:
#       print("B")
#     elif score >= 70:
#       print("C")
#     elif score >= 60:
#      print("D")
#     else:
#       print("E")
