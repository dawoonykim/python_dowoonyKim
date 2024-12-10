import datetime

now = datetime.datetime.today()

print(now)
print(now.year, now.month, now.day)
print(f"{now.hour} : {now.minute} : {now.second}")


today = datetime.date.today()

print(today)
print(today.year, today.month, today.day)
# today.hour가 안됨