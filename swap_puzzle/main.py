from grid import Grid
from solver import Solver
from graph import Graph 
import matplotlib.pyplot as plt

data_path = "/workspaces/projet_info/input/"
file_name = data_path + "grid4.in"




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

print(h.bfs(graph1, 2,3), 'resultat')





