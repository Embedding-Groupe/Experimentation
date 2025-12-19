def calculatrice():
    menu = True

    while menu == True:

        print("Calculatrice Cassio")
        nombre1 = input(f"Premier nombre ?\n")
        operateur = input(f"L'opération (+, -, *, /) ? \n")
        nombre2 = input(f"Deuxième nombre ?\n")

        resultat = 0

        message_resultat = f"le resultat de {nombre1} {operateur} {nombre2} est {resultat}\n"

        match operateur:
            case "+":
                resultat = int(nombre1) + int(nombre2)
                print (message_resultat)

            case "-":
                resultat = int(nombre1) - int(nombre2)
                print (message_resultat)

            case "*":
                resultat = int(nombre1) * int(nombre2)
                print (message_resultat)

            case "/":
                resultat = int(nombre1) / int(nombre2)
                print (message_resultat)

            case _:
                print("Erreur dans la saisie\n")

        continuer = input("voulez-vous continuez ? (Y/n)\n")

        erreurSortie = 1

        while erreurSortie == 1:
            if continuer == "" or continuer == "Y" or continuer =="y":
                menu = True
                erreurSortie = 0
            
            elif continuer == "n" or continuer == "N":
                menu = False
                erreurSortie = 0

            else:
                print("Erreur dans la saisie \n", end="", flush=True)
                erreurSortie = 1

if __name__ == "__main__":
    calculatrice()