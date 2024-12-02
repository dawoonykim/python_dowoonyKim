age = int(input("나이를 숫자로 입력해주세요 : "))
purchase = input("결제 방법을 입력해주세요. ('카드' 또는 '현금'만 입력) : ")

if not (purchase == "카드" or purchase == "현금"):
    print("카드 또는 현금만 입력하세요.")
else:
    if age >= 75:
        price = "무료"
    elif age >= 20:
        if purchase == "카드":
            price = "1200원"
        elif purchase == "현금":
            price = "1300원"
    elif age >= 14:
        if purchase == "카드":
            price = "720원"
        elif purchase == "현금":
            price = "1000원"
    elif age >= 8:
        price = "450원"
    else:
        price = "무료"

print(f"{age}세의 {purchase} 요금은 {price} 입니다.")
