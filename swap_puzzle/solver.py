class Solver(): 
    """
    A solver class, to be implemented.
    """
    from grid import Grid

    def get_solution(self):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        
        from grid import Grid
        compteur = 0
        list_of_moves = []
        while self.is_sorted() is False and compteur < m*n : 
            for i in range (self.n) :
                for j in range (self.m-1) :
                    if self.state[i][j] > self.state[i][j+1] : 
                        self.swap(self,(i,j),(i,j+1))
                        list_of_moves.append(((i,j),(i,j+1)))
            # On trie chacune des lignes dans l'ordre croissant : vrai si while se répète suffisamment de fois (m*n) au max ? 
            compteur = compteur + 1 

        compteur = 0 
        while self.is_sorted() is False and compteur < m*n :     
            for i in range (self.m) :
                for j in range (self.n) : 
                    if self.state[j][i] > self.state[j+1][i] :
                        self.swap(self,(j,i),(j,i+1))
                        list_of_moves.append(((i,j),(i,j+1)))
            compteur = compteur + 1
        
        return(list_of_moves, self)

