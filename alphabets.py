print ("Hello and welcome to word drawing")
text = input ("Enter your text you want to print:")
thick = input ("How thick would you like it? (min:1 max:100)")
import turtle
forward=turtle.forward
back=turtle.backward
right=turtle.right
left=turtle.left
pup=turtle.penup
pdown=turtle.pendown
thickness=turtle.width
thickness(thick)
pup()
left(180)
forward(400)
left(180)
pdown()

def space():
    pup()
    forward(100)
    pdown()

def a():
    for i in range(450): #this is an A
        forward(2)
        left(1)
    forward(140)
    right(180)
    forward(240)
    for i in range(90):
        forward(1)
        left(1)
    pup()
    forward(100)
    left(90)
    forward(25)
    right(90)
    pdown()

def b():
    left(90)
    forward(300)
    back(250)
    for i in range(180):
        forward(3)
        right(2)
    back(100)
    pup()
    right(90)
    forward(300)
    pdown()

def c():
    pup()
    forward(100)
    left(90)
    forward(50)
    right(90)
    pdown()
    right(135)
    for i in range(275):
        forward(2)
        right(1)
    pup()
    right(45)
    forward(200)
    left(90)
    forward(100)
    pdown()

def d():
    left(90)
    forward(300)
    back(250)  
    for i in range(180):
        forward(3)
        left(2)
    back(100)
    pup()
    left(90)
    forward(300)
    pdown()
def e():
    forward(100)
    back(100)
    left(90)
    forward(100)
    left(90)
    back(100)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)

def f():
    left(90)
    forward(100)
    right(90)
    forward(100)
    back(100)
    forward(100)
    back(100)
    left(90)
    forward(100)
    right(90)
    forward(100)
def g():
    left(90)
    forward(70)
    left(90)
    forward(70)
    left(90)
    forward(63)
    left(90)
    pdown()
    right(135)
    for i in range(275):
        forward(2)
        right(1)
    pup()
    right(45)
    forward(300)
    left(90)
    forward(100)
    pdown()
   
   
def h():
    left(90)
    forward(200)
    back(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    back(200)
def i():
    forward(200)
    back(100)
    right(90)
    forward(150+100)
    right(90)
    forward(100)
    back(200)
def j():
    pup()
    forward(100)
    right(90)
    forward(50)
    right(90)
    pdown()
    left(135)
    for i in range(100):
        forward(2)
        left(1)
    right(320+5)
    forward(220)
    right(90)
    forward(90)
    back(180)
def m():
    left(90)
    forward(150)
    right(90)
    forward(20)
    right(45)
    forward(50)
    forward(50)
    left(90+5)
    forward(90)
    right(45)
    forward(20)
    right(90)
    forward(150)
def k():
    left(90)
    forward(200)
    back(80)
    left(90+90+45)
    forward(120)
    back(90)
    left(90+20)
    forward(120)
   
def l():
    forward(100)
    back(100)
    left(90)
    forward(150)

def n():
    left(90)
    forward(100)
    right(90+45)
    forward(120)
    left(90+45)
    forward(100)
   
def o():
    turtle.circle(100)

def p():
    right(90)
    forward(300)
    back(250)
    for i in range(180):
        forward(3)
        left(2)
    back(100)
    pup()
    left(90)
    forward(300)
    pdown()
   
def q():
    turtle.circle(100)
    right(60)
    forward(50)
    back(80)
def r():
    left(90)
    forward(200)
    right(90)
    forward(80)
    right(90)
    forward(80)
    right(90)
    forward(80)
    back(30)
    right(90+45+45+68)
    forward(100+30)
   
def s():
    forward(90)
    left(90)
    forward(40)
    left(90)
    forward(90)
    right(90)
    forward(40)
    right(90)
    forward(90)
def t():
    left(90)
    forward(180)
    left(90)
    forward(80)
    back(160)
def u():
    right(90)
    forward(100)
    left(90)
    forward(60)
    right(90)
    forward(100)
   
def v():
    right(45+20)
    forward(200)
    left(90+45)
    forward(200)
   
def w():
    right(45+20)
    forward(200)
    left(90+45)
    forward(200)
    right(45+20)
    forward(200)
    left(90+45)
    forward(200)
def x():
    left(90+45)
    forward(200)
    back(100)
    right(90)
    forward(100)
    back(200)
def y():
    left(90)
    forward(100)
    right(45)
    forward(100)
    back(100)
    left(90)
    forward(100)

def z():
    forward(100)
    right(90+45)
    forward(130)
    left(90+45)
    forward(100)

draw = {" ":space, "a":a, "b":b, "c":c,"d":d,"e":e,"f":f,"g":g,"h":h,"i":i,"j":j,"k":k,"l":l,"m":m,"n":n,"o":o,"p":p,"q":q,"r":r,"s":s,"t":t,"u":u,"v":v,"w":w,"x":x,"y":y,"z":z}

for letter in text:
    if letter in draw.keys():
        draw[letter]()
turtle.exitonclick()
