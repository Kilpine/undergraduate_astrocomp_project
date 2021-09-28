# Importing libraries
import turtle
import sys
#import winsound

# Create a screen with  the class .Screen()
sc = turtle.Screen()
sc.title('Star Pong!')
sc.bgcolor('white')
sc.setup(width = 800, height = 600)
sc.tracer(0)

# Now adding objects

# Paddle A is created using class .Turtle
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square') # 20 by 20 size by default
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.color('black')
paddle_a.penup() # Turtles by defintion draw a line so this removes that function
paddle_a.goto(-350, 0) # Puts paddle at certain destination using .goto(x,y)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.color('black')
paddle_b.penup()
paddle_b.goto(350, 0)

# Balls(star)
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('black')
ball.penup()
ball.goto(0,0)

intialdx = 0.1
intialdy = 0.1
ball.dx = intialdx 
ball.dy = intialdy

# Score
score_1 = 0
score_2 = 0
# Title
pen = turtle.Turtle()
pen.speed(0)
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: {} Player 2: {}".format(score_1,score_2), align = 'center', font = ('Courier', 24, 'normal'))

# Now we begin to create some functions
def paddle_a_up():
    y = paddle_a.ycor() # Gets the y-coordinate of the paddle
    y += 20
    paddle_a.sety(y)
    
    # Keyboard bindings
    sc.listen()
    sc.onkeypress(paddle_a_up, 'w')

def paddle_a_down():
    y = paddle_a.ycor() # Gets the y-coordinate of the paddle
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() # Gets the y-coordinate of the paddle
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() # Gets the y-coordinate of the paddle
    y -= 20
    paddle_b.sety(y)
    
# Keyboard bindings
sc.listen()
sc.onkeypress(paddle_a_up,'w')
sc.onkeypress(paddle_a_down,'s')
sc.onkeypress(paddle_b_up,'Up')
sc.onkeypress(paddle_b_down,'Down')

# Main game loop
while True:
    
    # Whenever the main game loop runs it updates the screen
    sc.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        ball.dy *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1,score_2), align = 'center', font = ('Courier', 24, 'normal'))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        ball.dy *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1,score_2), align = 'center', font = ('Courier', 24, 'normal'))
    
    # Paddle and ball collisons
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() > paddle_a.ycor() - 40 and ball.ycor() < paddle_a.ycor() + 40):
        ball.setx(-340)
        ball.dx *= -1