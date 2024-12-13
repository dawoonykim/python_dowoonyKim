# while True:
#     try:
#         num = int(input("숫자 입력 : "))
#         print(f"정수 입력 성공 : {num}")
#         break
#     except ValueError:
#         print("정수가 아님! 정수를 입력하세요.")
#         continue # continue가 있어도 finally 부분 동작
#     finally:
#         print("무조건무조건")

while True:
    try:
        num = int(input("숫자 입력 : "))
        print(f"정수 입력 성공 : {num}")
        break
    except ValueError:
        print("정수가 아님! 정수를 입력하세요.")
    finally:
        print("무조건무조건")
