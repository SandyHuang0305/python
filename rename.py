#批次重命名
import os #用OS庫

path='C:\\Users\\user\\Desktop\\01' #要修改的檔案     
f=os.listdir(path)
print(f)

n = 0
for i in f:
    os.chdir(path)
    old_name = path + f[n]
    #new_name = path +'picture' + str(n+1) +'.jpg'
    os.rename( f[n],'圖片' + str(n+1) +'.jpg') #想更改成的名字
    n = n+1
