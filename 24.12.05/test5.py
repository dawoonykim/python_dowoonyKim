# https://www.acmicpc.net/problem/10828

# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 다섯 가지이다.

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

def push(num):
    int_list.append(num)

def top():
    if int_list:
        print(int_list[-1])
    else:
        print(-1)


def size():
    print(len(int_list))


def empty():
    if not int_list:
        print(1)
    else:
        print(0)


def pop():
    if int_list:
        print(int_list.pop())
    else:
        print(-1)


count = int(input("동작할 횟수 : "))
int_list = []

for i in range(count):
    active_input = input("").strip().split()
    active = active_input[0]
    if len(active_input) > 1 and active_input[1].isdigit:
        if active == "push":
            num = active_input[1]
            push(num)
    else:
        if active == "top":
            top()
        elif active == "size":
            size()
        elif active == "empty":
            empty()
        elif active == "pop":
            pop()
