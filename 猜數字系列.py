#隨機數生成

import random #導入模組

print(random.randint(0,10))

#猜數字小遊戲
import random

r = random.randint(0,100)
count = 0
while True:
	count = count + 1
	num = int(input('請猜數字:'))
	if num == r:
		print('你猜對了喔')
		break
	elif num > r:
	    print('比答案大喔')
	elif num < r:
	    print('比答案小喔')
	print('你已經猜了', count, '次了喔')        	

