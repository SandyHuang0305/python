#計算三角形面積
a = float(input('請輸入三角形第一邊長:'))
b = float(input('請輸入三角形第二邊長:'))
c = float(input('請輸入三角形第三邊長:'))

#計算半周長
s = (a + b + c) / 2

#計算面積
area = (s*(s-a)*(s-b)*(s-c))**0.5
print('三角形面積為%0.2f'%area) #浮点型保留2位小数 
