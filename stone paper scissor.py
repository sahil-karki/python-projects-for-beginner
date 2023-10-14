
import random

a = ['stone','paper','scissor']

computer = random.choice(a)   #Returns a random item from a list, tuple, or string

user = input("enter your move = ")

if user == computer:
    print("computer play same move")
    print("its a DRAW")
    
elif user == "stone":
    if computer == "paper":
        print("computer played PAPER")
        print("YOU LOST")
    elif computer == "scissor":
        print("computer played SCISSOR")
        print("YOU WIN")
        
elif user == "paper":    
    if computer == "stone":
        print("computer played STONE")
        print("YOU WIN")
    elif computer == "scissor":
        print("computer played SCISSOR")
        print("YOU LOST")
        
elif user == "scissor":
    if computer == "stone":
        print("computer played STONE")
        print("YOU LOST")
    elif computer == "paper":
        print("computer played SCISSOR")
        print("YOU WIN")
        
    






