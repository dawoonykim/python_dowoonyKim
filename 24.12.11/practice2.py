import time

# print(time.time())
# time.sleep(2)
# print(time.time())

# print(time.time())

# a = time.time()
# time.sleep(2)
# b = time.time()

# print(b-a)

# print(time.localtime())
# time_str = time.localtime()

# print(time_str.tm_year)

# print(time.ctime())
# print(time.ctime(a))
# print(time.ctime(b))

year_round = round(time.time()/(365*24*60*60))
year = time.time()/(365*24*60*60)
print(year_round)
print(year)

day_round = round(time.time()/(365*60*60))
day = time.time()/(365*60*60)
print(day_round)
print(day)
