# 사용자가 입력한 모든 숫자를 더하는 프로그램을 만들어라(argv 이용)
import sys
args=sys.argv[1:]
sum = 0
for i in args:
    sum += int(i)

print(sum)
