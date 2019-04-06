import os #operating system作業系統

products = [] #建立大清單
#檢查檔案存在與否
if os.path.isfile('products.csv'):#如果，路徑中有這個檔案
    print('找到檔案')
    #讀取檔案
    with open('products.csv', 'r', encoding='utf-8') as f:#讀取檔案#寫入與讀取檔案的編碼需相同
        for line in f: #line為變數
            if '商品,價格' in line: #跳過商品價格字串
                continue #不會跳出迴圈,只是前往下一迴，只能寫在迴圈裡
            name, price = line.strip().split(',')#1.去掉換行符號2.切割,括號內遇到甚麼時就切割
            products.append([name, price]) #建立小清單更簡易的方法
    print(products)
else:
    print('找不到檔案')    
   
#讓使用者輸入    	
while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
    	break
    price = input('請輸入商品價格:')	
    price = int(price)
    products.append([name, price])#把p裝進products
print(products)

#印出購買紀錄    	
for p in products: #for loop 教學
	print(p[0], '的價格為', p[1])

#寫入檔案
with open ('products.csv', 'w', encoding='utf-8')	as f: #依序為1.檔名2.寫入模式3.寫入當作f 4.處理字體亂碼問題
    f.write('商品,價格\n')
    for p in products:
    	f.write(p[0] +  ',' +  str(p[1]) + '\n') #真正的寫入檔案
    	                                    #csv檔以逗點做區格
