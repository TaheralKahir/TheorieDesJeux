import networkx as nx 
import matplotlib.pyplot as plt


#Le graphe qui est définit en global !
graph = nx.Graph()

def ajout_point():
    on = 1
    nodes = int(input("Nombres de points:"))
    while on == 1:
        if nodes < 2 :
            print("recommence")
        else:
            for i in range(nodes):
                graph.add_node(i)
                on = 0
                print("Les points ont été ajoutés !")
            
#def verify():

def afficher():
    nx.draw(graph, with_labels=True)
    plt.show()

def main():
    on = 1
    ajout_point()
    while on == 1 :
        print("Joueur 1")
        print("Choisit les points à relier :")
        choix_1 = int(input("le premier :"))
        choix_2 = int(input("le deuxième :"))
        graph.add_edge(choix_1, choix_2)
        afficher()
        print("Joueur 2")
        print("Choisit les points à relier :")
        choix_1 = int(input("le premier :"))
        choix_2 = int(input("le deuxième :"))
        graph.add_edge(choix_1, choix_2)
        afficher()
        on = 0

print(main())
























