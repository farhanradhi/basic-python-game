import turtle
import time
import random

delay = 0.1

#score
score = 0
high_score = 0

#screen
sc = turtle.Screen()
sc.title("Ular Game")
sc.bgcolor("green")
sc.setup(width=600, height=600)
sc.tracer(0) #mematikan screen update

#kepala ular
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

#makanan ular
food = turtle.Turtle()
food.speed(0)
food.shape("triangle")
food.color("blue")
food.penup()
food.goto(0,100)

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score : 0   High Score: 0", align="center", font=("Courier", 24, "normal"))



#fungsi 
def go_up():
    if head.direction != "down":
        head.direction = "up"
    
def go_down():
    if head.direction != "up":
        head.direction = "down"
    
def go_left():
    if head.direction != "right":
        head.direction = "left"
    
def go_right():
    if head.direction != "left":
        head.direction = "right"

#fungsi 
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction == "down":
        y = head.ycor() 
        head.sety(y - 20) 
           
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20) 

#keyboard bindings
sc.listen()
sc.onkeypress(go_up, "w")
sc.onkeypress(go_down, "s")
sc.onkeypress(go_left, "a")
sc.onkeypress(go_right, "d")
               
#main game loop
while True:
    sc.update()
    
    #check border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
       time.sleep(1)
       head.goto(0.0)
       head.direction = "stop"    
        
    #check for collision with the food
    if head.distance(food) < 20:
        #move random spot
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        food.goto(x,y)
        
        # add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
        #shorten the delay
        delay -= 0.001
        
        # increase the score
        score += 10
        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {} High Score: {} ".format(score,high_score), align="center", font=("Courier", 24,"normal"))    
        
    # move the end segment first in reverse model
    for index in range(len(segments)-1 ,0 ,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    
    #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
            
    
    move()
    
    #check for head with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0.0)
            head.direction = "stop"
            
            #hide segment
            for segment in segments:
                segment.goto(1000, 1000)
                
            #clear segment
            segment.clear()
            
            #reset the score
            score = 0
            
            pen.clear()
            pen.write("Score: {} High Score: {} ".format(score,high_score), align="center", font=("Courier", 24,"normal"))  
    
    time.sleep(delay)
    
sc.mainloop()
