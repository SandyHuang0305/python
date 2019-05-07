from PIL import Image #使用PIL套件中的Image功能
import os

#一次轉換多張圖片
for file in os.listdir('orig'): #在這個文件夾之下 #增加路徑合併
    if file.endswith('.jpg'): #不要印出python檔的處理方式
        img = Image.open('orig/' + file).convert('L')
        img.save('result/' + file[:-4] + '_grey.png')#存檔
#路徑合併的其他方式: (os.path,join('orig', file))