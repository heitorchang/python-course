# Number guessing game

import random

secret = random.randint(1, 9)
print(secret)

while True:
    guess = int(input('enter your guess '))
    if guess == random.randint(1, 9):
        print('congratulations you guessed the number')
        break
