import calendar as cal
print(cal.month(2019, 6))

#是否為閏年
from calendar import month, isleap
print(isleap(2012))

#沒有from 的用法
print(cal.isleap(2015))

#datetime 模組使用
from datetime import date
print(date.today())

today = date.today()
print(today.strftime('%Y%m%d'))
print(today.strftime('%Y/%m/%d'))


print(today.strftime('%Y{y}%m{m}%d{d}'). format(y= '年', m = '月', d = '日'))

print(today.strftime('%Y %B %d %a'))

#現在時間
from datetime import datetime as dt
print(dt.now())

now = dt.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))

#timedelta
from datetime import date, timedelta
today = date.today()
print(today)

one_week = timedelta(days = 7)
print(today + one_week)
print(today - one_week)