class Solver(): 
    """
    A solver class, to be implemented.
    """
    def get_solution(self, grille):
        print(grille)
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        def case_cible (numero_cible) :
            nombre_de_colonnes = grille.m     
            if nombre_de_colonnes >= numero_cible : 
                ligne = 0
            elif 5// nombre_de_colonnes == numero_cible : 
                ligne = numero_cible -1
            else : 
                ligne = numero_cible//nombre_de_colonnes

            if 5%nombre_de_colonnes == 0 :  
                colonne = numero_cible%nombre_de_colonnes 
            else : 
                colonne = numero_cible%nombre_de_colonnes -1
            return((ligne,colonne))
            #Donne les coordonnées de l'objectif selon la taille de la matrice et le numéro que l'on souhaite placer

        def case_actuelle (numero_cible) : 
            i = 0
            j = 0
            while grille.state[i][j] != numero_cible : 
                j = j + 1
                if j > grille.m -1 : 
                    j = 0 
                    i = i +1
            return((i,j))
        """
        list_of_moves = [] 
        numero_cible = 1 
        A = case_actuelle(numero_cible)
        if A[1] < case_cible(numero_cible)[1] : 
            while A[0][1] < case_cible(numero_cible)[0][1] :
                grille.swap((A, A[0], A[1]+1))
        else : 
            while A[1] > case_cible(numero_cible)[1] :
                grille.swap((A), (A[0], A[1]-1))
        #Bonne colonne

        if A[0] < case_cible[0] : 
            while A[0] < case_cible[0] :
                grille.swap((A), (A[0]-1, A[1]))
        else : 
            while A[0] > case_cible[0] :
                grille.swap((A), (A[0]+1, A[1]))
            #Bonne ligne
        numero_cible = numero_cible +1
        """
        return(grille, numero_cible, case_actuelle)

