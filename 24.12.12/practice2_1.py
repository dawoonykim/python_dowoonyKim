import time
import random

with open("word.txt", "r") as f:
    word = f.read().split()

try:
    n = 1
    input("[타자 게임] 준비되면 엔터!")

    start = time.time()

    while n < 11:
        print("문제", n)
        question = random.choice(word)
        print(question)
        user = input()

        if question == user:
            print("통과!!")
            n += 1
        else:
            print("오타!! 다시 도전")
    end = time.time()
    print(f"게임 소요 시간 : {end-start:.2f}초")

except:
    print("파일을 찾을 수 없습니다.")


# 파일이 있는지 없는지 조사하는 프로그램
# import os
# if os.path.exists("word.txt"):
#     with open("word.txt","r")as f:
#         word = f.read().split()
# else:
#     n = 1
#     input("[타자 게임] 준비되면 엔터!")

#     start = time.time()

#     while n < 11:
#         print("문제", n)
#         question = random.choice(word)
#         print(question)
#         user = input()

#         if question == user:
#             print("통과!!")
#             n += 1
#         else:
#             print("오타!! 다시 도전")
#     end = time.time()
#     print(f"게임 소요 시간 : {end-start:.2f}초")