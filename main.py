print("hello world")
print("keshav")
print("Danny")
'''
program 1 :
To create a Guess Number game
'''
import random
def Game() :
    lower_bound = 0
    higher_bound = 50
    Target = random.randint(lower_bound,higher_bound)
    attempts = 0
    
    print("Number Guessing Game")
   
    while True :
        Number = input("Enter a number between 1 and 50 : ")
        if Number.isdigit():
            Number = int(Number)
            attempts = attempts + 1
            if (Number < lower_bound or Number > higher_bound):
                print("Please enter number between 0 and 50")
            else :
                if (Number < Target):
                    print("Too low. Try again")
                elif (Number > Target):
                    print("Too high. Try again")
                else:
                    print(f"You won. The Target was {Target}")
                    print(f"You took {attempts} attempts to win the game")
                    break

while True :
    Game()
    x = input("Do you want to play again (y for yes and n for no)")
    if (x != 'y') :
       print("Bye")
       break
   
        

            








