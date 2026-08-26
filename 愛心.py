import turtle as tk
import math

screen=tk.Screen()
screen.title("heart") 
screen.bgcolor("black") #設置畫布的顏色

h_t=tk.Turtle() #畫愛心用的海龜
l_t=tk.Turtle() #畫線條用的海龜
s_t=tk.Turtle() #畫雪花用的海龜

h_t.goto(0,0)
h_t.pencolor("#EE98FF") #設置畫筆的顏色
h_t.fillcolor("#EE98FF") #填充顏色

size=5
change=0.5

def heart():
    global size,change #變數為全域範圍
    h_t.clear() #清除上一幀
    h_t.begin_fill() #在開始填色
    for i in range(361):
        tk.tracer(0)
        t=math.radians(i)
        x=size*(16*math.sin(t)**3)  #愛心參數式(參考網路公式)
        y=size*(13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t))

        h_t.goto(x,y)

    h_t.end_fill()
    h_t.pencolor("#FFF200")
    h_t.penup()
    h_t.goto(0,-20)
    h_t.write("LOVE",align='center',font=("Segoe Script",20)) #嵌入文字
    h_t.hideturtle() #隱藏海龜
    screen.update() #更新

    size+=change
    if size>=6:
        change=-0.3   #改變愛心的大小
    if size<=5:
        change=0.3

    screen.ontimer(heart,20) #用成類似於動畫的效果

l_t.pencolor("yellow")
l_t.pensize(4)
def line(): 
    l_t.penup()
    l_t.goto(150,50)
    l_t.pendown()
    l_t.forward(20)
    l_t.left(60)
    l_t.forward(20)
    l_t.right(100)
    l_t.forward(25)

    l_t.penup() 

    l_t.goto(-150,50)

    l_t.pendown()
    l_t.right(150)
    l_t.forward(20)
    l_t.right(45)
    l_t.forward(20)
    l_t.left(120)
    l_t.forward(20)
    l_t.right(60)
    l_t.forward(20)

def snow():
    s_t.penup()
    s_t.goto()

    
heart() #呼叫函式
line()
h_t.end_fill()
tk.done()


