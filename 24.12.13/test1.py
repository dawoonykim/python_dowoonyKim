# flag = True
# while flag:
#     try:
#         num = int(input("숫자 입력 : "))
#         print(f"정수 입력 성공 : {num}")
#         flag = False
#     except ValueError:
#         print("정수가 아님! 정수를 입력하세요.")


while True:
    try:
        num = int(input("숫자 입력 : "))
        print(f"정수 입력 성공 : {num}")
        break
    except ValueError:
        print("정수가 아님! 정수를 입력하세요.")
