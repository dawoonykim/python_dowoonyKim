num1 = int(input())
num2 = int(input())

baek = num2//100
sip = (num2-baek*100)//10
il = num2 % 10
# print(baek)
# print(sip)
# print(il)

first=num1*il
second=(num1)*sip
third=num1*baek

result=first+second*10+third*100
print(first)
print(second)
print(third)
print(result)
