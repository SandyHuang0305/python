#圓周率蒙特卡羅公式
from random import random
from time import perf_counter
DARTS = 1000*1000 #撒點的數量
hits = 0.0 #在圓內中點的數量
start = perf_counter()
for i in range(1, DARTS+1):
    x, y = random(), random()
    dist = pow(x**2 + y**2, 0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print('圓周率值是:{}'.format(pi))
print('運行時間是:{:.5f}s'.format(perf_counter()-start))
