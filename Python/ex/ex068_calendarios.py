import calendar
import locale

locale.setlocale(locale.LC_ALL, '')
# print(locale)
# print(calendar.calendar(2023))
#
print(calendar.monthrange(2023, 12))
print(list(calendar.day_name))
# print(locale.getlocale())
