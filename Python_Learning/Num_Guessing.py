from random import *
secret_num = randint(1, 100)
guessed_num = input('Welcome to the Number Guessing game!\n Please guess a number between 1 and 100:\n')
guessed_num=int(guessed_num)

while guessed_num != secret_num
    if guessed_num > secret_num:
        if guessed_num - secret_num > 25:
            guessed_num = input('Very cold; guess again')
            guessed_num=int(guessed_num)
        elif guessed_num - secret_num > 10:
            guessed_num = input('Getting warmer; guess again')
            guessed_num=int(guessed_num)
        elif guessed_num - secret_num > 5:
            guessed_num = input('Hot; guess again')
            guessed_num=int(guessed_num)
    if guessed_num < secret_num:
        if guessed_num - secret_num < 25:
            guessed_num = input('Very cold; guess again')
            guessed_num=int(guessed_num)
        elif guessed_num - secret_num < 10:
            guessed_num = input('Getting warmer; guess again')
            guessed_num=int(guessed_num)
        elif guessed_num - secret_num < 5:
            guessed_num = input('Hot; guess again')
            guessed_num=int(guessed_num)
        
print(type(secret_num))
print(type(guessed_num))