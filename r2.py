#如何統計對話內容

#讀取檔案
def read_file(filename):
    lines = []#創作清單
    with open (filename, 'r', encoding='utf-8-sig') as f:
        for line in f:#用for迴圈讀檔案
            lines.append(line.strip())#裝進清單#去掉換行符號
    return lines#回傳清單

#轉換
def convert(lines):
    person = None #處理當開頭不是人名的狀況
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in lines:#把lines清單的東西叫出來
        s = line.split(' ') #把空格切開
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:   
                for m in s[2:]: #計算訊息字數
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:   
                for m in s[2:]: #計算訊息字數
                    viki_word_count += len(m)  
    print('allen說了', allen_word_count, '個字')
    print('allen傳了', allen_sticker_count, '個貼圖')
    print('allen傳了', allen_image_count, '張圖片')
    print('Viki說了', viki_word_count, '個字')
    print('viki傳了', viki_sticker_count, '個貼圖')
    print('viki傳了', viki_image_count, '張圖片')
    

#寫入檔案
def write_file(filename, lines):#寫入檔名與內容
    with open(filename, 'w') as f:
        for line in lines:#讀取檔案中每一行
            f.write(line + '\n')#寫入+換行

    
def main():
    lines = read_file('-LINE-Viki.txt')#將回傳的東西存成lines，並確定檔名
    lines = convert(lines)
    #write_file('output.txt', lines)#寫出檔案


main()
