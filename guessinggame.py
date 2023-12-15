import random 
num = random.randrange(1,100)
i = 5
while i > 0:
    num_guess = int(input('Guess the number : '))
    i = i - 1
    if i == 0:
        print('You have ran out of choices')
    elif num_guess > num:
        print(f'Too high, choices remain {i}')
    elif num_guess < num:
        print(f'Too less, choices remain {i}')
    else:
        print('Congratulations, you have guessed the number correctly')
