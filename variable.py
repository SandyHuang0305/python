#全局變量與局部變量
APPLE = 100 #全局變量
def fun():
    a = 10 #局部變量
    return a+100
print(APPLE)
#print(a)  #會報錯，因為只有全局變量才能在def外面被調用

#若一定要在外部調用局部變量的方法
BOOK = 200 #全局變量  
b = None #定義全局變量
def money():
    global b #使用已定義好的全局變量
    b = 20 #現在的b已是全局變量
    return b+50 
print(BOOK)
print('b past:', b)
money()
print('b now:', b)    
