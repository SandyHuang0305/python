#交換變量

#用戶輸入
x = input('輸入x值: ')
y = input('輸入y值: ')
#交換變量方式1
x,y = y,x
print('交換後x的值為:', x)
print('交換後y的值為:', y)

#交換變量方式2
a = input('輸入a值:')
b = input('輸入b值:')
temp = a
a = b
b = temp
print('交換後a的值為:', a)
print('交換後b的值為:', b)
