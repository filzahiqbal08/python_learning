import random
secret_num = random.randint(1,20)
print('I am thinking of a number between 1 and 20')

for guesses_taken in range(1,6):
    print('Take a guess.')
    guess = int(input('>'))

    if guess < secret_num:
        print('Number is too low')
    elif guess > secret_num:
        print('Number is too high')
    else:
        break
    if guess == secret_num:
        print('Good job! You got it in', guesses_taken, 'tries!')
    else:
        print('No, the number was', secret_num)