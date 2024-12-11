import time
import random
word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
        'grape', 'garlic', 'onion', 'potato']


n = 1

input("[타자 게임] 준비되면 엔터!")
start = time.time()

while n <= 10:
    print(f"문제 {n}")
    question = random.choice(word)
    print(question)
    init = input()

    if question == init:
        print("통과!!")
        n += 1
    else:
        print("오타 다시 도전!")

end = time.time()

e_s = end-start

print(f"타자 시간 : {e_s : .2f}초")
