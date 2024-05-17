import random


def number_guessing(i=random.randint(0, 100), y=0):
    x = int(input("Essayez de trouver le nombre (entre 0 et 100) : "))
    while i != x:
        print("Le nombre est plus petit") if x > i else print("Le nombre est plus grand")
        y += 1
        x = int(input("Essayez à nouveau : "))

    return f"Bien joué tu as trouver le nombre {i} en {y} essai(s)"


print(number_guessing())