from univers import personnage
from utils.input_utils import demander_texte, demander_nombre, demander_choix, load_fichier


def introduction():
    print("\n" + "=" * 50)
    print("✨ CHAPITRE 1 : L'ARRIVÉE DANS LE MONDE MAGIQUE ✨")
    print("=" * 50)
    print("Bienvenue, jeune sorcier(e). Ton destin est sur le point de changer...")

    input("Appuie sur Entrée pour commencer...")


def creer_personnage():

    print("\n--- CRÉATION DU PERSONNAGE ---")

    nom = demander_texte("Entrez le nom de votre personnage : ")
    prenom = demander_texte("Entrez le prénom de votre personnage : ")

    print("\nChoisissez vos attributs :")
    courage = demander_nombre("Niveau de courage (1-10) : ", 1, 10)
    intelligence = demander_nombre("Niveau d'intelligence (1-10) : ", 1, 10)
    loyaute = demander_nombre("Niveau de loyauté (1-10) : ", 1, 10)
    ambition = demander_nombre("Niveau d'ambition (1-10) : ", 1, 10)

    attributs = {
        "courage": courage,
        "intelligence": intelligence,
        "loyauté": loyaute,
        "ambition": ambition
    }

    joueur = personnage.initialiser_personnage(nom, prenom, attributs)

    personnage.afficher_personnage(joueur)


    return joueur


def recevoir_lettre():

    print("Une chouette traverse la fenêtre et vous apporte une lettre scellée")
    print("du sceau de Poudlard...")
    print("« Cher élève,")
    print("Nous avons le plaisir de vous informer que vous avez été admis à")
    print("l’école de sorcellerie de Poudlard ! »")

    options = [
        "Oui, bien sûr !",
        "Non, je préfère rester avec l’oncle Vernon..."
    ]


    choix = demander_choix("Souhaitez-vous accepter cette invitation et partir pour Poudlard ?", options)

    if choix == options[1]:

        print("Vous déchirez la lettre, l’oncle Vernon pousse un cri de joie:")
        print("« EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! »")
        print("Le monde magique ne saura jamais que vous existiez... Fin du jeu.")
        exit()
    else:

        print("Vous préparez vos valises avec enthousiasme !")


def rencontrer_hagrid(joueur):

    prenom = joueur["Prenom"]

    print("\nHagrid : 'Salut {} ! Je suis venu t’aider à faire tes achats sur".format(prenom))
    print("le Chemin de Traverse.'")

    options = ["Oui", "Non"]

    choix = demander_choix("Voulez-vous suivre Hagrid ?", options)

    if choix == "Non":
        print("Hagrid insiste gentiment et vous entraîne quand même avec lui!")


#
def acheter_fournitures(joueur):
    """
    Gère les achats obligatoires et l'animal de compagnie.
    Gère le Game Over si plus d'argent.
    """
    print("\nBienvenue sur le Chemin de Traverse !")


    catalogue = load_fichier("data/inventaire.json")

    print("Catalogue des objets disponibles :")
    for i in range(1, len(catalogue) + 1):
        key = str(i)
        if key in catalogue:
            nom = catalogue[key][0]
            prix = catalogue[key][1]
            print("{}. {} - {} galions".format(key, nom, prix))

    obligatoires = ["Baguette magique", "Robe de sorcier", "Manuel de potions"]
    achats_faits = []


    while len(achats_faits) < 3:
        manquants = []
        for obj in obligatoires:
            if obj not in achats_faits:
                manquants.append(obj)

        print("\nVous avez {} galions.".format(joueur["Argent"]))
        print("Objets obligatoires restant à acheter : " + ", ".join(manquants))

        choix_num = demander_nombre("Entrez le numéro de l'objet à acheter : ", 1, len(catalogue))
        key = str(choix_num)

        objet_data = catalogue[key]
        nom_objet = objet_data[0]
        prix_objet = objet_data[1]

        if joueur["Argent"] < prix_objet:
            print("Vous n'avez pas assez d'argent pour acheter {} !".format(nom_objet))
            print("Vous ne pouvez pas entrer à Poudlard sans fournitures...")
            print("GAME OVER.")
            exit()

        elif nom_objet in achats_faits:
            print("Vous avez déjà acheté cet objet.")

        else:
            personnage.modifier_argent(joueur, -prix_objet)
            personnage.ajouter_objet(joueur, "Inventaire", nom_objet)

            if nom_objet in obligatoires:
                achats_faits.append(nom_objet)

            print("Vous avez acheté : {} (-{} galions).".format(nom_objet, prix_objet))

    print("Tous les objets obligatoires ont été achetés !")

    print("\nIl est temps de choisir votre animal de compagnie pour Poudlard !")
    print("Vous avez {} galions.".format(joueur["Argent"]))

    animaux_data = [
        ("Chouette", 20),
        ("Chat", 15),
        ("Rat", 10),
        ("Crapaud", 5)
    ]

    print("Voici les animaux disponibles :")
    for i in range(len(animaux_data)):
        nom_ani = animaux_data[i][0]
        prix_ani = animaux_data[i][1]
        print("{}. {} - {} galions".format(i + 1, nom_ani, prix_ani))

    choix_ani = demander_nombre("Quel animal voulez-vous ?", 1, 4)

    animal_choisi = animaux_data[choix_ani - 1]
    nom_animal = animal_choisi[0]
    prix_animal = animal_choisi[1]

    if joueur["Argent"] < prix_animal:
        print("Vous n'avez pas assez d'argent pour cet animal !")
        print("C'est triste, mais vous partez sans compagnon... (ou Game Over selon interprétation)")
        print("GAME OVER.")
        exit()
    else:
        personnage.modifier_argent(joueur, -prix_animal)
        personnage.ajouter_objet(joueur, "Inventaire", nom_animal)
        print("Vous avez choisi : {} (-{} galions).".format(nom_animal, prix_animal))

    print("\nTous les objets obligatoires ont été achetés avec succès ! Voici votre")
    print("inventaire final :")
    personnage.afficher_personnage(joueur)


def lancer_chapitre_1():

    introduction()

    joueur = creer_personnage()

    recevoir_lettre()

    rencontrer_hagrid(joueur)

    acheter_fournitures(joueur)

    print("Fin du Chapitre 1 ! Votre aventure commence à Poudlard...")

    return joueur