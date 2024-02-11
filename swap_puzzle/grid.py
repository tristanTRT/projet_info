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

        compteur = 1 # compteur compte de 1 à m*n (taille de la matrice) : il correspond à la valeur théorique de chaque case : il est donc réévalué à +1 quand on passe d'une case à l'autre
        Faux = 0 # on considère que Faux = 0 : la grille est rangée et on va tester si la valeur de chaque case est bien égale à la valeur attendue 
        for i in range (self.m) : 
            for j in range (self.n) : 
                if self.state[i][j] != compteur :
                    Faux = 1
                compteur = compteur +1
        return(Faux == 0)
                

    def swap(self, cell1, cell2):
        import numpy as np
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.
        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        # Teste si le swap est légal : il faut que soit les 2 cases aient leurs ordonnées qui coïncident et la valeur absolue de leurs abscisses < 1 (swap de gauche à droite ou inverse 
        # ou alors abscisses qui coïncident et ordonnées éloignées de <1 en valeur absolue (swap de haut en bas)
        if (np.abs(cell1[0] - cell2[0]) <= 1  and cell1[1]==cell2[1]) or (np.abs(cell1[1] - cell2[1]) <= 1 and (cell1[0] == cell2[0])):  
            a = self.state[cell1[0]][cell1[1]] 
            b = self.state[cell2[0]][cell2[1]] 
            self.state[cell1[0]][cell1[1]] = b
            self.state[cell2[0]][cell2[1]] = a
        else : 
            raise NotImplementedError # cas où le swap voulu est illégal

    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        # parcours la liste de swaps voulus et fait appel à la fonction swap
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
        for i in range(1, grille.m+2): #dessine lignes horizontales +2 car décalage dessin (il y a une sorte de cadre à la grille, donc il nous faut 2 cases en plus pour compenser)
            ax.axhline(i, color='black', lw=1) # paramètres sur la couleur des traits et leur épaisseur
        for j in range (1, grille.n+2): #dessine lignes verticales +2 car décalage dessin (idem que pour les traits horizontaux)
            ax.axvline(j, color='black', lw=1)
        
        # Placement des points  
        for i in range (grille.m) : 
            for j in range (grille.n) :
                x = j +0.5 +1 #+1 pour le décalage lié aux axes du repère (axe des ordonnées) qui font que la grille commence avec un décalage 
                y = grille.m-i-0.5+1 #+1 pour le décalage vertical lié à l'axe des abscisses 
                ax.text(x, y, f"{grille.state[i][j]}", ha='center', va='center', fontsize=12) # positionnement des chiffres dans la grille : f pilote ce qu'on écrit, ha et va le positionnement et frontsize la taille de la police 
                # x et y pilotent la case de la grille où l'on écrit 
        plt.show()

    
    def creation_grilles_possibles (self, grille) : # grille est la grille que l'on souhaite trier et dont on va créer toutes les config possibles étant donnée la taille imposée par grille
        # l'idée de la fonction est : 
        # - créer une liste de (m*n) ! grilles possibles 
        # - remplir ces grilles case par case (d'abord la case (0,0) de toutes les grilles, puis (0,1) ect ect 

        import copy
        #fonction auxilliaire pour ne pas avoir des grilles avec plusieurs fois le même nombre dedans 
        def est_present (grille_test, element) :
            for i in range (len(grille_test)) : 
                if (element in grille_test[i]) == True : 
                    return(True)
            return(False)
                
        #fonction auxilliaire pour ne pas avoir des 2 grilles pareilles dans la liste des grilles possibles 
        def existe_deja (liste, grille_candidate, nb_fois) :
            compteur = 0
            for element in liste : 
                if grille_candidate == element : 
                    compteur = compteur +1
                    if compteur == nb_fois :
                        return(True)
            return(False)
        
        #fonction auxilliaire pour avoir une idée du nombre de grilles que l'on construit pareil quand on remplit la case (0,0) (6) puis (0,1) (2) et (1,0) (1) et enfin (1,1) (1) dans le cas d'une matrice de taille 2*2
        # en effet, dans le case d'une matrice (2*2) il faut 6 grilles commençant par 4 en position (0,0), 6 commençant par 3 en (0,0) ect ect
        # ensuite quant on remplit la case (0,1), il nous faut 2 grilles avec 4 en (0,0) et 3 en (0,1), 2 grilles avec 4 en (0,0) et 2 en (0,1) ect ect 
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
            # nbb_fois renvoie une liste de nombre de grilles que l'on va devoir construire pareil selon où on en est du remplissage (case (0,0, case (0,1)...)
        
        #fonction auxilliaire : necessaire de 'retourner' la liste renvoyée par nbbfois qui est pour une matrice (2*2) [1,1,2,6] et pas [6,2,1,1]
        def retournement (liste) :
            correction = []
            for i in range (1, len(liste)+1) :
                correction.append(liste[-i])
            return(correction)

        #Création de l'outil factorielle : nécessire car il faut créer une liste de factorielle_matrices vides 
        factorielle = 1
        for i in range (1,grille.m * grille.n +1) :
            factorielle = i * factorielle

        # génération des (m*n)! grilles de taille (m,n) différentes que l'on va ensuite remplir
        liste = [[[0 for i in range (grille.m)] for j in range (grille.n)] for l in range (factorielle)] 
        
        ligne = 0
        colonne = 0 # pour se repérer dans le remplissage de la grille
        
        choix_possibles = []#création de la liste de nombres possibles pour constituer les grilles (nombres de 1 à m*n)
        for i in range (1,grille.n*grille.m+1) :
            choix_possibles.append(i)

        #remplissage des grilles possibles
        nombre_de_remplissage = grille.n*grille.m # nombre de fois où on met le nombre (cf descente de l'arbre de choix : 6 puis 2 et 1 et 1 dans le cadre d'une matrice 2*2)
        

        nb_foiss = retournement(nbb_fois(grille, factorielle))

        
        for case in range (grille.n*grille.m-1, -1, -1) : # il y a n*m cases dans la grille dont on envisage les configurations 
            numero_grille = 0
            diviseur = grille.n*grille.m
            #for i in range (factorielle) :
            for nombre in choix_possibles :
                compteur_occurence_nombre = 0 
                while compteur_occurence_nombre != int(factorielle/len(choix_possibles)) :
                    if (est_present(liste[numero_grille], nombre) == False) and (liste[numero_grille][ligne][colonne] ==0) : 
                        #2e condition nécessaire pour ne pas que le programme défasse ce qu'il a déjà fait
                        grille_candidate = [[0, 0], [0, 0]]
                        grille_candidate = copy.deepcopy(liste[numero_grille]) # on veut une copie de liste[numero_grille] sans lien entre les 2
                        grille_candidate[ligne][colonne] = nombre                        
                        if existe_deja (liste, grille_candidate, nb_foiss[case]) == False : 
                            liste[numero_grille][ligne][colonne] = nombre 
                            compteur_occurence_nombre = compteur_occurence_nombre +1
                    numero_grille = numero_grille + 1
                numero_grille = 0
          
            diviseur = diviseur *case

            #Pour passer à la case d'après
            colonne = colonne +1
            if colonne == grille.n : 
                colonne = 0
                ligne = ligne +1 
        return(liste)
  
            
    def creation_des_ponts (self, liste_grilles) : 
        import os
        liste_grilles = list(liste_grilles)
        
        def pont_possible (grille_1, grille_2) : #fonction auxilliaire qui renvoie si un pont entre deux états de la grille peut être construit (swap légal ou pas)
            for i in range (len(grille_1)) : #len(...) = nb de lignes de grille_1 
                for j in range (len(grille_1[0])) : # len(...) = nb_colonnes de grille_1
                    if grille_1[i][j] != grille_2[i][j] : # relève une différence
                        #cherche si le changement a été légal
                        if (j+1) < len(grille_1[0]) : 
                            if (grille_1[i][j] == grille_2[i][j+1]) : #necessaire de faire cette verif pour ne pas avoir de index out of range
                                return(True)
                            
                        elif (j-1) > 0 : 
                            if (grille_1[i][j] == grille_2[i][j-1]) : #necessaire de faire cette verif pour ne pas avoir de index out of range
                                return(True)
                            
                        elif (i-1) > 0 : 
                            if (grille_1[i][j] == grille_2[i-1][j]) : #necessaire de faire cette verif pour ne pas avoir de index out of range
                                return(True)
                            
                        elif (i+1) < len(grille_1) :
                            if (grille_1[i-1][j] == grille_2[i+1][j]) : #necessaire de faire cette verif pour ne pas avoir de index out of range
                                return(True)
                        else : 
                            return(False)

        liste_ponts = []   
          
        for grille in liste_grilles : 
            for grille_test in liste_grilles : 
                if grille_test != grille : # évacue le cas où on compare la grille avec elle-même
                    if pont_possible(grille, grille_test) == True : 
                        liste_ponts.append(str(liste_grilles.index(grille)) + " " + str(liste_grilles.index(grille_test)))
        
        #ecriture du fichier de retour (cf format attendu)
        fichier = open('nouveau.in', 'w', encoding='utf-8')
        fichier.write(str(len(liste_grilles))+" "+ str(len(liste_ponts)) +"\n") #ecriture nb grilles et nb ponts

        for element in liste_ponts : 
            fichier.write(str(element)+"\n")
        fichier.close()
        
        return(os.path.abspath('nouveau.in'))#le fichier s'appelle 'nouveau.txt'
        # renvoie la liste des ponts possibles entre les "noeuds" que sont les différentes grilles sous forme d'une liste 
        # l'index de chaque grille est le noeud qui lui correspond sur le graphe 
    
    
    def recherche_bonne_grille (self, liste_grille, grille_source) :
        liste_grille = list(liste_grille)
        for grille in (liste_grille) : 
            if grille_source == grille :
                return(liste_grille.index(grille))
    #renvoie la position de la grille voulu parmi l'ensemble des grilles possibles : c'est le numéro du noeud de départ sur le graphe

