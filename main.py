# Importation de la librairie random
import random


# Fonction number_guessing qui prend en paramètre i et y qui sont des entiers
def number_guessing(i=random.randint(0, 100), y=0):
    # Demande à l'utilisateur de rentrer un nombre entre 0 et 100
    x = int(input("Essayez de trouver le nombre (entre 0 et 100) : "))
    # Tant que x est différent de i
    while i != x:
        # Affiche si le nombre est plus petit ou plus grand que i et incrémente y
        print("Le nombre est plus petit") if x > i else print("Le nombre est plus grand")
        y += 1
        # Demande à l'utilisateur de rentrer un autre nombre
        x = int(input("Essayez à nouveau : "))

    # Retourne un message de félicitation
    return f"Bien joué tu as trouver le nombre {i} en {y} essai(s)"


# Affiche le résultat de la fonction number_guessing
print(number_guessing())
