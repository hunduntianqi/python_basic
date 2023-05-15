"""
    calendar模块: 日历模块
"""
import calendar

# calendar.monthrange(年, 月) 获取指定年份的指定月份的第一天时周几, 以及当月的天数
print(calendar.monthrange(2022, 3)[0] + 1, calendar.monthrange(2022, 1)[1])
