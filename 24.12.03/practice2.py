score = [70, 80, 50, 60, 90, 40]

sum_v = 0
count = len(score)
for i in score:
    sum_v += i

avg = sum_v/count

print(f"개수 : {count}")
print(f"합계 : {sum_v}")
print(f"평균 : {avg}")


print(f"합계 : {sum(score)}")
print(f"합계 : {sum([70, 80, 50, 60, 90, 40])}")