from random import randint

number = randint(1, 10)
while True:
    #number = randint(1, 10)
    guess = int(input('Guess what number I thought of: '))
    #print(number)
    if guess < number:
        print('A little higher.')
    elif guess > number:
        print('A little lower')
    if guess == number:
        print('Well done. You got it!')
        break
    else:
        print('Try again!')
