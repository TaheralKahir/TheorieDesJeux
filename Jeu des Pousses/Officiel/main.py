import sprout

# L'interface : 
def main():
    on = 1
    print("Bienvenue aux Jeu des Pousses :")
    while on == 1:
        choix_jeu = input("Voulez-vous jouer ?")
        if choix_jeu == 'oui':
            sprout.SproutGameJCJ()
        elif choix_jeu == 'non':
            on = 0
        else:
            print('Erreur de saisie veuillez recommencer...')
    print("Merci d'avoir participer !")
    