import random
import affichage

def verifie_mot(mot) :
    return False if('-' in list(mot)) else True

mots_aleatoire = ["pomme", "poire", "banane", "fraise", "framboise", "cerise", "abricot", "peche", "pasteque", "melon", "citron", "orange", "mandarine", "raisin", "mangue", "ananas", "pamplemousse", "grenade", "clementine", "kiwi", "prune", "mirabelle", "groseille", "cassis", "myrtille", "mure"]

nombre_participants = int(input(" Bienvenue dans ce jeu. \n Veuillez entrer le nombre de joueurs s'il vous plait : "))
list_participant = []
while nombre_participants > 0:
    print("\n Participant n° "+str(len(list_participant) + 1))
    nom_participant = input("\n Entrer votre nom : ")
    mot_à_deviner = random.choice(mots_aleatoire)
    nombre_tentative = 10
    labels = []
    while True :
        if(verifie_mot(affichage.affichage_mot_a_trouver(mot_à_deviner, labels))):
            list_participant.append({"nom":nom_participant, "tentative_restant": nombre_tentative})
            print("Felicitation, vous avez reussi")
            break
        input_label = input(" Entrer une lettre pour deviner le mot "+affichage.affichage_mot_a_trouver(mot_à_deviner, labels)+" : ")
        if(input_label in list(mot_à_deviner)):
            labels.append(input_label)
            print("Felicitation, c'etait une bonne reponse.")
            pass
        else:
            nombre_tentative -= 1
            if(nombre_tentative > 0) :
                print("retentez votre chance, vous avez encore " + str(nombre_tentative) + " tentatives")
            else :
                list_participant.append({"nom":nom_participant, "tentative_restant": 0})
                print("Vous avez perdu")
                break
    nombre_participants -= 1
