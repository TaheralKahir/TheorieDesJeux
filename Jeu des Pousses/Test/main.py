# L'interface : 
from jeu_des_pousses import jeu_des_pousses

def main():
    on_off = 1
    print("Bienvenue dans le Jeu des Pousses !")
    print("1: Jouer, 2: Lire les règles du jeu, 3: Quitter")
    while on_off == 1:
        choix1 = int(input("Que voulez-vous faire ?"))
        if choix1 == 1:
            print("Les choix de jeu : 1. Joueur contre Joueur, 2. Joueur contre IA, 3. Éteindre.")
            choix_jeu = int(input("Choississez votre mode de jeu:"))
            if choix_jeu == 1 :
                jeu_des_pousses(1)
            elif choix_jeu == 2:
                print("Les différentes difficultés : 2: Facile, 3: Moyen, 4: Impossible.")
                choix_difficultés = int(input("Choix de difficulté :"))
        elif choix1 == 2:
            print("Le Jeu des Pousses: On choisit un nombre de point.")
            print("Chacun son tour, joindre deux points par une ligne et dessiner un point sur cette ligne ou faire une boucle sur un seul point.")
            print("Les lignes ne se croisent pas. D'un point ne peuvent partir que 3 lignes maximum.")
            print("Le Gagnant est celui qui trace la dernière ligne.")
        elif choix1 == 3:
            on_off = 0
    print("Merci d'avoir joué !")
        
main()     
        