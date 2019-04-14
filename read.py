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