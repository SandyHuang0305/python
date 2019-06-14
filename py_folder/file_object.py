#讀取、寫入檔案
file_object = open('python.txt', 'r') #讀取
file_object.read()

file_object = open('python.txt', 'a')#追加寫入
file_object.write('add data from program')
file_object.close()