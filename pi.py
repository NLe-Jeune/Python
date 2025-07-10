import random

def pi_estimator(nb_points : int):

    compteur = 0

    for i in range(nb_points):
        x = random.random()
        y = random.random()
    
        if x**2 + y**2 <= 1:
            compteur += 1

    estimation = 4 * compteur / nb_points
    return estimation