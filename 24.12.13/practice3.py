# try:
#     num = int(input("정수입력 : "))
#     print(num)
# except ValueError:
#     print("정수가 아님")

# try:
#     num = float(input("실수입력 : "))
#     print(num)
# except ValueError:
#     print("실수가 아님")

# try:
#     num = int(input("정수입력 : "))
#     print(num)
# except ValueError as msg:
#     print(msg)


# try:
#     num = int(input("정수입력 : "))
#     print(num)
# except:
#     print("정수가 아님")

try:
    num = int(input("정수입력 : "))
    print(num)
except ValueError as msg:
    print(msg)
except Exception as msg:
    print(msg)
else:
    print("예외 없음")
