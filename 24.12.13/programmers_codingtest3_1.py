# 프로그래머스 - 치킨 쿠폰

def solution(chicken):

    f_service = chicken//10
    rest_chicken = chicken % 10  # => 쿠폰 1장
    s_service = f_service//10
    rest_coupon = f_service % 10
    t_service = s_service//10
    l_service = (rest_coupon+rest_chicken+t_service)//10
    print(f"first_service : {f_service}")
    print(f"rest_chicken : {rest_chicken}")
    print(f"second_service : {s_service}")
    print(f"rest_coupon_of_first_service : {rest_coupon}")
    print(f"third_service : {t_service}")
    print(f"fourth_service : {l_service}")

    print(f_service+rest_chicken+s_service+l_service)


print(solution(100))
print(solution(1081))
