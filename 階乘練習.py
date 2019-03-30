# 階乘練習

#讓用戶輸入數字
num = int(input('請輸入一個數字:'))
factorial = 1

#確認該數是正負數
if num < 0:
    print('負數沒有階乘的喔')
elif num == 0:
    print('0的階乘為1')
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(num, '的階乘為', factorial)

#利用math庫
import math
num = int(input('請輸入一個數字:'))
if num < 0:
    print('負數沒有階乘的喔')  
else:
    print(num, '的階乘為',math.factorial(num) )                  
