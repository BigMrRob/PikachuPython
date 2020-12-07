import turtle
# main// x = xcos() + ysin()
# main// y = -xsin() + ycos()
import math

global t
t = turtle.Turtle() # turtle instance
screen = turtle.Screen() # screen
screen.screensize(600, 600) # screen size
#t1 = turtle.Turtle()
turtle.bgcolor("yellow") # initial bg color
t.speed(0)

def initial(x , y): # -120 , 80 # initial values set to turlte
    # pen setup
    t.penup()
    t.setposition(x , y)
    t.hideturtle()
    t.pendown()
    #t.showturtle()

def first_circle_main_eye(c = 50): # main eye
    # first circle main eye
    t.begin_fill()
    t.fillcolor("black")
    t.circle(c)
    t.end_fill()

def first_eye_white_area(x , y , c = 10): # -100 , 130 # main eye white part
    # first eye white area
    t.setposition(x , y)
    t.begin_fill()
    t.fillcolor("white")
    t.circle(c)
    t.end_fill()
    t.penup()

def second_eye_main_eye(x , y , c = 50): # 120 , 80 # second main eye
    # 2nd eye circle main eye
    t.setposition(x , y)
    t.pendown()
    t.begin_fill()
    t.fillcolor("black")
    t.circle(c)
    t.end_fill()

def second_eye_white_area(x , y , c = 10): # 100 , 130 # second eye white part
    # 2nd eye white area
    t.setposition(x , y)
    t.begin_fill()
    t.fillcolor("white")
    t.circle(c)
    t.end_fill()
    t.penup()


def triangle(x , s2 = 50 , s1 = 70): # 45 # triangle mouth
    # triangle 0 , 0
    t.setposition(0 , 0)
    t.pendown()
    t.begin_fill()
    t.fillcolor("black")
    t.left(x) # 45
    t.forward(s2) 
    t.left(135) # 135
    t.forward(s1)
    t.left(135) # 135
    t.forward(s2)
    t.right(45) #
    t.end_fill()
    t.penup()

def mostach(x , y , c1 = 50 , c2 = 150): # 0 , -30 # mostach
    # breth
    t.setposition(x , y)
    t.pendown()
    t.width(4)
    t.circle(-c1 , c2)
    t.penup()
    t.setposition(x , y)
    t.pendown()
    t.left(-30)
    t.circle(-c1 , -c2)
    t.width(1)
    t.penup()
    t.setposition(0 , 0)


def first_face(x , y , c = 60): #140 , -80 # first face
    # first face
    t.setposition(x , y)
    t.pendown()
    t.begin_fill()
    t.fillcolor("red")
    t.circle(c)
    t.end_fill()
    t.penup()

def second_face(x , y , c = 60): # -250 , -80 # second face
    # 2nd face
    t.setposition(x , y)
    t.pendown()
    t.begin_fill()
    t.fillcolor("red")
    t.circle(c)
    t.end_fill()
    t.penup()

# face end

def space(): # space function for default activation
    t.clear()
    #t.destroy()
    #screen.clearturtlescreen()
    t.sety(0)
    t.setposition(0,0)
    initial(-120 , 80)
    first_circle_main_eye()
    first_eye_white_area(-100 , 130)
    second_eye_main_eye(120 , 80)
    second_eye_white_area(100 , 130)
    triangle(45)
    mostach(0 , -30)
    first_face(140 , -80)
    second_face(-250 , -80)


def up(): # up function for zoom
    
    t.clear()
    t.setposition(0,0)
    t.sety(0)
    initial(-350 , 200)
    first_circle_main_eye(100)
    first_eye_white_area(-210 , 170 , 20)
    second_eye_main_eye(200 , 200 , 100)
    second_eye_white_area(200 , 170 , 20)
    triangle(165 , 100 , 140)
    mostach(0 , -60 , 50 , 150)
    first_face(280 , -160 , 120)
    second_face(-500 , -160 , 120)

def down(): # down fucntion for zoom out 
    
    t.clear()
    t.setposition(0,0)
    t.sety(0)
    initial(-100 , 60)
    first_circle_main_eye(25)
    first_eye_white_area(-70 , 60 , 5)
    second_eye_main_eye(50 , 60 , 25)
    second_eye_white_area(60 , 60 , 5)
    triangle(165 , 25 , 35)
    mostach(0 , -15 , 25 , 150)
    first_face(80 , -40 , 30)
    second_face(-130 , -40 , 30)
 
def left(): # left for + 135 angle
    t.clear()
    t.setposition(0,0)
    t.sety(0)
    initial(-141.42 , -28)
    t.clear()
    initial(-28.28 , 200.42)
    first_circle_main_eye()
    first_eye_white_area(-21.21 , 162.63)    
    second_eye_main_eye(-200.42 , -35.28)
    second_eye_white_area(-162.63 , -21.21)
    triangle(220)
    mostach(21.21 , -21.21)
    first_face(-42.42 , -240.56)
    second_face(160.34 , 70.20)
    
    
def right(): # right for -45 angle
    t.clear()   
    initial(-141.42 , -28)
    t.clear()
    initial(-28.28 , 200.42)
    first_circle_main_eye()
    first_eye_white_area(21.21 , 162.63)
    
    second_eye_main_eye(141.42 , -28.28)
    second_eye_white_area(162.63 , -21.21)
    triangle(110)
    mostach(-21.21 , -21.21)
    first_face(42.42 , -155.56)
    second_face(-210.34 , 120.20)

def click_right(x , y): # click right function to activate orange color
    screen.bgcolor("orange")

def click_left(x , y): # to activate yellow color
    screen.bgcolor("yellow")

space() # main default state

turtle.listen()

turtle.onscreenclick(click_right , 3) # fuunction for right click
turtle.onscreenclick(click_left , 1) # for left click
turtle.onkey(up , 'Up') # for up button
turtle.onkey(down , 'Down') # for doown button
turtle.onkey(left , 'Left') # for left 
turtle.onkey(right , 'Right') # for right
turtle.onkey(space , 'space') # space for default

























