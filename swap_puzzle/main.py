from grid import Grid
from solver import Solver

data_path = "/home/onyxia/work/projet_info/input/"
file_name = data_path + "grid0.in"




g = Grid.grid_from_file(file_name)
print(g)

s = Solver()

print(s.get_solution(g))

from graph import Graph 

graph1 = Graph.graph_from_file(data_path + "graph1.in")
print(graph1) # le fichier donne le nombre de noeuds et le nombres de ponts au total / il décrit ensuite les arrangements faits entre les ponts

# But de l'implementation initiale de BFS : trouver plus court chemin entre noeud 1 et 2 par exemple 

h = Graph()

print(h.bfs(graph1,1,3))
