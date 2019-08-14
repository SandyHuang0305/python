#自動軌跡繪製
import turtle as t
t.title("自動軌跡繪製")
t.setup(800, 600, 0, 0) #定義視窗大小
t.pencolor("red")
t.pensize(5)


#數據讀取
datals = [] #製作列表
f = open("data.txt")
for line in f:
    line = line.replace("\n","")#去掉換行以空白代替
    if line != "":
        datals.append(list(map(eval,line.split(","))))
#用逗號來切割字串
#用map函數來設定字串，將每個字串做同樣eval的設定
#最後利用append放進上述定義的列表中
f.close()

#自動繪製
for i in range(len(datals)):
    t.pencolor(datals[i][3], datals[i][4], datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
t.done()