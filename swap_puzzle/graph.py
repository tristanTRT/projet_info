"""
This is the graph module. It contains a minimalistic Graph class.
"""


class Graph:
   """
   A class representing undirected graphs as adjacency lists.


   Attributes:
   -----------
   nodes: NodeType
       A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
       We will usually use a list of integers 1, ..., n.
   graph: dict
       A dictionnary that contains the adjacency list of each node in the form
       graph[node] = [neighbor1, neighbor2, ...]
   nb_nodes: int
       The number of nodes.
   nb_edges: int
       The number of edges.
   edges: list[tuple[NodeType, NodeType]]
       The list of all edges
   """


   def __init__(self, nodes=[]):
       """
       Initializes the graph with a set of nodes, and no edges.


       Parameters:
       -----------
       nodes: list, optional
           A list of nodes. Default is empty.
       """
       self.nodes = nodes
       self.graph = dict([(n, []) for n in nodes])
       self.nb_nodes = len(nodes)
       self.nb_edges = 0
       self.edges = []
      
   def __str__(self):
       """
       Prints the graph as a list of neighbors for each node (one per line)
       """
       if not self.graph:
           output = "The graph is empty"           
       else:
           output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
           for source, destination in self.graph.items():
               output += f"{source}-->{destination}\n"
       return output


   def __repr__(self):
       """
       Returns a representation of the graph with number of nodes and edges.
       """
       return f"<graph.Graph: nb_nodes={self.nb_nodes}, nb_edges={self.nb_edges}>"


   def add_edge(self, node1, node2):
       """
       Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes.
       When adding an edge between two nodes, if one of the ones does not exist it is added to the list of nodes.


       Parameters:
       -----------
       node1: NodeType
           First end (node) of the edge
       node2: NodeType
           Second end (node) of the edge
       """
       if node1 not in self.graph:
           self.graph[node1] = []
           self.nb_nodes += 1
           #self.nodes.append(node1)
       if node2 not in self.graph:
           self.graph[node2] = []
           self.nb_nodes += 1
           #self.nodes.append(node2)


       self.graph[node1].append(node2)
       self.graph[node2].append(node1)
       self.nb_edges += 1
       self.edges.append((node1, node2))
          


   def bfs(self, src, dst):
       """
       Finds a shortest path from src to dst by BFS. 


       Parameters:
       -----------
       src: NodeType
           The source node.
       dst: NodeType
           The destination node.


       Output:
       -------
       path: list[NodeType] | None
           The shortest path from src to dst. Returns None if dst is not reachable from src
       """
      
       def filtre (ref_index, cobaye_index, candidat_index) : #FONCTIONNE POUR LES MATRICES CARÉES ET COLONNES ET LIGNES
           from grid import Grid
           from solver import Solver
           from graph import Graph
          
           data_path = "/workspaces/projet_info/input/"
           file_name = data_path + "grid1.in"


           # 3 ENTRÉES :
           #REF (GRILLE QUE L'ON RECHERCHE À OBTENIR)
           #COBAYE (GRILLE D'OU L'ON PART)
           #CANDIDAT (GRILLE DONT ON ÉTUDIE SI ON LA MET DANS LA LISTE)


           #PROCESS DE COMTPTAGE DES CASES BIEN RANGÉES ENTRE REF ET COBAYE
           #APPLICATION À CANDIDAT : IL FAUT QUE CANDIDAT AIT AU MOINS ENCORE CES CASES BIEN RANGÉES AVEC REF




           g = Grid.grid_from_file(file_name)




           auxilliaire_1 = Grid(2,2)
           liste_grilles_possibles = auxilliaire_1.creation_grilles_possibles(g)


           ref = liste_grilles_possibles[ref_index]
           cobaye = liste_grilles_possibles[cobaye_index]
           candidat = liste_grilles_possibles[candidat_index]# Convertit le num du noeud en la matrice associée
          


           if (len(ref[0]) != 1) and (len(ref) != 1) : # vérification que format de la matrice n'est pas matrice ligne ni colonne
               colonne = 0
               ligne = 0
               compteur = 0
               for ligne in range (len(ref)):
                   for colonne in range (len(ref[0])) :
                       if int(ref[ligne][colonne]) == int(cobaye[ligne][colonne]) :
                           compteur += 1
                      


               # i = nb de caractères bien rangés avant le 1er dérangement : on ne doit pas toucher à ceux-là
               colonne = 0
               ligne = 0 
               for caratere in range (compteur-1) : # on ne veut répéter la condition que compteur -1 fois car le 1er dérangement a lieu à compteur
                   # donc il y a compteur -1 bonnes valeurs rangées
                   if ref[ligne][colonne] != candidat[ligne][colonne] :
                       return(False, compteur)
                   colonne = colonne +1
                  
                   if colonne == len(ref[0]) :
                       colonne = 0
                       ligne  = ligne +1


               return(True)




           elif (len(ref[0]) != 1) : # cas de la matrice ligne
               colonne = 0
               compteur = 0
               while int(ref[0][colonne]) == int(cobaye[0][colonne]) and compteur != len(ref[0]) :
                   compteur += 1
                   colonne += 1
              
               colonne = 0
               for caratere in range (compteur-1) : # on ne veut répéter la condition que compteur -1 fois car le 1er dérangement a lieu à compteur
                   # donc il y a compteur -1 bonnes valeurs rangées
                   if ref[0][colonne] != candidat[0][colonne] :
                       return(False, compteur)
                   colonne = colonne +1


               return(True)


           else : # cas de la matrice colonne
               ligne = 0
               compteur = 0
               while int(ref[ligne][0]) == int(cobaye[ligne][0]) and compteur != len(ref) :
                   ligne += 1
                   compteur += 1
              
               ligne = 0
               for caratere in range (ligne-1) : # on ne veut répéter la condition que compteur -1 fois car le 1er dérangement a lieu à compteur
                   # donc il y a compteur -1 bonnes valeurs rangées
                   if ref[ligne][0] != candidat[ligne][0] :
                       return(False, compteur)
                   ligne = ligne +1
               return(True)
      




       from grid import Grid
       from solver import Solver
       from graph import Graph
       from collections import deque


       chemin = set([src]) # A chaque noeud exploré on va le mettre dans le chemin parcouru
       predecesseurs = {src: None} #nécessaire pour reconstituer le chemin le plus court
       queue = deque([src])




       while queue :
           noeud_actuel = queue.popleft()


           for noeud in self.graph[noeud_actuel] :
               if (noeud not in chemin) and filtre(dst, noeud_actuel, noeud) : # cela ne sert à rien de mettre deux fois un même noeud dans la liste de ceux à explorer
                   queue.append(noeud)
                   chemin.add(noeud)
                   predecesseurs[noeud] = noeud_actuel


                   if noeud == dst :
                       path = [noeud]
                       while predecesseurs[path[-1]] is not None:
                           path.append(predecesseurs[path[-1]])
                       path.reverse()
                       return path
      
       return None
          
              




   @classmethod
   def graph_from_file(cls, file_name):
       """
       Reads a text file and returns the graph as an object of the Graph class.


       The file should have the following format:
           The first line of the file is 'n m'
           The next m lines have 'node1 node2'
       The nodes (node1, node2) should be named 1..n


       Parameters:
       -----------
       file_name: str
           The name of the file


       Outputs:
       -----------
       graph: Graph
           An object of the class Graph with the graph from file_name.
       """
       with open(file_name, "r") as file:
           n, m = map(int, file.readline().split())
           graph = Graph(range(1, n+1))
           for i in range(m):
               edge = list(map(int, file.readline().split()))
               if len(edge) == 2:
                   node1, node2 = edge
                   graph.add_edge(node1, node2) # will add dist=1 by default
               else:
                   raise Exception("Format incorrect")
       return graph
  












   def heuristique (self, noeud_cible, noeud_candidat) :
       from grid import Grid
       from solver import Solver
       from graph import Graph
       data_path = "/workspaces/projet_info/input/"
       file_name = data_path + "grid1.in"
       import numpy as np


       g = Grid.grid_from_file(file_name)




       auxilliaire_1 = Grid(2,2)
       liste_grilles_possibles = auxilliaire_1.creation_grilles_possibles(g)


       grille_cible = liste_grilles_possibles[noeud_cible]
       grille_cobaye = liste_grilles_possibles[noeud_candidat]


       heuristique = 0
       for ligne in range (len(grille_cobaye)):
           for colonne in range (len(grille_cobaye[0])) :
               if grille_cobaye[ligne][colonne] != grille_cible[ligne][colonne] :
                   for lignee in range (len(grille_cible)) :  
                       if (grille_cobaye[ligne][colonne] in list(grille_cible[lignee])) == True :
                           infos = list(grille_cible[lignee]).index(grille_cobaye[ligne][colonne])
                           calcul1 = np.abs(lignee - ligne)
                           calcul2 = np.abs(infos - colonne)
                           heuristique = heuristique + calcul1 + calcul2


       heuristique = heuristique /2
       return(heuristique)
  


   def A_star(self, src, dst):
       from grid import Grid
       from solver import Solver
       from graph import Graph
       import heapq


       chemin = set([src])  # A chaque noeud exploré on va le mettre dans le chemin parcouru
       predecesseurs = {src: None}  # nécessaire pour reconstituer le chemin le plus court
       queue = [(0, 0, 0, src)]  # 1ere valeur : somme des heuristiques et coût réel, 2e valeur : coût réel, 3e valeur : heuristique (distance de Manhattan), 4e valeur : numéro/index du noeud
       compteur = 1


       while queue and compteur != 10:
           noeud_actuel = heapq.heappop(queue)  # Retirez le nœud avec la priorité la plus basse
           compteur = compteur + 1


           for noeud in self.graph[noeud_actuel[3]]:
               compteur = compteur + 1
               if noeud not in chemin:  # cela ne sert à rien de mettre deux fois un même noeud dans la liste de ceux à explorer
                   auxilliaire = Graph()
                   nouvel_element = (noeud_actuel[0] + 1 + auxilliaire.heuristique(dst, noeud), noeud_actuel[0] + 1, auxilliaire.heuristique(dst, noeud), noeud)
                   heapq.heappush(queue, nouvel_element)
                   chemin.add(noeud)
                   predecesseurs[noeud] = noeud_actuel[3]


                   if noeud == dst:
                       path = [noeud]
                       while predecesseurs[path[-1]] is not None:
                           path.append(predecesseurs[path[-1]])
                       path.reverse()
                       return path
                  
                   compteur = compteur + 1
              
       return None
  

