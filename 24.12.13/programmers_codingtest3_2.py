# 프로그래머스 - 치킨 쿠폰

def solution(chicken):
    total = 0
    coupon = chicken
    while coupon >= 10:
        new_chicken = coupon//10
        # print(f"new_chicken : {new_chicken}")
        total += new_chicken
        # print(f"total : {total}")
        coupon = coupon % 10+new_chicken
        # print(f"coupon : {coupon}")
    return total


print(solution(100))
print(solution(1081))
