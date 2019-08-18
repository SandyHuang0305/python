#英文詞頻統計

def getText():
    txt = open("Twilight.txt","r",encoding='utf-8').read()#打開文件
    txt = txt.lower() #英文字全轉換為小寫
    for ch in '!"#$%&()*+,-.:；<=>?@[\\]^_{|}.~`”':#刪除特殊符號
        txt = txt.replace(ch, " ")
    return txt
Twilightxt = getText()
words = Twilightxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print('{0:<10}{1:>5}'.format(word, count))