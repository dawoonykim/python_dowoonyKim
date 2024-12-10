import datetime

print("지금까지 며칠?")
first_day = datetime.date(2024, 11, 25)
print(first_day)

today = datetime.date.today()
print(today)

passed_time = today-first_day
# print(passed_time)
print(f"개강 이후 {passed_time.days}일이 지났습니다.")
