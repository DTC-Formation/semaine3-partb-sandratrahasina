# Exercice 6: Gestion des contacts

# Description :
# Vous devez créer un programme qui permet de gérer une liste de contacts. Chaque contact sera représenté par un dictionnaire contenant les informations suivantes : nom, prénom et numéro de téléphone.

# Instructions :
# 1. Créez une liste vide appelée "contacts" pour stocker les contacts.
# 2. Demandez à l'utilisateur s'il souhaite ajouter un contact ou afficher la liste des contacts.
# 3. Si l'utilisateur choisit d'ajouter un contact, demandez-lui de saisir le nom, le prénom et le numéro de téléphone du contact.
# 4. Créez un dictionnaire contenant les informations du contact saisi.
# 5. Ajoutez le dictionnaire à la liste "contacts".
# 6. Si l'utilisateur choisit d'afficher la liste des contacts, parcourez la liste "contacts" et affichez les informations de chaque contact (nom, prénom et numéro de téléphone).

# Exemple d'interaction avec le programme :
# 1. Voulez-vous ajouter un contact ou afficher la liste des contacts ? (ajouter/afficher) : ajouter
#    Entrez le nom : Dupont
#    Entrez le prénom : Jean
#    Entrez le numéro de téléphone : 123456789
#    Le contact a été ajouté avec succès !

# 2. Voulez-vous ajouter un contact ou afficher la liste des contacts ? (ajouter/afficher) : afficher
#    Contacts :
#    Nom : Dupont, Prénom : Jean, Téléphone : 123456789

# 3. Voulez-vous ajouter un contact ou afficher la liste des contacts ? (ajouter/afficher) : ajouter
#    Entrez le nom : Martin
#    Entrez le prénom : Alice
#    Entrez le numéro de téléphone : 987654321
#    Le contact a été ajouté avec succès !

# 4. Voulez-vous ajouter un contact ou afficher la liste des contacts ? (ajouter/afficher) : afficher
#    Contacts :
#    Nom : Dupont, Prénom : Jean, Téléphone : 123456789
#    Nom : Martin, Prénom : Alice, Téléphone : 987654321

# Consignes supplémentaires :
# - Assurez-vous de gérer les entrées de l'utilisateur et de traiter les cas d'erreur.
# - Vous pouvez ajouter des fonctionnalités supplémentaires, comme la possibilité de rechercher un contact par nom ou de supprimer un contact de la liste.
# - Ajoutez des commentaires pour expliquer votre code et faciliter la compréhension.
# - Testez votre programme avec différentes entrées pour vous assurer qu'il fonctionne correctement.

# Bonne chance !




contacts = []

while(True):
    print("Voulez-vous ajouter un contact ou afficher la liste des contacts ? (ajouter/afficher) :", end=" ")
    choix_1 = input()

    if(choix_1=="ajouter"):
        print("Entrez le nom :", end=" ")
        nom = input()
        print("Entrez le prénom :", end=" ")
        prenom = input()
        print("Entrez le numéro de téléphone :", end=" ")
        tel = input()

        contacts.append({"nom": nom, "prenom": prenom, "tel": tel})

        print("Le contact a été ajouté avec succès !")

    elif(choix_1=="afficher"):
        for contact in contacts:
            print("nom : " + contact["nom"] + ", prenom : " + contact["prenom"] + " , numéro de telephone : " + contact["tel"])
    else:
        print("error")