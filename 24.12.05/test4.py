# 주문 상품 가격이 20,000원 미만이면 배송비(2,500원) 포함이고,
# 아니면 배송비를 포함하지 않는 프로그램을 작성하세요.

def compaere_cost(price, count):
    cost = 0
    if price*count < 20000:
        cost = price*count+2500
    else:
        cost = price*count
    return cost


price, count = map(int, input("가격과 수량을 입력하세요. : ").split())

print(f"상품   결제 : {compaere_cost(price, count)}원")
print(f"상품 1 결제 : {compaere_cost(15000, 2)}원")
print(f"상품 2 결제 : {compaere_cost(5000, 3)}원")
