# https://www.acmicpc.net/problem/10828

# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 다섯 가지이다.

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
import sys


def push(num):
    int_list.append(num)


def top():
    if len(int_list) == 0:
        print(-1)
    else:
        print(int_list[-1])


def size():
    print(len(int_list))


def empty():
    if len(int_list) == 0:
        print(1)
    else:
        print(0)


def pop():
    if len(int_list) == 0:
        print(-1)
    else:
        print(int_list.pop())


count = int(sys.stdin.readline())
int_list = []

for i in range(count):
    active_input = sys.stdin.readline().split()

    match active_input[0]:

        case "push":
            push(active_input[1])
        case "top":
            top()
        case "size":
            size()
        case "empty":
            empty()
        case "pop":
            pop()

    # if active_input[0] == "push":
    #     push(active_input[1])

    # elif active_input[0] == "top":
    #     top()
    # elif active_input[0] == "size":
    #     size()
    # elif active_input[0] == "empty":
    #     empty()
    # elif active_input[0] == "pop":
    #     pop()
