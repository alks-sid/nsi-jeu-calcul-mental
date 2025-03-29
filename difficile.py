import random
import time

score = 0
start_time = time.time()

# Questions
for i in range(5):
    nombre_1 = random.randint(0, 15)
    nombre_2 = random.randint(0, 15)
    nombre_3 = random.randint(0, 15)
    nombre_4 = random.randint(0, 15)
    operation = (nombre_1 + nombre_2) * nombre_3 - nombre_4
    reponse = int(input(f'Quelle est le résultat de : ({nombre_1} + {nombre_2}) x {nombre_3} - {nombre_4} ? '))
    if reponse == ValueError:
        print('Mauvaise réponse', '\N{cross mark}')
        print(f'La réponse était : {operation}')
    if operation == reponse:
        print('Bonne réponse', '✅')
        score += 1
    else:
        print('Mauvaise réponse', '\N{cross mark}')
        print('La réponse était :', operation)
end_time = time.time()

# Affichage du score
print('Votre score est de :', score, '/ 5')
if score > 2:
    print('Ouai pas mal pas mal', '\N{fire}')
else:
    print('Bien guez', '\N{fire}')

total_time = end_time - start_time
print(f'Temps total écoulé : {total_time:.2f} secondes')

# Niveaude l'utilisateur en fonction de son temps
if total_time < 20:
    print('Incroyable !')
elif total_time < 40:
    print('Très fort !')
elif total_time > 60:
    print('Ca passe')
elif total_time < 80:
    print('Bof')
else:
    print("T'es nul")