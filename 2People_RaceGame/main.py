# game project with "turtle"
import turtle
import random
import time

# p1 = player_one
# p2 = player_two

# setting screen
wn = turtle.Screen()
wn.title("race game")
turtle.bgpic(r"jungle.png")
wn.setup(width=800, height=600)
wn.tracer(0)


# setting p1's turtle and it's default start position
p1 = turtle.Turtle()
p1.penup()
p1.speed(10)
p1.pencolor("red")
p1.shape("turtle")
p1.goto(-200, 100)
p1.shapesize(2,2,2)
p1.width(10)

# setting p2's turtle and it's default start position
p2 = p1.clone()
p2.penup()
p2.speed(10)
p2.pencolor("blue")
p2.goto(-200, -100)
p2.shapesize(2,2,2)
p2.width(10)

# setting finish line for p1
p1.goto(300, 70)
p1.pendown()

p1.begin_fill()
for i in range(2):
    p1.forward(25)
    p1.left(90)
    p1.forward(60)
    p1.left(90)
p1.end_fill()


# setting finish line for p2
p2.goto(300, -130)
p2.pendown()

p2.begin_fill()
for i in range(2):
    p2.forward(25)
    p2.left(90)
    p2.forward(60)
    p2.left(90)
p2.end_fill()

# go base position
p1.penup()
p1.goto(-200, 100)

p2.penup()
p2.goto(-200, -100)

# setting last speed
p1.speed(1)
p2.speed(1)


# which player is gonna start?
# heads or tails
side = input("\n\nheads or tails, decide\n\nIf your choice wins you become \"Player One\"\n\nAfter you decide, press ENTER.\n\n")
side_list = ["heads","tails"]
result = random.choice(side_list)
print(f"{result} wins!\n\n")

wn.tracer(1)
# setting gameplay
while True:
    wn.update()
    
    # heads label
    
    # setting p1's move
    p1_turn = input("Player One, press 'Enter' to roll the dice\n")
    dice_outcome = random.randrange(1, 7)
    print("The result of dice roll is:\n", dice_outcome)
    time.sleep(0.8)
    print("The number of steps will be:\n", 30 * dice_outcome)
    time.sleep(0.8)
    print("-------------------------------------")
    time.sleep(1.3)
    p1.forward(30 * dice_outcome)

    
    
    # tails label
    
    # setting p2's move
    p2_turn = input("Player Two, press 'Enter' to roll the dice\n")
    dice_outcome = random.randrange(1, 7)
    print("The result of dice roll is:\n", dice_outcome)
    time.sleep(0.8)
    print("The number of steps will be:\n", 30 * dice_outcome)
    time.sleep(0.8)
    print("-------------------------------------")
    time.sleep(1.3)
    p2.forward(30 * dice_outcome)

    # setting condition for finish
    
    if p1.xcor() >= 300 and p2.xcor() >= 300:
        print("NO WINNER")
        break
    
    elif p1.xcor() >= 300:
        print("Player One Wins!\nEZ")
        break
    
    elif p2.xcor() >= 300:
        print("Player Two Wins!\nEZ")
        break
    
# EXIT

print("GOODBYE")
time.sleep(3)
wn.bye()