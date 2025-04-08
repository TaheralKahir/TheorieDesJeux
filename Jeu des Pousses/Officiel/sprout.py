import numpy as np
import mathplotlib.pyplot as plt
import networkx as nx


class État(): # Cette classe va me servir pour afficher modifier puis réafficher !

    def __init__(self):
        self.graph = nx.Graph()
        self.number_of_edge = 0
        self.matrix = None
        self.affichage()
        
    def affichage(self):
        nx.draw(self, with_labels=True)
        plt.show()

    def ajouter_point(self, nombre):
        for i in range(nombre):
            self.add_node(i)
    
    def n_face(self):
        pass
    
    def matrix_zero(self, nombre):
        liste = []
        for i in range(nombre):
            liste.append(0)
        self.matrix = np.array(liste, ndim= nombre)
    
    def ajouter_arrete(self, s_depart, s_arrivee):
        self.add_edge(s_depart, s_arrivee)
        self.number_of_edge += 1

    def verifier_s(self, sommet):
            if self.degree(sommet) <= 3:
                return True
            elif self.degree(sommet) >= 3:
                return False
        
    def verifier_planaire(self):
        pass

    def affiche_lien(self, sommet):
        print(f"{sommet}: {3 - graph.degree(sommet)} liaison(s) possible(s).")

# LE JEUX :

def SproutGameJCJ(): # Version Joueur contre Joueur !
    état = État()
    on = 1
    nb_point = int(input("Veuilliez choisir un nombre de point:"))
    état.graph.ajouter_point(nb_point) # On crée les points.
    état.graph.affichage() # Premier affichage.
    print("La partie commence !")
    while on == 1:
        print("Joueur 1, à toi de jouer !") # Joueur 1, joue.
        choix1 = input("Joueur 1, choisit le point de départ :") 
        choix2 = input("Joueur 1, choisit le point d'arrivée :") 
        état.graph.ajouter_arrete(choix1,choix2)
        # On vérifie qu'il n'y a d'incohérence comme un noeuds avec plus de 3 branches.
        if état.graph.verifier_s(choix1) is False:
            print("Tu enfreins une des règles du jeu. On recommence le tour !")
            continue
        if état.graph.verifier_s(choix2) is False:
            print("Tu enfreins une des règles du jeu. On recommence le tour !")
            for i in range(nb_sommet):
                if état.graph.verifier_s(i) is False:
                    count += 1
            if count == nb_sommet:
                print("Joueur 2, a perdu !")
                break
        état.graph.affichage() # À partir de maintenant on va afficher à chaque modification du graphe.
        for i in range(nb_point): 
            état.graph.affiche_lien(i)
        print("Joueur 2, à toi de jouer !") # Joueur 2, joue.
        choix3 = input("Joueur 2, choisit le point de départ :") 
        choix4 = input("Joueur 2, choisit le point d'arrivée :") 
        état.graph.ajouter_arrete(choix1,choix2) 
        if état.graph.verifier_s(choix1) is False:
            print("Tu enfreins une des règles du jeu. On recommence le tour !")
            continue
        if état.graph.verifier_s(choix2) is False:
            print("Tu enfreins une des règles du jeu. On recommence le tour !")
            for i in range(nb_sommet):
                if état.graph.verifier_s(i) is False:
                    count += 1
            if count == nb_sommet:
                print("Joueur 1, a perdu !")
                break
        état.graph.affichage() 
        for i in range(nb_point): 
            état.graph.affiche_lien(i)


























