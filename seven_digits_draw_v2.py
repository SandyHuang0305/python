#7段數碼管倒計時h測試
import turtle, time

def drawGap(): #數碼管間格
    turtle.penup()
    turtle.fd(5)
def drawLine(draw): #畫單段數碼管
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawDigit(d): #根據數字來繪製數碼管
    drawLine(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9 ] else drawLine(False)
    drawLine(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawCount(count):
    turtle.pensize(10)
    turtle.pencolor('blue')
    for i in range(10,0,-1): 
        drawDigit(i)  
        time.sleep(1) 
        turtle.reset()
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(10)
    turtle.pencolor('blue')
    drawCount('')
    #turtle.reset()
    turtle.write('時間到了', font=('Arial', 40, 'normal'))
    turtle.hideturtle()
    turtle.done()   
main()
