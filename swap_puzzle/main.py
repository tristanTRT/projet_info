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






graph2 = Graph.graph_from_file(data_path + "graph2.in")
print(graph1) # le fichier donne le nombre de noeuds et le nombres de ponts au total / il décrit ensuite les arrangements faits entre les ponts
# But de l'implementation initiale de BFS : trouver plus court chemin entre noeud 1 et 2 par exemple 

print(graph2.bfs(2,10), 'resultats 1') # donne le plus court chemin entre le noeud 2 et 10 dans le graph2



import os # pour lire le chemin d'accès au fichier crée par chemins possibles
import shutil # pour déplacer le fichier crée par chemins possibles
auxilliaire_1 = Grid(2,2)
liste_grilles_possibles = auxilliaire_1.creation_grilles_possibles(g) # renvoie liste grilles construites à partir de g, matrice de taille 2*2 (cf grid0)

graph_produit = Grid(2,2)

graph_produit.creation_des_ponts(liste_grilles_possibles)

noeud_grille_source = Grid(2,2) 
noeud_grille_cible = Grid(2,2)

source = noeud_grille_source.recherche_bonne_grille(liste_grilles_possibles, [[3, 4], [1, 2]])# noeud grille source = index de grille source dans liste grilles
cible = noeud_grille_cible.recherche_bonne_grille(liste_grilles_possibles, [[4, 1], [2, 3]])# noeud grille cible = index de grille cible dans liste grilles
print(source,cible, "donnees")




print(graph_produit.creation_des_ponts(liste_grilles_possibles))# renvoie un chemin d'accès au fichier du graphe attendu au bon format (1 ligne avec nb de noeuds et nb de ponts) puis descriptif des ponts en question

# on va ranger ce fichier au bon endroit
destination_path = "/workspaces/projet_info/input/"
shutil.move(str(graph_produit.creation_des_ponts(liste_grilles_possibles)), destination_path) # déménage le fichier avec le fichier de la liste des ponts entre les noeuds
os.remove("/workspaces/projet_info/input/nouveau.in")# supprime le fichier généré et appelé 'nouveau.in' qui n'est plus utile 

graph1 = Graph.graph_from_file(destination_path +'graph1.in') # crée un objet de la classe graph (sur lequel appliquer le bfs) à partir du fichier crée plus haut avec l'ensemble des ponts possibles entre les différents états d'une matrice de taille 2*2
print(graph1.bfs(source,cible), 'resultats 2')# applique le bfs à ce fichier et renvoie le chemin pour aller de noeud source à noeud cible
