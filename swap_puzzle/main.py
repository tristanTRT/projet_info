from grid import Grid
from solver import Solver
from graph import Graph 
import matplotlib.pyplot as plt

data_path = "/workspaces/projet_info/input/"
file_name = data_path + "grid0.in"




g = Grid.grid_from_file(file_name) # test avec l'input grid0.in


a = Grid(1,1)
a.afficher_grille(g) # test de la représentation graphique d'une grille appliquée à g

s = Solver()
print(s.get_solution(g)) # résout la grille g






graph1 = Graph.graph_from_file(data_path + "graph2.in")
graph4 = Graph.graph_from_file(data_path + "graph4.in")
print(graph1) # le fichier donne le nombre de noeuds et le nombres de ponts au total / il décrit ensuite les arrangements faits entre les ponts
# But de l'implementation initiale de BFS : trouver plus court chemin entre noeud 1 et 2 par exemple 



print(graph1.bfs(2,10), 'resultats 1')



import os # pour lire le chemin d'accès au fichier crée par chemins possibles
import shutil # pour déplacer le fichier crée par chemins possibles

h1 = Grid(2,2)

graph_produit = Grid(2,2)
liste_grilles_possibles = h1.creation_grilles_possibles(g) # renvoie liste grilles

graph_produit.creation_des_ponts(liste_grilles_possibles)

noeud_grille_source = Grid(2,2) 
noeud_grille_cible = Grid(2,2)

source = noeud_grille_source.recherche_bonne_grille(liste_grilles_possibles, [[3, 4], [1, 2]])# noeud grille source 
cible = noeud_grille_cible.recherche_bonne_grille(liste_grilles_possibles, [[4, 1], [2, 3]])# noeud grille cible 

print(source,cible, "donnees")


h = Graph()

print(graph_produit.creation_des_ponts(liste_grilles_possibles))

destination_path = "/workspaces/projet_info/input/"
shutil.move(str(graph_produit.creation_des_ponts(liste_grilles_possibles)), destination_path) # bouge le fichier avec le fichier de la liste des ponts entre les noeuds
os.remove("/workspaces/projet_info/input/nouveau.in")

graph1 = Graph.graph_from_file(destination_path +'graph1.in') #crée graph avec le fichier d'entrée et la liste des ponts
print(type(graph1))

#print(graph1.bfs(noeud_grille_source,noeud_grille_cible), 'resultat')# applique le bfs au graphe avec h4 grille source et h5 grille cible 
print(graph4.bfs(source,cible), 'resultats 2')
