import json



def demander_texte(message):
    saisie_utilisateur = input(message)

    while saisie_utilisateur.strip()== "":
        saisie_utilisateur= input(message)

    return saisie_utilisateur.strip()



def demander_nombre(message,min_val = -10000 ,max_val = 10000):

    nombre_valide = False

    while nombre_valide == False :
        saisie_nombre = demander_texte(message)
        nombre_negatif = False
        uniquement_nombre = True

        if saisie_nombre[0] == "-":
            nombre_negatif = True
            if len(saisie_nombre) == 1 :
                uniquement_nombre = False

        if nombre_negatif == True :
            for i in range(1,len(saisie_nombre)):
                if (ord(saisie_nombre[i]) < 48 or ord(saisie_nombre[i]) > 57) :
                    uniquement_nombre = False


            if uniquement_nombre == True:
                nombre = 0
                chiffre = 0
                for i in range(1,len(saisie_nombre)):
                    chiffre = ord(saisie_nombre[i]) - ord('0')
                    nombre = nombre * 10 + chiffre
                nombre = nombre * -1

                if nombre >= min_val and nombre <= max_val:
                    nombre_valide = True
                else :
                    print("Veuillez entrer un nombre entre {} et {}.".format(min_val, max_val))

        else :
            for i in range(len(saisie_nombre)):
                if (ord(saisie_nombre[i]) < 48 or ord(saisie_nombre[i]) > 57):
                    uniquement_nombre = False

            if uniquement_nombre == True:
                nombre = 0
                chiffre = 0
                for i in range(len(saisie_nombre)):
                    chiffre = ord(saisie_nombre[i]) - ord('0')
                    nombre = nombre * 10 + chiffre

                if nombre >= min_val and nombre <= max_val:
                    nombre_valide = True
                else :
                    print("Veuillez entrer un nombre entre {} et {}.".format(min_val, max_val))

        if uniquement_nombre == False:
            print("Veuillez entrer un nombre entre {} et {}.".format(min_val, max_val))

    return nombre


def demander_choix(message, liste_choix):  # N'oublie pas les deux points

    print(message)

    for i in range(len(liste_choix)):
        print("{}. {}".format(i + 1, liste_choix[i]))

    choix_numero = demander_nombre("Votre choix : ", 1, len(liste_choix))


    return liste_choix[choix_numero - 1]



def load_fichier(chemin_fichier):
    with open(chemin_fichier, 'r', encoding='utf-8') as f :
        donnees = json.load(f)

    return donnees






