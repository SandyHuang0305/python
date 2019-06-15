#PythonDraw.py
#以絕對方向與絕對角度定義
import turtle
turtle.setup(650, 350, 200, 200) #定義窗體大小#非必須設置
turtle.penup()
turtle.fd(-250) #向前運行
turtle.pendown()
turtle.pensize(25)
turtle.pencolor('cyan')
turtle.seth(-40) #改變行進角度senth(angle)
for i in range(4):
    turtle.circle(40, 80) #曲線運行
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()