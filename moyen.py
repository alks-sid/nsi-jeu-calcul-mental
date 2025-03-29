import random
import time

score = 0
start_time = time.time()

# Questions
for i in range(5):
    nombre_1 = random.randint(0, 15)
    nombre_2 = random.randint(0, 15)
    produit = nombre_1 * nombre_2
    reponse = int(input('Quelle est le résultat de ce produit ? '))
    if reponse == ValueError:
        print('Mauvaise réponse', '\N{cross mark}')
        print(f'La réponse était : {produit}')
    if produit == reponse:
        print('Bonne réponse', '✅')
        score += 1
    else:
        print('Mauvaise réponse', '\N{cross mark}')
        print('La réponse était :', produit)
end_time = time.time()

# Affichage du score
print('Votre score est de :', score, '/ 5')
if score > 2:
    print('Ouai pas mal pas mal', '\N{fire}')
else:
    print('Bien guez', '\N{fire}')

#Affichage du temps mis par le joueur
total_time = end_time - start_time
print(f'Temps total écoulé : {total_time:.2f} secondes')