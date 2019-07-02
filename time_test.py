#time庫練習
import time
t = time.gmtime()
print(time.strftime('%Y-%m-%d %H:%M:%S',t))
print('====================')
timeStr = '2019-07-01 10:47:00'
print(time.strptime(timeStr, "%Y-%m-%d %H:%M:%S"))
