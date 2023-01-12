import random 
def guessing_game():
    answer=random.randint(0,100)
    while True:
        user_guess=int(input('Guess number between 0 and 100 '))
        
        if(user_guess==answer):
            print(f'Right! The answer is {user_guess}')
            break
        if user_guess<answer:
            print(f'Your guess of {user_guess} is too low!\n')
        else:
            print(f'Your guess of {user_guess} is too high!\n')
guessing_game()  
