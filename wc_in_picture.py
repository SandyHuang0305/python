#利用wordcloud讀檔
import jieba #要讀中文檔要先用jieba
import wordcloud

import imageio 
mask = imageio.imread('圖檔')
f = open('文件檔', 'r', encoding='ANSI')
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = ' '.join(ls)
w = wordcloud.WordCloud(font_path = 'msyh.ttc',\
    mask = mask,\
    width = 1000, height = 700, background_color = 'white',\
    )
w.generate(txt)
w.to_file('圖檔')