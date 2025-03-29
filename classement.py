# fichier qui contient les scores : chaque ligne est composée du temps et du pseudo séparé par une espace
fichier = "Classement.txt"
separateur = ';'

# on lit le fichier pour mettre le contenu dans la variable 'lignes' de type liste
f = open(fichier, 'r')
lignes = f.readlines()
f.close()

print(lignes)