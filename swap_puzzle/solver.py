class Solver(): 
    """
    A solver class, to be implemented.
    """
    def get_solution(self, grille):
        def case_cible (numero_cible) :
            nombre_de_colonnes = grille.n   
            if nombre_de_colonnes >= numero_cible : 
                ligne = 0
            #cas ou num_cible va à la premiere ligne
            elif numero_cible % nombre_de_colonnes != 0 : 
                ligne = numero_cible//nombre_de_colonnes 
            #cas ou num_cible va entre la 2e et l'avant derniere ligne
            else : 
                ligne = numero_cible//nombre_de_colonnes -1
            #cas ou le num_cible = nb_colonnes * entier : le num cible va a la derniere ligne

            if numero_cible%nombre_de_colonnes == 0 :  
                colonne = nombre_de_colonnes -1
            else : 
                colonne = numero_cible%nombre_de_colonnes -1
            
            return((ligne,colonne))
            #Donne les coordonnées de la case objectif selon la taille de la matrice et le numéro que l'on souhaite placer

        def case_actuelle (numero_cible) : 
            i = 0
            j = 0
            while grille.state[i][j] != numero_cible : 
                j = j + 1
                if j > grille.n -1 : 
                    j = 0 
                    i = i +1
            return((i,j))
       

        
        list_of_moves = [] 
        numero_cible = 1
        
        for i in range (1, grille.m*grille.n+1): 
            A = case_actuelle(numero_cible) # A = case actuelle 

            if A[0] < case_cible(numero_cible)[0] : 
                while A[0] < case_cible(numero_cible)[0] :
                    grille.swap((A), (A[0]+1, A[1]))
                    list_of_moves.append((A,(A[0]+1, A[1])))
                    A = case_actuelle(numero_cible) #Maj de la case actuelle numéro cible
            else : 
                while A[0] > case_cible(numero_cible)[0] :
                    grille.swap((A), (A[0]-1, A[1]))
                    list_of_moves.append((A,(A[0]-1, A[1])))
                    A = case_actuelle(numero_cible) # Maj de la case actuelle numéro cible
                #Bonne ligne
            #Necessaire de commencer par les lignes pour ne pas 'déranger' la grille déjà rangée

            if A[1] < case_cible(numero_cible)[1] : 
                while A[1] < case_cible(numero_cible)[1] :
                    grille.swap((A), (A[0], A[1]+1))
                    list_of_moves.append((A,(A[0], A[1]+1)))
                    A = case_actuelle(numero_cible)
            else : 
                while A[1] > case_cible(numero_cible)[1] :
                    grille.swap((A), (A[0], A[1]-1))
                    list_of_moves.append((A,(A[0], A[1]-1)))
                    A = case_actuelle(numero_cible)
            #Bonne colonne

            numero_cible = numero_cible +1
        
        return(list_of_moves, grille) #bizarrement : n'affiche pas la matrice explicitement quand mis avec la liste des moves

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
                ax.text(x, y, f"{grille.state[i][j]}", ha='center', va='center', fontsize=12)# positionnement des chiffres dans la bonne case de la grille (x,y), choix de la taille de la police et du centrage du chiffre



        plt.show()
        
