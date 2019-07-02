import time
scale = 10 #文本進度條的寬度
print('執行開始'.center(20,'-'))
#print('============執行開始==========')
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale) * 100
    print('{:^3.0f}%[{}-->{}]'.format(c,a,b))#居中+小數點0位
    time.sleep(0.1)
#print('------------執行結束-------------')
print('執行結束'.center(20,'-'))