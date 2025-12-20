# ================================
# Gain de points pour sa maison
# ================================

def actualiser_points_maison(maisons, nom_maison, points):
    if nom_maison in maisons:
        maisons[nom_maison] = maisons[nom_maison] + points
        print(f"{nom_maison} gagne {points} points. Total : {maisons[nom_maison]} points.")
    else:
        print("Maison introuvable.")


# ================================
# Affichage de la maison gagnante
# ================================


def afficher_maison_gagnante(maisons):
    # 1. Initialiser score_max avec la première maison
    for maison in maisons:
        score_max = maisons[maison]
        break

    # 2. Trouver le score maximum
    for maison in maisons:
        if maisons[maison] > score_max:
            score_max = maisons[maison]

    # 3. Trouver les maisons gagnantes
    gagnantes = []
    for maison in maisons:
        if maisons[maison] == score_max:
            gagnantes.append(maison)

    # 4. Affichage
    if gagnantes[1:] == []:
        print("La maison gagnante est", gagnantes[0], "avec", score_max, "points.")
    else:
        print("Maisons à égalité :")
        for maison in gagnantes:
            print("-", maison, "(", score_max, "points )")


# ================================
# Répartition d'un joueur dans les maisons quiz
# ================================



def repartition_maison(joueur, questions):
    # 1. Initialiser les scores
    scores = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }

    # 2. Points venant des attributs (*2)
    attributs = joueur["Attributs"]
    scores["Gryffondor"] += attributs["courage"] * 2
    scores["Serpentard"] += attributs["ambition"] * 2
    scores["Poufsouffle"] += attributs["loyauté"] * 2
    scores["Serdaigle"] += attributs["intelligence"] * 2

    # 3. Quiz (chaque bonne réponse donne +3 à une maison)
    for question, options, maisons_associees in questions:
        print(question)
        choix = 1
        for option in options:
            print(str(choix) + ". " + option)
            choix += 1

        reponse = demander_choix("Ton choix :", options)
        maison = maisons_associees[options.index(reponse)]
        scores[maison] += 3

    # 4. Trouver la maison gagnante
    for maison in scores:
        maison_gagnante = maison
        break

    for maison in scores:
        if scores[maison] > scores[maison_gagnante]:
            maison_gagnante = maison

    # 5. Affichage récapitulatif
    print("Résumé des scores :")
    for maison in scores:
        print(maison + " :", scores[maison], "points")

    return maison_gagnante