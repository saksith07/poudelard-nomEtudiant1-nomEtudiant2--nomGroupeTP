# ================================
# Création du personnage
# ================================


def initialiser_personnage(nom, prenom, attributs):
    liste_inventaire = []
    liste_sortilege = []
    argent = 100
    joueur = {
        "Nom": nom,
        "Prenom": prenom,
        "Argent": argent,
        "Inventaire": liste_inventaire,
        "Sortilèges": liste_sortilege,
        "Attributs": attributs
    }

    return joueur

# ================================
# Affichage du personnage
# ================================

def afficher_personnage(joueur):
    print("Profil du personnage :")

    for cle in joueur:
        # Cas des attributs (dictionnaire)
        if cle == "Attributs":
            print("Attributs :")
            for attribut in joueur["Attributs"]:
                print("- " + attribut + " : " + str(joueur["Attributs"][attribut]))

        # Cas de l'inventaire (liste)
        elif cle == "Inventaire":
            if joueur["Inventaire"] == []:
                print("Inventaire :")
            else:
                print("Inventaire : " + ", ".join(joueur["Inventaire"]))

        # Cas des sortilèges (liste)
        elif cle == "Sortilèges":
            if joueur["Sortilèges"] == []:
                print("Sortilèges :")
            else:
                print("Sortilèges : " + ", ".join(joueur["Sortilèges"]))

        # Cas simples (Nom, Prenom, Argent, etc.)
        else:
            print(cle + " : " + str(joueur[cle]))

# ================================
# Gestion de l'argent
# ================================

def modifier_argent(joueur, montant):
    joueur["Argent"] = joueur["Argent"] + montant

# ================================
# Ajout d'un objet
# ================================

def ajouter_objet(joueur, cle, objet):
    joueur[cle].append(objet)


















