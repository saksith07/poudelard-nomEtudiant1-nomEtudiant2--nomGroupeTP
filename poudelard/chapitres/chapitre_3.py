import random
from utils.input_utils import load_fichier
from univers.personnage import afficher_personnage
from univers.maison import actualiser_points_maison, afficher_maison_gagnante


def apprendre_sorts(joueur, chemin_fichier="../data/sorts.json"):
    print("\nTu commences tes cours de magie à Poudlard...")

    tous_les_sorts = load_fichier(chemin_fichier)

    liste_offensifs = []
    liste_defensifs = []
    liste_utilitaires = []

    for sort in tous_les_sorts:
        if sort["type"] == "Offensif":
            liste_offensifs.append(sort)
        elif sort["type"] == "Défensif":
            liste_defensifs.append(sort)
        elif sort["type"] == "Utilitaire":
            liste_utilitaires.append(sort)


    sort_off = random.choice(liste_offensifs)
    joueur["Sortilèges"].append(sort_off)
    print("Tu viens d'apprendre le sortilège : {} ({})".format(sort_off["nom"], sort_off["type"]))
    input("Appuie sur Entrée pour continuer...")

    sort_def = random.choice(liste_defensifs)
    joueur["Sortilèges"].append(sort_def)
    print("Tu viens d'apprendre le sortilège : {} ({})".format(sort_def["nom"], sort_def["type"]))
    input("Appuie sur Entrée pour continuer...")

    compteur = 0
    while compteur < 3:
        sort_hasard = random.choice(liste_utilitaires)

        if sort_hasard not in joueur["Sortilèges"]:
            joueur["Sortilèges"].append(sort_hasard)
            print("Tu viens d'apprendre le sortilège : {} ({})".format(sort_hasard["nom"], sort_hasard["type"]))
            input("Appuie sur Entrée pour continuer...")

            compteur = compteur + 1

    print("\nTu as terminé ton apprentissage de base à Poudlard !")
    print("Voici les sortilèges que tu maîtrises désormais :")

    for sort in joueur["Sortilèges"]:
        print("- {} ({}) : {}".format(sort["nom"], sort["type"], sort["description"]))


def quiz_magie(joueur, chemin_fichier="../data/quiz_magie.json"):

    print("\n" + "=" * 50)
    print("🎓 BIENVENUE AU QUIZ DE MAGIE DE POUDLARD !")
    print("=" * 50)
    print("Réponds correctement aux 4 questions pour faire gagner des points à")
    print("ta maison.")

    toutes_les_questions = load_fichier(chemin_fichier)

    questions_quiz = []

    while len(questions_quiz) < 4:
        choix = random.choice(toutes_les_questions)

        if choix not in questions_quiz:
            questions_quiz.append(choix)

    score_partie = 0
    numero = 1

    for q in questions_quiz:
        print("\n{}. {}".format(numero, q["question"]))

        reponse_joueur = input("> ")


        if reponse_joueur.strip().lower() == q["reponse"].lower():
            print("Bonne réponse ! +25 points pour ta maison.")
            score_partie = score_partie + 25
        else:
            print("Mauvaise réponse. La bonne réponse était : {}".format(q["reponse"]))

        numero = numero + 1

    print("\nScore obtenu : {} points".format(score_partie))

    if "Score" in joueur:
        joueur["Score"] += score_partie
    else:
        joueur["Score"] = score_partie


def lancer_chapitre_3(joueur, maisons):
    print("\n" + "=" * 50)
    print("🪄 CHAPITRE 3 : LES COURS ET LA DÉCOUVERTE 🪄")
    print("=" * 50)


    apprendre_sorts(joueur, "data/sorts.json")


    score_avant = 0
    if "Score" in joueur:
        score_avant = joueur["Score"]

    quiz_magie(joueur, "data/quiz_magie.json")

    nouveau_score = joueur.get("Score", 0)
    points_gagnes = nouveau_score - score_avant

    if points_gagnes > 0:
        print("\n--- MISE À JOUR DES POINTS DES MAISONS ---")
        actualiser_points_maison(maisons, joueur["Maison"], points_gagnes)

    afficher_maison_gagnante(maisons)

    print("\n--- BILAN DU CHAPITRE 3 ---")
    afficher_personnage(joueur)

    print("\nFin du Chapitre 3 ! Vous maîtrisez les bases de la magie.")
    return joueur