import matplotlib.pyplot as plt
import networkx as nx 
graph = nx.Graph()

def jeu_des_pousses(n):
    #Mode Joueur vs Joueur:
    if n == 1:
    #Création du plan de jeu:
        bon_choix = 1
        listebon = []
        listepasbon =[]
    #Choix du nombre de point:
        while bon_choix == 1:
            choix_point = int(input("Choisir le nombre de point:"))
            if choix_point < 2 :
                print("Il faut avoir deux point minimum !")
            else :
                bon_choix =0
    
    #On pose les points sur le plan:s
        for i in range (choix_point):
            graph.add_node(i)
            listebon.append(i)
    #La partie :
        bon_choix = 1
        while bon_choix == 1:
        # Joueur 1:
            print('Joueur 1 à toi de jouer !')
            choix_arete = int(input('Que veux-tu faire ? 1: Faire une boucle. 2: Relier deux arêtes.'))
            if choix_arete == 1:
                sommet = input('Choisit l\'arête que tu souhaites:')
                if graph.degree(sommet) == '3':
                    print('Celui-là est déjà plein !')
                graph.add_edge(sommet, sommet)
            elif choix_arete == 2:
                sommet = input('Choisit le sommet de départ:')
                if graph.degree(sommet) == '3' :
                    print('Celui-là est déjà plein !')
                sommet2 = input('Choisit le sommet d\'arrivée:')
                if graph.degree(sommet2) == '3' :
                    print('Celui-là est déjà plein !')
                graph.add_edge(sommet, sommet2)
            else:
                print('Pourquoi es-tu si stupide T-T...')
            for i in graph.nodes:
                if graph.degree(i) <= 3:
                    print(f"{i} est ok, il lui reste {3 - graph.degree(i)}.")
                else:
                    listepasbon.append(i)
                    print(f"{i} est complet.")
                    if len(listepasbon) == choix_point:
                        print("Joueur 1 a remporté la partie !")
                        break

        # Joueur 2:
            print('À toi de jouer Joueur 2 !')
            choix_arete = int(input('Que veux-tu faire ? 1: Faire une boucle. 2: Relier deux arêtes.'))
            if choix_arete == 1:
                sommet = input('Choisit l\'arête que tu souhaites:')
                if graph.degree(sommet) == '3':
                    print('Celui-là est déjà plein !')
                graph.add_edge(sommet, sommet)
            elif choix_arete == 2:
                sommet = input('Choisit le sommet de départ:')
                if graph.degree(sommet) == '3':
                    print('Celui-là est déjà plein !')
                sommet2 = input('Choisit le sommet d\'arrivée:')
                if graph.degree(sommet2) == '3':
                    print('Celui-là est déjà plein !')
                graph.add_edge(sommet, sommet2)
            else:
                print('Pourquoi es-tu si stupide T-T...')
            for i in graph.nodes:
                if graph.degree(i) <= 3:
                    print(f"{i} est ok, il lui reste {3 - graph.degree(i)}.")
                else:
                    listepasbon.append(i)
                    print(f"{i} est complet.")
                    if len(listepasbon) == choix_point: 
                        print("Joueur 2 a remporté la partie !")
                        break

        

       
jeu_des_pousses(1)
