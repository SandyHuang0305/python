#文本進度條v3
import time
sacle = 50
print('執行開始'.center(sacle//2, '-')) # center 將字符串居中，//整除
start  = time.perf_counter() #使用程序計時
for i in range(sacle+1):
    a = '*' * i
    b = '-' * (sacle-i)
    c = (i/sacle) * 100
    dur =time.perf_counter() - start #紀錄印出文本紀錄條的時間
    print('\r{:^3.0f}%[{}-->{}]{:.2f}s'.format(c,a,b,dur), end='') #\r 回車
    time.sleep(0.1)
print('\n' + '執行結束'.center(sacle//2, '-'))
