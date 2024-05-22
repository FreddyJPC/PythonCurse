import random

def guess_number():
    number = random.randint(1, 100)
    guessed = False

    while not guessed:
        guess = int(input("Adivina el número: "))
        
        if guess < number:
            print("Demasiado bajo")
        elif guess > number:
            print("Demasiado alto")
        else:
            print("¡Felicidades! ¡Adivinaste el número!")
            guessed = True

guess_number()