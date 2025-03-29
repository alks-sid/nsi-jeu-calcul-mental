start = input('Quel niveau veux tu choisir entre : Facile, Moyen, Difficile et Extrème ? ').lower()
if start == 'facile':
    regle_facile = input('Le niveau facile consiste à faire la somme de deux nombres pris au hasard entre 0 et 100, es-tu sure de vouloir y jouer ? ').lower()
    if regle_facile == 'oui':
        import facile
    else:
        import principal    
elif start == 'moyen':
    regle_moyen = input('Le niveau moyen consiste à résoudre une nultiplication de deux nombres pris entre 0 et 15, es-tu sure de vouloir y jouer ? ').lower()
    if regle_moyen == 'oui':
        import moyen
    else:
        import principal
elif start == 'difficile':
    regle_difficile = input('Le niveau difficile consiste à résoudre une opération de nombres pris au hasard entre 0 et 15, es-tu sure de vouloir y jouer ? ').lower()
    if regle_difficile == 'oui':
        import difficile
    else:
        import principal
elif start == 'extreme':
    regle_extreme = input("Le niveau extrème consiste à trouver le carré d'un nombre pris au hasard entre 0 et 100, es-tu sure de vouloir y jouer ? ").lower()
    if regle_extreme == 'oui':
        import extreme
    else:
        import principal
else:
    import principal
