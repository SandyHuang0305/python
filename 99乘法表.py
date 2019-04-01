# 九九乘法表
#方法1
print('方法1')
for i in range(1, 10 ):
    for j in range(1, i+1):
        if i == j: #i = j 的部分要處理
            print(j, '*', i, '=', i*j, end='\n')
        else:
            print('%d*%d=%2d' % (j,i,i*j),end='\t')    

#方法2
print('方法2')
for i in range(1,10):
    for j in range(1, i+1):
        print('%d*%d=%2d' % (j,i,i*j), end='\t')
    print()    

 #長方形輸出九九乘法表
print('長方形輸出')
for i in range(1,10):
    for j in range(1,10):
        print('%d*%d=%2d' % (i,j,j*i),end=' ')
    print('')

#左上角三角形
print('左上角三角形式')
for i in range(1,10):
    for j in range(i,10): #差別處
        print('%d*%d=%2d' % (i,j,i*j), end=' ')
    print('')  #表示換行
    
#右上三角形
print('右上三角形式')
for i in range(1,10):
    for k in range(1,i): #差別處
        print(end='      ')#空6格 
    for j in range(i,10):
        print('%d*%d=%2d' % (i,j,i*j), end='')
    print('')

#左下三角形
print('左下三角形式')
for i in range(1,10):
    for j in range(1,i+1): #差別處
        print('%d*%d=%2d' % (i,j,i*j),end='')
    print('')                                 
