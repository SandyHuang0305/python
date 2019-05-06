from PIL import Image #使用PIL套件中的Image功能
import os

#一次轉換多張圖片
for file in os.listdir('.'): #在這個文件夾之下
    if file.endswith('.jpg'): #不要印出python檔的處理方式
        img = Image.open(file).convert('L')
        img.save(file[:-4] + '_grey.png')#存檔
