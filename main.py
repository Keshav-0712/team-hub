#print("hello world")
#print("keshav")
#print("hello")


import random

def play_game() :
    low_num = 1
    high_num = 50
    number = random.randint(low_num, high_num)
    guesses = 0
    print("welcome to python number guessing game")
    print(f"guess the number between ({low_num} and {high_num}) : ")
    while True:
        guess = input("guess a number : ")
        if guess.isdigit():
            guess = int(guess)
            guesses += 1

            if guess < low_num or guess > high_num:
                print("your guess is out of range please try again")
                print(f"guess the number between ({low_num} and {high_num}) : ")

            elif guess < number:
                print(f"your guess is to low try again")
                print(f"guess the number between ({low_num} and {high_num}) : ")
            elif guess > number:
                print("your guess is too high try again")
                print(f"guess the number between ({low_num} and {high_num}) : ")
            else:
                print(f"your guess is correct the answer was {number}  ")
                print(f"number of guesses you took was {guesses}")
                break


        else:
            print("invalid input ")
            print(f"enter a number between ({low_num} and {high_num})")

while True :
    play_game()
    play_again= input("do you want to play again (y/n) : ").lower()
    if play_again != "y":
        print("goodbye ")
        break