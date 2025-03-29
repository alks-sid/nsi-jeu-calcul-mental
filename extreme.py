import random
import time

score = 0
start_time = time.time()
exposant = '²'

# Questions
for _ in range(5):
    nombre = random.randint(0, 50)
    carre = nombre ** 2
    print(str(nombre) + exposant)
    reponse = int(input('Quelle est le résultat de ce carré ? '))
    if reponse == ValueError:
        print('Mauvaise réponse', '\N{cross mark}')
        print(f'La réponse était : {carre}')
    if carre == reponse:
        print('Bonne réponse', '✅')
        score += 1
    else:
        print('Mauvaise réponse', '\N{cross mark}')
        print('La réponse était :', carre)
end_time = time.time()

#Affichage du scrore
print('Votre score est de :', score, '/ 5')
if score > 2:
    print('Ouai pas mal pas mal', '\N{fire}')
else:
    print('Bien guez', '\N{fire}')

total_time = end_time - start_time
print(f'Temps total écoulé : {total_time:.2f} secondes')

# Niveau de l'utilisateur en fonction de son temps
if total_time < 45:
    print('Incroyable !')
elif total_time < 90:
    print('Très fort !')
elif total_time < 125:
    print('Ca passe')
elif total_time < 170:
    print('Bof')
else:
    print("T'es nul")