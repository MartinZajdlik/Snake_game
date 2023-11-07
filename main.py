### hra je dělana podle tutorialu Davida Šetka
#ovládání klávesy W,A,S a D 

from turtle import Turtle, Screen , exitonclick
import time
import random

#promenne
score= 0
highest_score = 0

screen = Screen()
screen.bgcolor("black")
screen.title("WELCOME IN SNAKE GAME")
screen.setup(width = 600, height = 600)
screen.tracer(False)

# Hadi hlava,telo a potrava
head = Turtle("square")
head.color("dark green") 
head.speed(0)           #na začatku bez pohybu
head.penup()            #zvedne pero, had nesmi kreslit caru
head.goto(0,0)          #zacatek uprostřed
head.direction = "stop"

apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(100,100)

score_sign = Turtle("square")
score_sign.speed(0)
score_sign.color("white")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0,265)
score_sign.write(f"Score: {score} Nejvyšší skore: {highest_score}",align="center", font=("Arial",18))

body_parts = []

#Funkce
def move():
    if head.direction == "up":
        y=head.ycor()         
        head.sety(y+20)
        
    if head.direction == "down":
        y=head.ycor()
        head.sety(y-20)
        
    if head.direction == "left":
        x=head.xcor()
        head.setx(x-20)
        
    if head.direction == "right":
        x=head.xcor()
        head.setx(x+20)
        
def move_up():
    if head.direction != "down":
        head.direction = "up"
    
def move_down():
    if head.direction != "up":
        head.direction = "down"
    
def move_left():
    if head.direction != "right":
        head.direction = "left"
    
def move_right():
    if head.direction != "left":
        head.direction = "right"

#kliknuti na klavesy
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

    
#hlavni cyklus        
while True:
    screen.update()
    
    #kontrola kolize s hranou obrazovky
    if head.xcor()>290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor()<-290:
        time.sleep(2)
        head.goto(0,0)
        head.direction = "stop"
        
        #skryjeme casti hada po kolizi
        for one_body_part in body_parts:
            one_body_part.goto(1500,1500)   #posle ctverecky mimo platno
            
        #vyprazdnime list s castmi tela
        body_parts.clear()   
        
        #resetovani skore
        score = 0
        
        score_sign.clear()   
        score_sign.write(f"Score: {score} Nejvyšší skore: {highest_score}",align="center", font=("Arial",18))    
    
    
    #had sni jablko
    if head.distance(apple) < 20:        
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        apple.goto(x,y)
        
        
        # přidani casti tela
        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("green")
        new_body_part.penup()
        body_parts.append(new_body_part)
        
        score+=10
        if score > highest_score:
            highest_score = score
            
        score_sign.clear()   
        score_sign.write(f"Score: {score} Nejvyšší skore: {highest_score}",align="center", font=("Arial",18))
    
        
    #pridavani tela hada za sebe
    for i in range(len(body_parts)-1,0,-1):
        x = body_parts[i - 1].xcor()
        y = body_parts[i - 1].ycor()
        body_parts[i].goto(x,y)
    
        
    if len(body_parts)>0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x,y)
        
    move()
    
    # hlava narazila do tela    
    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20:
            time.sleep(2)
            head.goto(0,0)
            head.direction = "stop"
            
            #skryjeme casti hada po kolizi
            for one_body_part in body_parts:
                one_body_part.goto(1500,1500)   #posle ctverecky mimo platno
                
            #vyprazdnime list s castmi tela
            body_parts.clear()        
        
             #resetovani skore
            score = 0
            
            score_sign.clear()   
            score_sign.write(f"Score: {score} Nejvyšší skore: {highest_score}",align="center", font=("Arial",18))    
        
    time.sleep(0.1)

screen.exitonclick()
