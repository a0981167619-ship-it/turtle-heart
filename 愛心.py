import turtle as tk
import math
import random

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
m_t=tk.Turtle() #畫月亮用的海龜
t_t=tk.Turtle() #畫樹用的海龜
w_t=tk.Turtle() #畫波浪用的海龜

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

def heart2(): #畫右上角的愛心
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
    h_t2.write("O",align='center',font=("Playfair Display",20)) #嵌入文字

    h_t2.hideturtle() #隱藏海龜
    
h_t3.pencolor("#FF21EC")
h_t3.fillcolor("#FF21EC")
h_t3.pensize(4)
def heart3(): #畫左上角的愛心
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
    h_t3.write("L",align='center',font=("Playfair Display",20))  #嵌入文字
    h_t3.hideturtle() #隱藏海龜
    
h_t4.pencolor("#F736BD")
h_t4.fillcolor("#F736BD")
h_t4.pensize(4)
def heart4(): #畫左下角的愛心
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
    h_t4.write("V",align='center',font=("Playfair Display",20)) #嵌入文字
    h_t4.hideturtle() #隱藏海龜
        
h_t5.pencolor("#FF3A96")
h_t5.fillcolor("#FF3A96")
h_t5.pensize(4)
def heart5(): #畫右下角的愛心
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
    h_t5.write("E",align='center',font=("Playfair Display",20)) #嵌入文字

    h_t5.hideturtle() #隱藏海龜
            

    
    
l_t.pencolor("yellow")
l_t.pensize(4)
def line(): #畫愛心旁邊的線條
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


x=-200
y=350

x1=200
y1=-120

x2=-200
y2=-120    #設置各顆星星的座標

x3=300
y3=340

x4=-300
y4=-50

x5=450
y5=120

x6=-400
y6=200
def star(): #星星
    global x,y #全域範圍
    s_t.clear()
    s_t.penup()
    s_t.goto(x,y)
    s_t.pendown()
    s_t.pencolor('#C7E9FF')
    s_t.right(120)
    s_t.forward(90)
    for i in range(5):
              s_t.right(20)
              s_t.forward(30)
              s_t.right(120)
              s_t.forward(30)

    global x1,y1
    s_t.penup()
    s_t.goto(x1,y1)
    s_t.pendown()
    s_t.pencolor('#FFF8F5')
    s_t.right(120)
    s_t.forward(120)
    for i in range(5):
              s_t.right(20)
              s_t.forward(30)
              s_t.right(120)
              s_t.forward(30)

    global x2,y2
    s_t.penup()
    s_t.goto(x2,y2)
    s_t.pendown()
    s_t.pencolor('#FFF8F5')
    s_t.right(110)
    s_t.forward(120)
    for i in range(5):
                  s_t.right(20)
                  s_t.forward(30)
                  s_t.right(120)
                  s_t.forward(30)

    global x3,y3
    s_t.penup()
    s_t.goto(x3,y3)
    s_t.pendown()
    s_t.pencolor('#AEE8FF')
    s_t.left(170)
    s_t.forward(90)
    for i in range(5):
                      s_t.right(20)
                      s_t.forward(30)
                      s_t.right(120)
                      s_t.forward(30)

    global x4,y4
    s_t.penup()
    s_t.goto(x4,y4)
    s_t.right(30)
    s_t.pendown()
    s_t.pencolor('#B9E8FF')
    s_t.forward(90)
    for i in range(5):
                    s_t.right(20)
                    s_t.forward(30)
                    s_t.right(120)
                    s_t.forward(30)

    global x5,y5 #全域範圍
    s_t.penup()
    s_t.goto(x5,y5)
    s_t.right(30)
    s_t.pendown()
    s_t.pencolor('#F4F8FF')
    s_t.forward(90)
  
    for i in range(5):
                  s_t.right(20)
                  s_t.forward(30)
                  s_t.right(120)
                  s_t.forward(30)

    global x6,y6
    s_t.setheading(90)
    s_t.penup()
    s_t.goto(x6,y6)
    s_t.pencolor("#C9E5F5")
    s_t.pendown()
    s_t.right(110)
    s_t.forward(120)
   
  
    for i in range(5):
                  s_t.right(20)
                  s_t.forward(30)
                  s_t.right(120)
                  s_t.forward(30)

    s_t.penup()
    s_t.goto(-100,350)
    s_t.pencolor("#D1E3EF")
    s_t.pendown()
    for i in range(5):
                  s_t.right(20)
                  s_t.forward(30)
                  s_t.right(120)
                  s_t.forward(30)

    s_t.penup()
    s_t.goto(30,250)
    s_t.pencolor("#DCEAF4")
    s_t.pendown()
    for i in range(5):
                      s_t.right(20)
                      s_t.forward(30)
                      s_t.right(120)
                      s_t.forward(30)
    
    s_t.hideturtle() #隱藏海龜

color=["#FFFFFF","#BDEBFF","#7DD3FC","#38BDF8","#60A5FA","#818CF8","#A5B4FC",]  #顏色序列
dot2=[] #設置存星星座標的串列
def dot(): #星點
    tk.tracer(0)
    d_t.clear()
    for i in range(1000):
           d_t.penup()
           if len(dot2)<1000: #星星的數量要小於1000顆
             x=random.randint(-700,700)  #x與y的隨機取數範圍
             y=random.randint(-400,400)
             a=[-1,1] #星點移動的速度
             speed=random.choice(a)
             dot2.append([x,y,speed]) #加入串列
          
           else: #如果星點數量大於1000顆
                  x=dot2[i][0]
                  y=dot2[i][1]   #儲存星星的座標
                  speed=dot2[i][2]

           y+=speed #移動星星
           dot2[i][1]=y #將移動後的星星座標存回串列

           d_t.goto(x,y)
           d_t.pendown()
           d_t.pencolor(random.choice(color)) #隨機選取星點的顏色
           d_t.dot(5) #星點的大小
           d_t.hideturtle() #隱藏海龜
        
    screen.update() #更新
    screen.ontimer(dot,30) #每30秒觸發一次

m_t.pencolor("#FBFF03")
m_t.pensize(4)
m_t.fillcolor("#FBFF03")
def moon(): #月亮
      m_t.begin_fill()
      m_t.penup()
      m_t.goto(100,270)
      m_t.circle(50,360)
      m_t.end_fill()
   
      m_t.pencolor('black')
      m_t.fillcolor('black')
      m_t.pensize(4)
      m_t.penup()
      m_t.goto(85,270)
      m_t.pendown()
      m_t.begin_fill()
      m_t.circle(50,360)
      m_t.end_fill()


def tree(): #樹
       t_t.penup()
       t_t.goto(260,-200)
       t_t.pencolor("#0A752E")
       t_t.fillcolor("#0A752E")
       t_t.begin_fill()
       t_t.pensize(4)
       t_t.pendown()
       t_t.setheading(0)
       t_t.circle(20,150)
       t_t.right(80)
       t_t.circle(20,150)
       t_t.right(70)
       t_t.circle(20,150)
       t_t.right(100)
       t_t.circle(20,150)
       t_t.right(-15)
       t_t.forward(50)
       t_t.end_fill()

       t_t.setheading(270) #面朝正下方
       t_t.penup()
       t_t.goto(260,-205)
       t_t.pendown()
       t_t.fillcolor("#2C2203")
       t_t.pencolor("#2C2203")
       t_t.begin_fill()
       t_t.forward(190)
       t_t.setheading(180)
       t_t.forward(35)
       t_t.setheading(90)
       t_t.forward(190)
       t_t.end_fill()

       t_t.penup()
       t_t.goto(-215,-200)
       t_t.pencolor("#0A752E")
       t_t.fillcolor("#0A752E")
       t_t.begin_fill()
       t_t.pensize(4)
       t_t.pendown()
       t_t.setheading(0)
       t_t.circle(20,150)
       t_t.right(80)
       t_t.circle(20,150)
       t_t.right(70)
       t_t.circle(20,150)
       t_t.right(100)
       t_t.circle(20,150)
       t_t.right(-15)
       t_t.forward(50)
       t_t.end_fill()
       
       t_t.setheading(270) #面朝正下方
       t_t.penup()
       t_t.goto(-215,-205)
       t_t.pendown()
       t_t.fillcolor("#2C2203")
       t_t.pencolor("#2C2203")
       t_t.begin_fill()
       t_t.forward(190)
       t_t.setheading(180)
       t_t.forward(35)
       t_t.setheading(90)
       t_t.forward(190)
       t_t.end_fill()

x8=-210
x9=-210
x10=-210
def wave(): #畫兩棵樹中間的波浪
        global x8,x9,x10
        w_t.pencolor("#1599F1")
        w_t.pensize(4)

        for j in range(10):
         w_t.penup()
         w_t.goto(x8,-350)
         w_t.pendown()

         w_t.setheading(0) #海龜面朝右方
         w_t.left(10)
         w_t.forward(20)
         w_t.circle(5,180)

         x8+=45 #改變x的座標

        for i in range(10):
         w_t.penup()
         w_t.goto(x9,-370)
         w_t.pendown()
         
         w_t.setheading(0)
         w_t.left(10)
         w_t.forward(20)
         w_t.circle(5,180)
         x9+=45

         for i in range(10):
          w_t.penup()
          w_t.goto(x10,-385)
          w_t.pendown()
                  
         w_t.setheading(0)
         w_t.left(10)
         w_t.forward(20)
         w_t.circle(5,180)

         x10+=45

        w_t.hideturtle() #隱藏海龜

heart() #呼叫函式
line()
heart2()
heart3()
heart4()
heart5()
star()
dot()
moon()
tree()
wave()
tk.done()




