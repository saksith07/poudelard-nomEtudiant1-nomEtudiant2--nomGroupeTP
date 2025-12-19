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