import networkx as nx 
import matplotlib.pyplot as plt
import time

#Le graphe qui est définit en global !
graph = nx.Graph()

def ajout_point():
    global graph
    on = 1
    nodes = int(input("Nombres de points:"))
    while on == 1:
        if nodes < 2 :
            print("recommence")
        else:
            for i in range(nodes):
                graph.add_node(i)
                print(f"Le point {i} a été ajouté !")
            on = 0
    return nodes

def verify(node):
    global graph
    if graph.degree(node) > 2:
        return False
    return True

def verify_all(nodes):
    global graph
    compteur = 0
    for i in range(nodes):
        if verify(i) is False:
            compteur += 1
    if compteur == nodes:
        return False

def jeu(i, nodes, increment):
    global graph
    on = 1
    print(f"Joueur {i}")
    print("Choisit les points à relier :")
    while on == 1: 
        choix_1 = int(input("le premier :"))
        if verify(choix_1) is False:
            print(f"{choix_1} est full, choisis-en un autre !")
        else:
            on = 0
    on = 1
    while on == 1:
        choix_2 = int(input("le deuxième :"))
        if verify(choix_2) is False:
            print(f"{choix_2} est full, choisis-en un autre !")
        else:
            on = 0
    name = nodes + increment
    graph.add_node(name)
    graph.add_edge(choix_1, name)
    graph.add_edge(name, choix_2)
    afficher()
        

def afficher():
    global graph
    nx.draw(graph, with_labels=True)
    plt.show(block=False)

def afficher_point(nodes, increment):
    global graph
    number_of_nodes = nodes + increment
    for i in range(number_of_nodes + 1):
        print(f"Le point {i} est d'ordre {graph.degree(i)}.")

def main():
    global graph
    on = 1
    nodes = ajout_point()
    increment = 0
    while on == 1 :
        jeu(1, nodes, increment)
        if verify_all(nodes) == False:
            print("Joueur 1 a gagné !!!")
            on = 0
        time.sleep(10)
        plt.close()
        afficher_point(nodes, increment)
        increment += 1
        jeu(2, nodes, increment)
        if verify_all(nodes) == False:
            print("Joueur 2 a gagné !!!")
            on = 0 
        time.sleep(10)
        plt.close()
        afficher_point(nodes, increment)
        increment += 1
print(main())
























