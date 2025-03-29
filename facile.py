import random
import time

score = 0
pseudo = input('Entrez votre pseudo : ')
start_time = time.time()

# Questions
nb_questions = 5
for _ in range(nb_questions):
    nombre_1 = random.randint(0, 100)
    nombre_2 = random.randint(0, 100)
    somme = nombre_1 + nombre_2
    reponse = int(input(f'Quelle est le résultat de : {nombre_1} + {nombre_2} ? '))
    if reponse == ValueError:
        print('Mauvaise réponse', '\N{cross mark}')
        print(f'La réponse était : {somme}')
    elif somme == reponse:
        print('Bonne réponse', '✅')
        score += 1
    else:
        print('Mauvaise réponse', '\N{cross mark}')
        print(f'La réponse était : {somme}')
end_time = time.time()

# Affichage du score
print(f'Votre score est de : {score}/5')
if score > 2:
    print('Ouai pas mal pas mal', '\N{fire}')
else:
    print('Bien guez', '\N{fire}')

total_time = end_time - start_time
total_time_sec = f'{total_time:.2f}'
print(f'Temps total écoulé : {total_time_sec} secondes')


# fichier qui contient les scores : chaque ligne est composée du temps et du pseudo séparé par une espace
fichier = 'Classement.txt'
separateur = ' ; '
# on lit le fichier pour mettre le contenu dans la variable 'lignes' de type liste
f = open(fichier, 'r')
rang = f.readlines()
f.close()

# Pour trier plus facilement, on transforme la liste 'lignes' en liste de tuples, chaque tuple est composé de :
#  - nb fautes
#  - temps de réponse en secondes
#  - score
#  - pseudo
# Ainsi, le tri se fait en premier sur le nb de fautes, puis sur le temps.
# On stocke le score pour l'afficher le classement.
# On transorme le temps en float pour trier dessus et on supprime le retour charriot \n
joueurs = []
for joueur in rang:
    j = joueur.split(separateur)
    joueurs.append((int(j[0]), float(j[1]), int(j[2]), j[3].strip()))
# on ajoute un nouveau tuple (nb_fautes, temps, score, pseudo) à la liste de tuples 'joueurs'
joueurs.append((nb_questions - int(score), float(total_time_sec), int(score), f'{pseudo}'))
# on trie la liste de tuples avant de l'afficher et de sauvegarder dans le fichier de scores
joueurs.sort()
for joueur in joueurs:
    print('{} {} {} {}'.format(str(joueur[0]), joueur[1], str(joueur[2]), joueur[3]))

# on sauvegarde les scores dans le fichier
f = open(fichier, 'w')
for joueur in joueurs:
    f.write('{}{}{}{}{}{}{}\n'.format(str(joueur[0]), separateur, joueur[1], separateur, str(joueur[2]), separateur, joueur[3]))
f.close()

# Affichage des scores
if len(joueurs) < 3:
    borne_top = len(joueurs)
else:
    borne_top = 3
print('Top {} :'.format(borne_top))
print('Score | Temps | Pseudo')
for i in range(borne_top):
    print('{} | {} | {}'.format(str(joueurs[i][2]), joueurs[i][1], joueurs[i][3]))
