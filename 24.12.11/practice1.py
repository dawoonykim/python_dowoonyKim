import datetime
import calendar

# calendar.prcal(2024)

# calendar.prmonth(2024,6)

print(calendar.weekday(2024, 8, 12))


days = ["월", "화", "수", "목", "금", "토", "일"]

weekday = datetime.date.today().weekday()
# print(weekday)
print(f"오늘은 {days[weekday]}요일")

the_day = datetime.date(2024, 12, 25).weekday()
print(f"크리스마스는 {days[weekday]}요일")


def getWeekday(yyyy, mm, dd):
    days = ["월", "화", "수", "목", "금", "토", "일"]
    the_day = datetime.date(yyyy, mm, dd).weekday()
    print(f"{yyyy}년 {mm}월 {dd}일은 {days[weekday]}요일")


getWeekday(2024, 12, 11)
