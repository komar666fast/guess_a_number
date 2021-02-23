# Guess a number
import random

lot = random.randint(1, 10)
answer = input('Choose your number from 1 to 10:')

while True:
    if int(answer) == lot:
        print('Bravo!!! You won!!')
        break
    elif int(answer) < lot:
        print('The number u are looking for is bigger')
        answer = input('Choose your number from 1 to 10:')
    else:
        print('The number u are looking for is smaller')
        answer = input('Choose your number from 1 to 10:')
    