#質數的判斷
n = int(input('請輸入一個數字:'))
for i in range(2, n ):
    if n % i == 0 :
        print(n, '不是質數')
        break # 不是質數就跳出循環
else: 
    print(n, '是質數') 
    
#輸出指定範圍內的質數

#選定範圍
lower = int(input('請輸入最小值:'))
upper = int(input('請輸入最大值:'))

#求質數
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)  
