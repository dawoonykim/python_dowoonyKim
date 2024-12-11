# 세개를 입력 받는데 mul 이면 두 수를 곱하고 add 면 두 수를 더해라
# ex)  a.py mul 2 3
# 6
# a.py add 4 5
# 9
import sys

cal_type = sys.argv[1]

if cal_type == "add":
    print(int(sys.argv[2])+int(sys.argv[3]))
elif cal_type == "mul":
    print(int(sys.argv[2])*int(sys.argv[3]))
