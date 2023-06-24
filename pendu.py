# Énoncé du jeu du pendu

# Objectif :
# Créer un jeu du pendu en utilisant des listes et des dictionnaires en Python.

# Description :
# Le jeu du pendu est un jeu où le joueur doit deviner un mot en proposant des lettres une par une. Pour chaque lettre proposée, le programme vérifie si la lettre est présente dans le mot à deviner et met à jour l'affichage en conséquence. Le joueur a un nombre limité de chances pour deviner le mot complet.

# Instructions :
# 1. Le programme doit choisir un mot aléatoire parmi une liste prédéfinie de mots.
# 2. Le mot à deviner doit être affiché sous forme de tirets représentant les lettres manquantes.
# 3. Le joueur doit pouvoir entrer une lettre à deviner.
# 4. Si la lettre est présente dans le mot à deviner, elle doit être affichée à sa place dans le mot.
# 5. Si la lettre est incorrecte, le joueur perd une chance.
# 6. Le joueur a un nombre limité de chances pour deviner le mot complet.
# 7. Si le joueur devine correctement toutes les lettres du mot, il gagne la partie.
# 8. Si le joueur n'a plus de chances, il perd la partie.

# Consignes supplémentaires :
# 1. Utilisez des listes pour stocker les lettres déjà trouvées et pour afficher le mot partiellement deviné.
# 2. Utilisez un dictionnaire pour ajouter des fonctionnalités supplémentaires, comme le suivi des scores des joueurs ou l'ajout de catégories de mots.

# Remarques :
# - Assurez-vous d'ajouter des commentaires pour expliquer votre code et faciliter la compréhension.
# - Vous pouvez personnaliser le jeu et ajouter vos propres fonctionnalités pour améliorer l'expérience de jeu.
# - N'hésitez pas à tester votre jeu avec différents mots et à le partager avec vos camarades pour jouer ensemble !

# Bonne chance !

import random

all_my_word = ["coucou", "ianareo", "rehetra"]

my_random_number = random.randint(1, len(all_my_word))

unknown_word = all_my_word[my_random_number-1]

uw_list = list(unknown_word)

uw_found = []

new_word_affichage = []

for tir in uw_list:
    new_word_affichage.append('-')

point_de_vie = 10

print(unknown_word)

while(True):
    if("".join(new_word_affichage).find("-")==-1):
        print("felicitation, vous avez gagnez")
        break
    print("le mot a trouver est : " + "".join(new_word_affichage))
    print("Entrer une lettre pour deviner le mot : " , end=" ")
    lettre_trouver = input()
    if(unknown_word.find(lettre_trouver)!=-1):
        print("Bienjouer, vous avez trouvez une lettre")
        uw_found.append(lettre_trouver)
        i = 0
        print(uw_found)
        for i_w in uw_list:
            for j_w in uw_found:
                if(i_w==j_w): 
                    new_word_affichage[i] = j_w
                    pass
            i = i+1
        print("".join(new_word_affichage)) 
    else:
        point_de_vie = point_de_vie - 1
        if(point_de_vie==0):
            print("vous avez perdu")
            break

    