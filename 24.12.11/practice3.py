import time

# start = time.time()

# for i in range(10):
#     print(i)
#     time.sleep(1)

# end = time.time()

# print(f"수행 시간 : {end-start}")


def check_time(func):
    start = time.time()
    func()
    end = time.time()
    print(f"수행 시간 : {end-start}")



def a():
    for i in range(10):
        print(i)
        time.sleep(1)


def b():
    for i in range(20):
        print(i)
        time.sleep(1)


check_time(a)
check_time(b)