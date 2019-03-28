#質數的判斷
n = int(input('請輸入一個數字:'))
for i in range(2, n ):
    if n % i == 0 :
        print(n, '不是質數')
        break # 不是質數就跳出循環
else: 
    print(n, '是質數')       
