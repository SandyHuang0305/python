#中文詞頻統計
import jieba
txt = open("文件名稱", 'r', encoding='utf-8').read() #讀檔
words = jieba.lcut(txt) #切割文檔的文字
counts = {} #設置字典
for word in words: #遍例文檔中所有文字並計數
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items()) #建立列表
items.sort(key=lambda x:x[1], reverse=True)
for i in range(15): #抓前15位
    word, count = items[i]
    print('{0:<10}{1:>5}'.format(word, count))