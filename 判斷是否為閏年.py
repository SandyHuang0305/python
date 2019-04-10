#判斷是否為閏年
year = int(input('請輸入一個年份:'))
if (year % 4) == 0:
    if (year % 100) ==0:
        if (year % 400) ==0:
            print(year, '是閏年')
        else:
            print(year, '不是閏年')
    else:
        print(year, '不是閏年')
else:
    print(year, '不是閏年')

#進階版
#用calendar庫
import calendar
year = int(input('請輸入年份:'))
y = calendar.isleap(year)
if y == True:
	print(y, '為閏年')
else:
    print(y, '不是閏年')	
