from grid import Grid
from solver import Solver
from graph import Graph 
import matplotlib.pyplot as plt

data_path = "/workspaces/projet_info/input/"
file_name = data_path + "grid0.in"




g = Grid.grid_from_file(file_name)


a = Grid(1,1)

a.afficher_grille(g)

s = Solver()

print(s.get_solution(g)) # affiche la grille initiale



s.afficher_grille(g) # affiche la grille résolue




graph1 = Graph.graph_from_file(data_path + "graph2.in")
print(graph1) # le fichier donne le nombre de noeuds et le nombres de ponts au total / il décrit ensuite les arrangements faits entre les ponts

# But de l'implementation initiale de BFS : trouver plus court chemin entre noeud 1 et 2 par exemple 

h = Graph()

print(h.bfs(graph1, 2,10), 'resultat')


import os # pour lire le chemin d'accès au fichier crée par chemins possibles
import shutil # pour déplacer le fichier crée par chemins possibles

h1 = Grid(2,2)
h3 = Grid(2,2)
h2 = h1.creation_grilles_possibles(g) # renvoie liste grilles

h3.creation_des_ponts(h2)

h4 = Grid(2,2) 
h5 = Grid(2,2)

h4.recherche_bonne_grille(h2, [[3, 4], [1, 2]])# noeud grille source 
h5.recherche_bonne_grille(h2, [[4, 1], [2, 3]])# noeud grille cible 



h = Graph()

print(h3.creation_des_ponts(h2))

destination_path = "/workspaces/projet_info/input/"
shutil.move(str(h3.creation_des_ponts(h2)), destination_path) # bouge le fichier avec le fichier de la liste des ponts entre les noeuds


graph1 = Graph.graph_from_file(destination_path +'graph1.in') #crée graph avec le fichier d'entrée et la liste des ponts


print(h.bfs(graph1, h4,h5), 'resultat')# applique le bfs au graphe avec h4 grille source et h5 grille cible 

