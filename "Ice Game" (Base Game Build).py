import turtle
import math
import os
import random







uname = input("To start the game, please enter a username")

print("Have Fun,", uname + "." )

wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Ice Game")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

score = 0

#draw the score in turtle
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("black")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score %s" %score
score_pen.write(scorestring, False, align="left", font=("Comic Sans MS", 14, "normal"))
score_pen.hideturtle()

level = 1


#create the level
level_pen = turtle.Turtle()
level_pen.speed(0)
level_pen.color("black")
level_pen.penup()
level_pen.setposition(-290, 250)
levelstring = "Level %s" %level
level_pen.write(levelstring, False, align="left", font=("Comic Sans MS", 14, "normal"))
level_pen.hideturtle()



#Add Credits



number_of_enemies = 10
#Create a list
enemies = []

#add enemies to the list
for i in range(number_of_enemies):
    #Create The Enemy
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("gray")
    enemy.shape("circle")
    enemy.speed(0.50)
    enemy.penup()
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    enemy.setposition(x, y)
    enemyspeed = 1

number_of_pellets = 15
#Create a list
pellets = []

#add point pellets
for i in range(number_of_pellets):
    #Create The Enemy
    pellets.append(turtle.Turtle())
for pellet in pellets:
    pellet.color("blue")
    pellet.shape("circle")
    pellet.speed(0.50)
    pellet.penup()
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    pellet.setposition(x, y)
    pelletspeed = 1


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("brown")
        self.penup()
        self.shape("square")
        self.speed(0)
        self.speed = 1
        self.friction = 0.99

    def turnleft(self):
        self.left(30)

    def turnright(self):
        self.right(30)

    def increasespeed(self):
        self.speed += 1

    def deacreasespeed(self):
        self.speed += -1

    def exitgame(self):
        print("Game Over")
        player.hideturtle()







    def crodits(self):
        credit_pen = turtle.Turtle()
        credit_pen.speed(0)
        credit_pen.color("black")
        credit_pen.penup()
        credit_pen.setposition(-290, 220)
        credit_pen.write(("Made by Liam Giraldo, Music by hmmm101"), align="left", font=("Comic Sans MS", 14, "normal"))
        credit_pen.hideturtle()



    def move(self):
        self.speed *= self.friction
        self.fd(self.speed)









        if self.xcor() > 290 or self.xcor() < -290:
            self.left(90)
            os.system("afplay pixelhit.wav&")

        if self.ycor() > 290 or self.ycor() < -290:
            self.right(90)
            os.system("afplay pixelhit.wav&")


    def song1(self):
        os.system("afplay MainTrack.wav&")

    def song2(self):
        os.system("afplay SecondTrack.wav&")

    def song3(self):
        os.system("afplay ThirdTrack.wav&")

def isCollision(t1, t2):
        distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
        if distance < 20:
            return True
        else:
            return False





player = Player()


turtle.listen()
wn.onkey(player.turnleft, "a")
wn.onkey(player.turnright, "d")
wn.onkey(player.increasespeed, "w")
wn.onkey(player.deacreasespeed, "s")
wn.onkey(player.exitgame, "p")
wn.onkey(player.crodits, "o")
wn.onkey(player.song1, "1")
wn.onkey(player.song2, "2")
wn.onkey(player.song3, "3")



while True:
    player.move()

    for enemy in enemies:
        if isCollision(player, enemy):
            os.system("afplay phit.wav&")

    for pellet in pellets:
        if isCollision(player, pellet):
            os.system("afplay Coin.wav&")
            pellet.hideturtle()
            score += 10
            scorestring = "Score: %s" % score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Comic Sans MS", 14, "normal"))

    #bug list
#passing through the corner of the border (not VERY important)
#enemy sounds staying after turtle hides (absolutely fix)
#turtle in the middle (not too important)
#music continuing after closing the program (play time will probably be extended)
#multiple sounds playing when an enemy or pellet is hit (absolutely fix)
#not all spikes / pellets work (absolutely fix)
#music stacking (users problem)
#screensize (not too important)
#music continuing after death of player
#sounds continuing after enemy/player turtle is hidden
#scoretring continues after turtle is hidden


    #for home
#make the levelstring do something
#fix bugs
#add questions after hitting a spike
#die rn