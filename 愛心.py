import turtle as tk
import math

screen=tk.Screen()
screen.title("heart") 
screen.bgcolor("black") #設置畫布的顏色

h_t=tk.Turtle() #畫愛心用的海龜
h_t2=tk.Turtle()
h_t3=tk.Turtle()
h_t4=tk.Turtle()
h_t5=tk.Turtle()
s_t=tk.Turtle() #畫星星用的海龜
l_t=tk.Turtle() #畫線條用的海龜
d_t=tk.Turtle() #畫星點用的海龜

h_t.goto(0,0)
h_t.pencolor("#EE98FF") #設置畫筆的顏色
h_t.fillcolor("#EE98FF") #填充顏色

size=5
change=0.5

def heart():
    global size,change #變數為全域範圍
    h_t.clear() #清除上一幀
    h_t.begin_fill() #再開始填色
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

h_t2.pencolor("#F16AFD")
h_t2.pensize(4)
h_t2.fillcolor("#F16AFD")

def heart2():
    h_t2.penup()
    h_t2.goto(400,300)
   
    h_t2.pendown()

    h_t2.begin_fill()
    h_t2.circle(30,220)
    h_t2.right(120)
    h_t2.circle(30,220)
    h_t2.penup()
    h_t2.goto(400,300)
    h_t2.pendown()
    h_t2.right(130)
    h_t2.forward(30)
    h_t2.right(48.5)
    h_t2.forward(50)

    h_t2.end_fill()


    h_t2.penup()
    h_t2.pencolor("#FBFF07")
    h_t2.goto(375,315)
    h_t2.pendown()
    h_t2.write("O",align='center',font=("Playfair Display",20))

    h_t2.hideturtle() #隱藏海龜
    

h_t3.pencolor("#FF21EC")
h_t3.fillcolor("#FF21EC")
h_t3.pensize(4)
def heart3():
    h_t3.penup()
    h_t3.goto(-390,300)
    
    h_t3.pendown()
    
    h_t3.begin_fill()
    h_t3.circle(30,220)
    h_t3.right(120)
    h_t3.circle(30,220)
    h_t3.penup()
    h_t3.goto(-390,300)
    h_t3.pendown()
    h_t3.right(130)
    h_t3.forward(30)
    h_t3.right(48.5)
    h_t3.forward(50)
    
    h_t3.end_fill()
    
    
    h_t3.penup()
    h_t3.pencolor("#FEFFB5")
    h_t3.goto(-415,315)
    h_t3.pendown()
    h_t3.write("L",align='center',font=("Playfair Display",20))
    h_t3.hideturtle()
    

h_t4.pencolor("#F736BD")
h_t4.fillcolor("#F736BD")
h_t4.pensize(4)
def heart4():
    h_t4.penup()
    h_t4.goto(-390,-340)
    
    h_t4.pendown()
        
    h_t4.begin_fill()
    h_t4.circle(30,220)
    h_t4.right(120)
    h_t4.circle(30,220)
    h_t4.penup()
    h_t4.goto(-390,-340)
    h_t4.pendown()
    h_t4.right(130)
    h_t4.forward(30)
    h_t4.right(48.5)
    h_t4.forward(50)
        
    h_t4.end_fill()
        
        
    h_t4.penup()
    h_t4.pencolor("#FEFFB5")
    h_t4.goto(-415,-330)
    h_t4.pendown()
    h_t4.write("V",align='center',font=("Playfair Display",20))
    h_t4.hideturtle()
        
            

h_t5.pencolor("#FF3A96")
h_t5.fillcolor("#FF3A96")
h_t5.pensize(4)
def heart5():
    h_t5.penup()
    h_t5.goto(400,-340)
            
    h_t5.pendown()
            
    h_t5.begin_fill()
    h_t5.circle(30,220)
    h_t5.right(120)
    h_t5.circle(30,220)

    h_t5.penup()
    h_t5.goto(400,-340)
    h_t5.pendown()
    h_t5.right(130)
    h_t5.forward(30)
    h_t5.right(48.5)
    h_t5.forward(50)
            
    h_t5.end_fill()
            
            
    h_t5.penup()
    h_t5.pencolor("#FEFFB5")
    h_t5.goto(380,-330)
    h_t5.pendown()
    h_t5.write("E",align='center',font=("Playfair Display",20))

    h_t5.hideturtle()
            

    
    
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
    l_t.hideturtle()

s_t.pencolor("#DBDBD9")
s_t.pensize(3)
def star():
    s_t.penup()
    s_t.goto(-200,350)
    s_t.pendown()
    s_t.right(120)
    s_t.forward(90)
    for i in range(5):
              s_t.right(20)
              s_t.forward(30)
              s_t.right(120)
              s_t.forward(30)


    s_t.penup()
    s_t.goto(200,-170)
    s_t.pendown()
    s_t.right(120)
    s_t.forward(120)
    for i in range(5):
              s_t.right(20)
              s_t.forward(30)
              s_t.right(120)
              s_t.forward(30)

    s_t.penup()
    s_t.goto(-200,-170)
    s_t.pendown()
    s_t.right(110)
    s_t.forward(120)
    for i in range(5):
                  s_t.right(20)
                  s_t.forward(30)
                  s_t.right(120)
                  s_t.forward(30)

    s_t.penup()
    s_t.goto(200,340)
    s_t.pendown()
    s_t.left(170)
    s_t.forward(90)
    for i in range(5):
                      s_t.right(20)
                      s_t.forward(30)
                      s_t.right(120)
                      s_t.forward(30)



    
heart() #呼叫函式
line()
heart2()
heart3()
heart4()
heart5()
star()
tk.done()




