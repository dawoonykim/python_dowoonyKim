# 세개를 입력 받는데 mul 이면 두 수를 곱하고 add 면 두 수를 더해라
# ex)  a.py mul 2 3
# 6
# a.py add 4 5
# 9
# 입력이 2개 이하거나 4개이상이면 오류처리
import sys

cal_type = sys.argv[1]

if len(sys.argv[1:]) <= 2 or len(sys.argv[1:]) >= 4:
    print("잘못 입력하셨습니다.")
else:
    if cal_type == "add":
        print(int(sys.argv[2])+int(sys.argv[3]))
    elif cal_type == "mul":
        print(int(sys.argv[2])*int(sys.argv[3]))
