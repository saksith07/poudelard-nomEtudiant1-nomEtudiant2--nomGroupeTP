from univers import personnage
from utils.input_utils import demander_choix, demander_texte, demander_nombre, load_fichier
from univers.maison import repartition_maison

def rencontrer_amis(joueur):
    """
    Gère les rencontres dans le train (Ron, Hermione, Drago).
    Modifie les attributs (courage, ambition, etc.) selon les choix.
    """
    print("\n" + "=" * 50)
    print("🚂 CHAPITRE 2 : LE VOYAGE VERS POUDLARD")
    print("=" * 50)

    print("Vous montez à bord du Poudlard Express. Le train démarre lentement en")
    print("direction du Nord...")


    print("\nUn garçon roux entre dans votre compartiment, l’air amical.")
    print("— Salut ! Moi c’est Ron Weasley. Tu veux bien qu’on s’assoie ensemble ?")

    opts_ron = [
        "Bien sûr, assieds-toi !",
        "Désolé, je préfère voyager seul."
    ]
    choix_ron = demander_choix("Que répondez-vous ?", opts_ron)

    if choix_ron == opts_ron[0]:

        joueur["Attributs"]["loyauté"] += 1
        print("Ron sourit : — Génial ! Tu verras, Poudlard, c’est incroyable !")
    else:  # Choix 2 : Refuse
        # Ambition +1 (indépendance)
        joueur["Attributs"]["ambition"] += 1
        print("Ron hausse les épaules et va s'asseoir plus loin.")

    print("\nUne fille entre ensuite, portant déjà une pile de livres.")
    print("— Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire")
    print("de la Magie’ ?")

    opts_hermione = [
        "Oui, j’adore apprendre de nouvelles choses !",
        "Euh… non, je préfère les aventures aux bouquins."
    ]
    choix_hermione = demander_choix("Que répondez-vous ?", opts_hermione)

    if choix_hermione == opts_hermione[0]:
        joueur["Attributs"]["intelligence"] += 1
        print("Hermione sourit : — C'est fascinant, n'est-ce pas ?")
    else:

        joueur["Attributs"]["courage"] += 1
        print("Hermione fronce les sourcils : — Il faudrait pourtant s’y mettre un jour !")


    print("\nPuis un garçon blond entre avec un air arrogant.")
    print("— Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le")
    print("départ, tu ne crois pas ?")

    opts_drago = [
        "Je lui serre la main poliment.",
        "Je l’ignore complètement.",
        "Je lui réponds avec arrogance."
    ]
    choix_drago = demander_choix("Comment réagissez-vous ?", opts_drago)

    if choix_drago == opts_drago[0]:

        joueur["Attributs"]["ambition"] += 1
        print("Drago hoche la tête avec satisfaction.")

    elif choix_drago == opts_drago[1]:

        joueur["Attributs"]["loyauté"] += 1
        print("Drago fronce les sourcils, vexé. — Tu le regretteras !")

    else:  # Choix 3 : Arrogance/Conflit
        # Courage +1
        joueur["Attributs"]["courage"] += 1
        print("Drago vous lance un regard noir et s'en va en murmurant.")


    print("\nLe train continue sa route. Le château de Poudlard se profile à")
    print("l’horizon...")
    print("Tes choix semblent déjà en dire long sur ta personnalité !")


    print("Tes attributs mis à jour :", joueur["Attributs"])



def mot_de_bienvenue():
    print("\n" + "=" * 40)
    print("GRANDE SALLE DE POUDLARD")
    print("=" * 40)

    print("Vous entrez dans la Grande Salle.")
    print("Le Professeur Dumbledore se lève pour son discours :")
    print("\n« Bienvenue ! Bienvenue pour une nouvelle année à Poudlard ! »")
    print("« Avant de commencer notre banquet, je voudrais dire quelques mots. »")

    input("Appuyez sur Entrée pour la suite...")



def ceremonie_repartition(joueur):

    print("\nLa cérémonie de répartition commence dans la Grande Salle...")
    print("Le Choixpeau magique t’observe longuement avant de poser ses questions :")


    questions = [
        (
            "Tu vois un ami en danger. Que fais-tu ?",
            ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l’aide", "Je reste calme et j’observe"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Quel trait te décrit le mieux ?",
            ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Face à un défi difficile, tu...",
            ["Fonces sans hésiter", "Cherches la meilleure stratégie", "Comptes sur tes amis", "Analyses le problème"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        )
    ]


    maison_gagnante = repartition_maison(joueur, questions)

    joueur["Maison"] = maison_gagnante

    print("\nLe Choixpeau s’exclame : {} !!!".format(maison_gagnante))
    print("Tu rejoins les élèves de {} sous les acclamations !".format(maison_gagnante))



def installation_salle_commune(joueur):

    print("\nVous suivez les préfets à travers les couloirs du château...")


    donnees_maisons = load_fichier("data/maisons.json")


    nom_maison = joueur["Maison"]


    info_maison = donnees_maisons[nom_maison]


    description = info_maison["description"]


    message = info_maison["message_installation"]


    liste_couleurs = info_maison["couleurs"]
    couleurs_texte = ", ".join(liste_couleurs)


    if "emoji" in info_maison:
        print("{} {}".format(info_maison["emoji"], description))
    else:
        print(description)

    print(message)
    print("Les couleurs de votre maison : {}".format(couleurs_texte))




def lancer_chapitre_2(joueur):

    rencontrer_amis(joueur)

    mot_de_bienvenue()

    ceremonie_repartition(joueur)

    installation_salle_commune(joueur)

    print("\n" + "=" * 40)
    print("BILAN DU CHAPITRE 2")
    print("=" * 40)
    personnage.afficher_personnage(joueur)

    print("\nFin du Chapitre 2 ! Les cours à Poudlard vont bientôt commencer...")

    return joueur