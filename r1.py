#對話紀錄練習
#讀取檔案
def read_file(filename):
    lines = []#創作清單
    with open (filename, 'r', encoding='utf-8-sig') as f:
        for line in f:#用for迴圈讀檔案
            lines.append(line.strip())#裝進清單#去掉換行符號
    return lines#回傳清單

#轉換
def convert(lines):
    new = []#創造空清單
    person = None #處理當開頭不是人名的狀況
    for line in lines:#把lines清單的東西叫出來
        if line == 'Allen':
            person = 'Allen' #把Allen裝進person
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        new.append(person + ':' + line) #處理每一行       
    return new

#寫入檔案
def write_file(filename, lines):#寫入檔名與內容
    with open(filename, 'w') as f:
        for line in lines:#讀取檔案中每一行
            f.write(line + '\n')#寫入+換行

    
def main():
    lines = read_file('input.txt')#將回傳的東西存成lines，並確定檔名
    lines = convert(lines)
    write_file('output.txt', lines)#寫出檔案


main()
