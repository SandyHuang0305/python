# 費波那契數列fibonacci
#方法1
print('方法1')
terms = int(input('請問你需要幾項:')) #詢問用戶數據
n1 = 0 #第一項
n2 = 1 #第二項
count = 2

if terms <= 0: #確認輸入的值是否正確
    print('請輸入一個正數:')
elif terms == 1:
    print('裴波那契數列:', n1)
else:
    print('裴波那契數列:')
    print(n1, ',', n2,end=',')
    while count < terms:
        nth = n1 + n2
        print(nth, end=',')
        n1 = n2 #更新值
        n2 = nth
        count += 1

#方法2--遞歸法        
print('\n')
print('方法2')
def fun(n):
    if n <= 1:
        return n
    else:
        return fun(n-1) + fun(n-2)
for i in range(10):
    print(fun(i))            

#方法3
print('\n')
print('方法3')
a = 0
b = 1
while b < 1000:
    print(b)
    a, b = b, a+b   

#方法4--以list方式
print('\n')
print('方法4')
lis = []
for i in range(20):
    if i ==0 or i == 1: #第一二項都是1
        lis.append(1)
    else:
        lis.append(lis[i-2]+lis[i-1]) #從第三項開始每個值為前兩個的和
print(lis)            
