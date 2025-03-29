import time
def compte_a_rebours(secondes):
    while secondes > 0:
        print(f"Temps restant : {secondes} secondes")
        time.sleep(1)
        secondes -= 1
    print('Temps écoulé !')

compte_a_rebours(5)