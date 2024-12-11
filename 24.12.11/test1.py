# 사용자가 입력한 모든 숫자를 더하는 프로그램을 만들어라(argv 이용)
import sys

sum = 0
for i in range(1,len(sys.argv[1:])+1):
    sum += int(sys.argv[i])

print(sum)
