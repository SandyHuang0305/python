#如何從清單中取出東西

lines = []
with open ('3.txt', 'r', encoding = 'utf-8-sig') as f:
    for line in f:
        lines.append(line)

for line in lines:
    s = line.split(' ') #切割
    time = s[0][:5] #分割清單
    name = s[0][5:]
    print(name)       