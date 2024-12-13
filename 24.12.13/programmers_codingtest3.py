# 프로그래머스 - 치킨 쿠폰

def solution(chicken):

    service = chicken//10
    rest_chicken = chicken % 10 # => 쿠폰 1장
    service_first_chicken = service//10

    rest_coupon_coupon = service % 10
    service_second_chicken = service_first_chicken//10

    last_service_chicken=(rest_chicken+rest_coupon_coupon+service_second_chicken)//10
    print(f"service : {service}")
    print(f"rest_chicken : {rest_chicken}")
    print(f"service_first_chicken : {service_first_chicken}")
    print(f"rest coupon coupon : {rest_coupon_coupon}")
    print(f"service_second_chicken : {service_second_chicken}")

    print(service+rest_chicken+service_first_chicken+service_second_chicken+last_service_chicken)

    


print(solution(100))
print(solution(1081))
