#雪花曲線
import turtle as t
def koch(size, n):
    if n == 0:
        t.fd(size) #若n = 0則畫直線
    else: #畫角度
        for angle in [0, 60, -120, 60]:
            t.left(angle)
            koch(size/3, n-1)
def main():
    t.setup(800, 400) #設定畫布大小
    t.penup()
    t.goto(-300, -50)
    t.pendown()
    t.pensize(2)
    koch(600, 3)
    t.hideturtle()
    t.done()
main()
