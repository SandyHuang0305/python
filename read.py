data = []
count = 0


with open('reviews.txt', 'r') as f:#讀檔
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0: # %是用來求餘數，即count分之1000
            print(len(data))
print('檔案讀取完了,總共有',len(data), '筆資料')

#算平均長度
sum_len = 0
for d in data: #把每筆資料命名為d
    sum_len = sum_len + len(d)   
print('每筆留言的平均長度是',sum_len / len(data)) 

#計算留言中最常出現的字
wc = {} #製作計數的dict
for d in data:#拿出清單中的字
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] += 1 #if word有出現在wc字典裡，就加一
        else:
            wc[word] = 1

#統計            
for word in wc:
    if wc[word] > 100000:
        print(word, wc[word])
print(len(wc))#確認字典中有幾個key  

#讓使用者查找單字
while True:
    word = input('請問想查找甚麼字？')
    if word == 'q':
        print('感謝使用')
        break
    if word in wc:
        print(word, '出現過的次數為:', wc[word])
    else:
        print('沒出現在字典裡喔')                     


