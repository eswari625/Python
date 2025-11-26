'''
Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water or a gun. 
The gun beats the snake, the water beats the gun and the snake beats the water. Write a python program to create a Snake water gun game in python using if-else statements.
Do not create any fancy GUI. Use proper functions to check for win.

'''
import random
def pick_random():
    n=random.randint(0,2)
    return n
print("Hello!! Welcome to Snake Water Gun game. We have 10 rounds of this game. Let's play!!!")

cand=0
comp=0
for x in range(0,10):
    
    print("Enter a value")
    print("0: Snake 1: Water 2: Gun")
    i =int(input())
    y=pick_random()
    print(f"I chose {y}")
    if i==y:
        print("It's a Draw")
    elif (i==0 and y==1) or (i==1 and y==2) or (i==2 and y==0):
        print("You got a point :)")
        cand +=1
    elif (i==0 and y==2) or (i==1 and y==0) or (i==2 and y==1):
        print("You lost :(")
        comp += 1
        
    else:
        print("Please enter a valid number 0 or 1 or 2")
if cand > comp:
    print(f"You won this game. Your score is {cand}")
elif cand == comp:
    print(f"It's a draw!!My score is {comp} and your score is {cand}")
else:
    print(f"I won this game. My score is {comp} and your score is {cand}")
