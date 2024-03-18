"""
This is the grid module. It contains the Grid class and its associated methods.
"""


import random
import matplotlib.pyplot as plt


class Grid():
   """
   A class representing the grid from the swap puzzle. It supports rectangular grids.


   Attributes:
   -----------
   m: int
       Number of lines in the grid
   n: int
       Number of columns in the grid
   state: list[list[int]]
       The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column.
       Note: lines are numbered 0..m and columns are numbered 0..n.
   """
  
   def __init__(self, m, n, initial_state = []):
       """
       Initializes the grid.


       Parameters:
       -----------
       m: int
           Number of lines in the grid
       n: int
           Number of columns in the grid
       initial_state: list[list[int]]
           The intiail state of the grid. Default is empty (then the grid is created sorted).
       """
       self.m = m
       self.n = n
       if not initial_state:
           initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]           
       self.state = initial_state


   def __str__(self):
       """
       Prints the state of the grid as text.
       """
       output = f"The grid is in the following state:\n"
       for i in range(self.m):
           output += f"{self.state[i]}\n"
       return output


   def __repr__(self):
       """
       Returns a representation of the grid with number of rows and columns.
       """
       return f"<grid.Grid: m={self.m}, n={self.n}>"


   def is_sorted(self):
       """
       Checks is the current state of the grid is sorte and returns the answer as a boolean.
       """
       compteur = 1 # donne la valeur théorique de chaque case que l'on va parcourir : on ajoute +1 à element à chaque case parcourue
       Faux = 0 # On part du principe que la grille est rangée avant de l'étudier
       for i in range (self.m) :
           for j in range (self.n) :
               if self.state[i][j] != compteur : # si on trouve un écart avec la valeur attendue à la case analysée : c'est que la grille est dérangée
                   Faux = 1
               compteur = compteur +1
       return(Faux == 0) # teste si la grille est bien rangée (booléen : True ou False si Faux == 1)
              


   def swap(self, cell1, cell2):
       import numpy as np
       """
       Implements the swap operation between two cells. Raises an exception if the swap is not allowed.
       Parameters:
       -----------
       cell1, cell2: tuple[int]
           The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell.
       """
       # Teste si le swap est légal :
       # soit c'est un swap en ligne et les ordonnées doivent être égales et l'écart entre les abscisses plus petit que 1 en valeur absolue
       # soit c'est un swap en colonne et les abscisses doivent être égales et l'écart entre les ordonnées plus petit que 1 en valeur absolue
       if (np.abs(cell1[0] - cell2[0]) <= 1  and cell1[1]==cell2[1]) or (np.abs(cell1[1] - cell2[1]) <= 1 and (cell1[0] == cell2[0])): 
           a = self.state[cell1[0]][cell1[1]]
           b = self.state[cell2[0]][cell2[1]]
           self.state[cell1[0]][cell1[1]] = b
           self.state[cell2[0]][cell2[1]] = a
       else :
           raise NotImplementedError


   def swap_seq(self, cell_pair_list):
       """
       Executes a sequence of swaps.


       Parameters:
       -----------
       cell_pair_list: list[tuple[tuple[int]]]
           List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers).
           So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
       """
       # Pour chaque swap voulu, on appelle la fonction swap
       for i in range (len(cell_pair_list)) :    
           self.swap(cell_pair_list[i][0], cell_pair_list[i][1])
       else :
           raise NotImplementedError


   @classmethod
   def grid_from_file(cls, file_name):
       """
       Creates a grid object from class Grid, initialized with the information from the file file_name.
      
       Parameters:
       -----------
       file_name: str
           Name of the file to load. The file must be of the format:
           - first line contains "m n"
           - next m lines contain n integers that represent the state of the corresponding cell


       Output:
       -------
       grid: Grid
           The grid
       """
       with open(file_name, "r") as file:
           m, n = map(int, file.readline().split())
           initial_state = [[] for i_line in range(m)]
           for i_line in range(m):
               line_state = list(map(int, file.readline().split()))
               if len(line_state) != n:
                   raise Exception("Format incorrect")
               initial_state[i_line] = line_state
           grid = Grid(m, n, initial_state)
       return grid


   def afficher_grille(self, grille):
       fig, ax = plt.subplots()#crée un repère avec abscisses et ordonnées
       ax.set_xticks([])
       ax.set_yticks([])#cache les graduations du repère




       # Dessiner la grille
       for i in range(1, grille.m+2): #dessine lignes horizontales +2 car décalage dessin (du fait de l'axe des abscisses et ordonnées qui créent artificiellemnt 1 case en trop)
           ax.axhline(i, color='black', lw=1)
       for j in range (1, grille.n+2): #dessine lignes verticales +2 car décalage dessin (du fait des axes)
           ax.axvline(j, color='black', lw=1)
      
       # Placement des points 
       for i in range (grille.m) :
           for j in range (grille.n) :
               x = j +0.5 +1 #+1 pour le décalage lié aux axes
               y = grille.m-i-0.5+1 #+1 pour le décalage lié aux axes
               ax.text(x, y, f"{grille.state[i][j]}", ha='center', va='center', fontsize=12) # positionnement des chiffres dans la bonne case de la grille (x,y), choix de la taille de la police et du centrage du chiffre


       plt.show()


  
   def creation_grilles_possibles (self, grille) : # grille est la grille que l'on souhaite trier
       import copy
       #fonction auxilliaire pour ne pas avoir des grilles avec plusieurs fois le même nombre dedans
       def est_present (grille_test, element) :
           for i in range (len(grille_test)) :
               if (element in grille_test[i]) == True :
                   return(True)
           return(False)
              
       #fonction auxilliaire pour ne pas avoir des 2 grilles pareilles dans la liste
       def existe_deja (liste, grille_candidate, nb_fois) :
           compteur = 0
           for element in liste :
               if grille_candidate == element :
                   compteur = compteur +1
                   if compteur == nb_fois :
                       return(True)
           return(False)
      
       #fonction auxilliaire pour avoir une idée du nombre de grilles qu'on construit pareilles quand on remplit la case (0,0) (6) puis (0,1) (2) et (1,0) (1) et enfin (1,1) (1) dans le cas d'une matrice de taille 2*2
       def nbb_fois (grille, factorielle) :
           liste = []
           for i in range (1,grille.n*grille.m +1) :
               liste.append(i)
           nb_fois = []
           for j in range (1,grille.n*grille.m+1) :
               diviseur = 1
               for l in range (1,j+1) :
                   diviseur = diviseur * liste[-l]
               nb_fois.append(int(factorielle/diviseur))
           return(nb_fois)
      
       #fonction auxilliaire : necessaire de retourner la liste renvoyée par nbbfois ...
       def retournement (liste) :
           correction = []
           for i in range (1, len(liste)+1) :
               correction.append(liste[-i])
           return(correction)


       #Création de l'outil factorielle
       factorielle = 1
       for i in range (1,grille.m * grille.n +1) :
           factorielle = i * factorielle


       # génération des (m*n)! grilles de taille (m,n) différentes que l'on va ensuite remplir / OK fonctionne
       liste = [[[0 for i in range (grille.n)] for j in range (grille.m)] for l in range (factorielle)]
       ligne = 0
       colonne = 0
       choix_possibles = []


       for i in range(1, grille.n * grille.m + 1):
           choix_possibles.append(i)


       nb_foiss = retournement(nbb_fois(grille, factorielle))


       diviseur = grille.n * grille.m


       for case in range(grille.n * grille.m - 1, -1, -1):
           numero_grille = 0
           for nombre in choix_possibles:
               compteur_occurence_nombre = 0
               while compteur_occurence_nombre != factorielle // len(choix_possibles) :
                   if (
                       ligne < grille.m
                       and colonne < grille.n
                       and not est_present(liste[numero_grille], nombre)
                       and liste[numero_grille][ligne][colonne] == 0
                   ):
                       grille_candidate = copy.deepcopy(liste[numero_grille])
                       grille_candidate[ligne][colonne] = nombre
                       if not existe_deja(liste, grille_candidate, nb_foiss[case]):
                           liste[numero_grille][ligne][colonne] = nombre
                           compteur_occurence_nombre += 1
                   numero_grille += 1
               numero_grille = 0




           # Pour passer à la case d'après
           colonne += 1
           if colonne == grille.n:
               colonne = 0
               ligne += 1
       return liste


           
   def creation_des_ponts (self, liste_grilles) : # fonction qui renvoie l'ensemble des ponts possibles entre les grilles d'une liste de grilles en input
       # format de retour : écriture d'un fichier avec en 1ere ligne le nombre de noeuds du graphe (nb de configurations de la grille) et le nombre de ponts entre les noeuds
       # puis nsur chaque ligne suivante, le pont désigné par la grille de départ et d'arrivée séparée par un espace
       # chaque grille est désignée par son index (position) dans la liste des grilles possibles
       import os
      
       liste_grilles = list(liste_grilles)
       def pont_possible (grille_1, grille_2) :
           changements = []
           for i in range (len(grille_1)) : #len(...) = nb de lignes de grille_1
               for j in range (len(grille_1[0])) : # len(...) = nb_colonnes de grille_1
                   if grille_1[i][j] != grille_2[i][j] : # relève une différence
                       Legal = 1 # Par défaut le changement est illégal
                       if (j+1) < len(grille_1[0]) :
                           if (grille_1[i][j] == grille_2[i][j+1]) :
                               Legal = 0


                       if (j-1) >= 0 :
                           if (grille_1[i][j] == grille_2[i][j-1]) : #necessaire de faire cette verif pour pas avoir de index out of range
                               Legal = 0
                          
                       if (i-1) >= 0 :
                           if (grille_1[i][j] == grille_2[i-1][j]) : #necessaire de faire cette verif pour pas avoir de index out of range
                               Legal = 0
                          
                       if (i+1) < len(grille_1) :
                           if (grille_1[i][j] == grille_2[i+1][j]) : #necessaire de faire cette verif pour pas avoir de index out of range
                               Legal = 0
                       changements.append(Legal)


           if len(changements) > 2 :
               return(False)
          
           if (1 in changements) == True :
               return(False)


           else :
               return(True)
                  


       liste_ponts = []  
        
       for grille in liste_grilles : # pour chaque grille de la liste grille, on va tester si un pont est possibles avec les autres composantes de cette liste de grilles
           for grille_test in liste_grilles :
               if grille_test != grille : # évacue le cas où on compare la grille avec elle-même
                   if pont_possible(grille, grille_test) == True :
                       liste_ponts.append(str(liste_grilles.index(grille)) + " " + str(liste_grilles.index(grille_test)))
       # le format est ici une liste de chaînes de caractère (nombres) séparées par un espace, on va alors créer un fichier
      
       #ecriture du fichier de retour (cf format attendu pour appliquer le BFS)
       fichier = open('nouveau.in', 'w', encoding='utf-8')
       fichier.write(str(len(liste_grilles))+" "+ str(len(liste_ponts)) +"\n") #ecriture de la première ligne : nb grilles (noeuds) et nb de ponts
      
       for element in liste_ponts :
           fichier.write(str(element)+"\n") # retour à la ligne nécessaire
       fichier.close()
      
       return(os.path.abspath('nouveau.in'))#le fichier s'appelle 'nouveau.in' # on pourra y accéder à l'aide de ce chemin d'accès
       # renvoie la liste des ponts possibles entre les "noeuds" que sont les différentes grilles sous forme d'une liste
       # l'index de chaque grille est le noeud qui lui correspond sur le graphe
  
  
   def recherche_bonne_grille (self, liste_grille, grille_source) :
       liste_grille = list(liste_grille)
       for grille in (liste_grille) :
           if grille_source == grille :
               return(liste_grille.index(grille))
   #renvoie la position de la grille voulue parmi l'ensemble des grilles possibles : c'est le numéro du noeud de départ sur le graphe


   def creation_du_fichier (self, file_name) :
       with open(file_name, "r") as file : #lit le fichier
           ligne1 = list(map(int, file.readline().split()))
           niveau_difficulte = file.readline() # lit l'éloignement voulu par l'utilisateur depuis la solution rangee (mesure en nb de mouv mini)
           fichier = open('difficulte_control_grille_range.in', 'w', encoding='utf-8')
           fichier.write(str(ligne1[0]) + " " + str(ligne1[1])+"\n") #indique la taille de la matrice
           compteur = 1
           for j in range (ligne1[0]) :
               for i in range (ligne1[1]-1) :
                   fichier.write(str(compteur)+" ")
                   compteur = compteur + 1
               fichier.write(str(compteur)+"\n")
               compteur = compteur +1
           fichier.close()
           # bouge le fichier avec le fichier de la liste des ponts entre les noeuds
       return(niveau_difficulte)
       #la fonction fonctionne 
       #cree une matrice rangée de taille cible
       #stocke dans un fichier nommé 'difficulte_control_grille_rangee'
       #return le nom de ce fichier


   #fonction auxilliaire de difficulte_control
   def conversion_liste(self, grid_entree) :
       liste = [[]for i in range (grid_entree.m)]
       for i in range (grid_entree.m) :
           for j in range (grid_entree.n) :
               liste[i].append(grid_entree.state[i][j])
       return(liste)




   # BUT : fonction qui lit un fichier comportant la taille de la matrice et le nombre mini de swaps pour avoir la résolution(= difficulté souhaitée)
   # elle renvoie l'index d'une matrice du niveau souhaitée au sein de l'ensemble des matrices possibles
   def difficulte_control (self, file_name) : #prend en fichier source 2 lignes : taille de la matrice / éloignement de la matrice rangée
       import copy
       import random as rd
       import os
       import shutil
       from graph import Graph
       destination_path = "/workspaces/projet_info/input/"


       auxilliaire_0 = Grid(1,1)
       niveau_difficulte = auxilliaire_0.creation_du_fichier(file_name)
       #cree une matrice rangée de taille cible
       #stocke dans un fichier nommé 'difficulte_control_grille_rangee'
       #return le nom de ce fichier


       shutil.move("/workspaces/projet_info/difficulte_control_grille_range.in", destination_path)
      


       grille = Grid.grid_from_file("/workspaces/projet_info/input/difficulte_control_grille_range.in") # format grid_input requis
       auxilliaire = Grid(1,1)   
       liste_grilles_possibles= auxilliaire.creation_grilles_possibles(grille) #renvoie les grilles de taille 2*2 possibles


       graph_produit = Grid(2,2)
       stock_chemin_graphe = graph_produit.creation_des_ponts(liste_grilles_possibles)
      
      
       grille_derangee = copy.deepcopy(grille) #ok fonctionne
      


       eloignement_solution = 0
       while eloignement_solution < int(niveau_difficulte) :
           ligne_random = rd.randint(0, grille.m-1)
           colonne_random = rd.randint(0,grille.n-1)
           swaps_possibles = []
           if (ligne_random - 1) != -1 :
               swaps_possibles.append([ligne_random-1,colonne_random])
          
           if (ligne_random +1) <= grille.m - 1 :
               swaps_possibles.append([ligne_random+1, colonne_random])


           if (colonne_random -1) != -1 :
               swaps_possibles.append([ligne_random, colonne_random -1])
          
           if (colonne_random +1) <= grille.n -1 :
               swaps_possibles.append([ligne_random, colonne_random +1])
          
           swap = rd.randint(0,len(swaps_possibles)-1)
          


           grille_derangee.swap((ligne_random,colonne_random), (swaps_possibles[swap][0],swaps_possibles[swap][1]))




          
           # ok fonctionne le dérangement
           auxilliaire_2 = Grid(1,1)
           auxilliaire_3 = Grid(1,1)
          
           grille_liste = auxilliaire_2.conversion_liste(grille) #necessaire pour après pouvoir aller chercher l'index
           grille_derangee_liste = auxilliaire_3.conversion_liste(grille_derangee) #necessaire pour après pouvoir aller chercher l'index
      
          
           index_grille_derangee = liste_grilles_possibles.index(grille_derangee_liste) # numero du noeud de grille derangee dans le graphe
           index_grille_rangee = liste_grilles_possibles.index(grille_liste)
           print(index_grille_derangee,index_grille_rangee)


           graph1 = Graph.graph_from_file(stock_chemin_graphe)
          
           eloignement_solution = len(graph1.bfs(index_grille_derangee, index_grille_rangee))


       os.remove("/workspaces/projet_info/nouveau.in")
       os.remove("/workspaces/projet_info/input/difficulte_control_grille_range.in")
       return(grille_derangee)



