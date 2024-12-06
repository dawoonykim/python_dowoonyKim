# def pr_str(txt, count=1):
#     # 매개변수는 앞에거는 생략하면 안된다
#     # 그 이유는 앞에거를 생략했을 경우,
#     # 호출 부분에서 입력되는 매개변수가
#     # 어느 변수를 부르는지 알 수 없기 때문
#     for i in range(count):
#         print(txt)


# pr_str("1. Hello", 3)
# pr_str("2. Hello")
# pr_str()

def pr_str(txt, count=1, count2=1):
    for i in range(count):
        print(txt)
        print(count2)


pr_str("1. Hello", 3)
pr_str("2. Hello")
# pr_str()
