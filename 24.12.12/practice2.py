# 영타자 연습 프로그램
with open("word.txt", "w") as f:
    word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
            'grape', 'garlic', 'onion', 'potato']

    for i in word:
        f.write(i+" ")  # \n, \t, \r

import random

with open("word.txt", "r") as f:
    data = f.read().split()  # \n => data=f.readlines()
    word = random.choice(data)
    print(word)
