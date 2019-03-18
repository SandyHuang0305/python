#記帳程式
products = [] #建立大清單
with open('products.csv', 'r',ecoding='utf-8') as f: #讀取檔案#寫入與讀取檔案的編碼需相同
    for line in f: #line為變數
    	s = line.strip().split(',')#1.去掉換行符號2.切割,括號內輸入遇到甚麼時要切割
    	print(s)

while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
    	break
    price = input('請輸入商品價格:')	
    p = [] #建立小清單
    p = [name, price]
    products.append(p)#把p裝進products
print(products)

products[1][1]#大清單的第一個中的第一格    	

for product in products: #for loop 教學
	print(product[0], '的價格為', product[1])
with open ('products.csv', 'w', ecoding='utf-8')	as f: #依序為1.檔名2.寫入模式3.寫入當作f 4.處理字體亂碼問題
    f.write('商品,價格\n')
    for p in products:
    	f.write(p[0] +  ',' +  p[1] + '\n') #真正的寫入檔案
    	                                    #csv檔以逗點做區格