import random

def guess(x=100):
    random_number=random.randint(1,x)
    guess=0
    guess_count=5
    while guess_count!=0 :

        guess = int(input(f"guess a number between 1 and {x}   :   "))
        if guess == random_number:
            print("CONGRATS.YOU WON THE GAME")
            break
        elif guess < random_number:
            print("sorry..Your answer is too low..Guess again")
        elif guess > random_number:
            print("sorry..Your answer is too high..Guess again")
        guess_count -=1
        print(f"you have only {guess_count} more gueeses left")
        if  guess_count==0:
            print("sorry,no more chances left")
            print("you lost")



guess()