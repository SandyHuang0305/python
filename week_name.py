#如何獲取星期字符串
#方式一
weekStr = '星期一星期二星期三星期四星期五星期六星期日'
weekId = eval(input('請輸入星期數字(1-7):'))
pos = (weekId - 1) * 3
print(weekStr[pos: pos + 3])


#方式二
weekStr = '一二三四五六日'
weekId = eval(input('請輸入星期數字(1-7):'))
print('星期' + weekStr[weekId - 1])