import random

com = random.randint(1, 100)
print(f"com : {com}")
min_v, max_v, count = 1, 100, 1

while True:
    try:
        guess = int(input(f"숫자 입력 {min_v} ~ {max_v} : "))
        if guess < 0 or guess > 100:
            print("입력 범위를 초과했어요.")
        elif com == guess:
            print("정답입니다.")
            score = 100-(count-1)*10
            if score < 0:
                score = 0
            print(f"도전 횟수 : {count} /  점수 : {score}점")
            break
        elif com > guess and min_v < guess:
            print("랜덤 수보다 작아요.")
            # print("랜덤 수가 커요.")
            count += 1
            min_v = guess
        elif com < guess and max_v > guess:
            print("랜덤 수보다 커요.")
            # print("랜덤 수가 작아요")
            count += 1
            max_v = guess
    except ValueError:
        print("숫자만 입력 가능합니다.")
