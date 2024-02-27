from grid import Grid
from solver import Solver
from graph import Graph 
import matplotlib.pyplot as plt

data_path = "/workspaces/projet_info/input/"
file_name = data_path + "grid1.in"




g = Grid.grid_from_file(file_name) # test avec l'input grid0.in


#RESOLUTION DE LA GRILLE
s = Solver()
print(s.get_solution(g)) 

#REPRESENTATION GRAPHIQUE GRILLE
a = Grid(1,1)
a.afficher_grille(g) # test de la représentation graphique d'une grille appliquée à g







#BFS AVEC ENTRÉES NOEUDS D'UN GRAPHE
graph2 = Graph.graph_from_file(data_path + "graph2.in")
print(graph2.bfs(2,10), 'resultats 1')






#APPLICATION DU BFS AU PROBLEME DU SWAP_PUZZLE
# NE FONCTIONNE PAS SI G N'EST PAS CARREE
import os # pour lire le chemin d'accès au fichier crée par chemins possibles
import shutil # pour déplacer le fichier crée par chemins possibles
auxilliaire_1 = Grid(2,2)
liste_grilles_possibles = auxilliaire_1.creation_grilles_possibles(g) # renvoie liste grilles construites à partir de g, matrice de taille 2*2 (cf grid0)
print(liste_grilles_possibles)



graph_produit = Grid(2,2)
noeud_grille_source = Grid(2,2) 
noeud_grille_cible = Grid(2,2)

source = noeud_grille_source.recherche_bonne_grille(liste_grilles_possibles, [[4, 3, 2, 1]] )# noeud grille source = index de grille source dans liste grilles
cible = noeud_grille_cible.recherche_bonne_grille(liste_grilles_possibles, [[1, 4, 3, 2]] )# noeud grille cible = index de grille cible dans liste grilles
#Double crochets indispensables : ce sont des grilles de 1 ligne 
print(source, cible)

#CI DESSUS FONCTIONNE POUR TOUTE TAILLE DE MATRICE

# on va ranger ce fichier au bon endroit
destination_path = "/workspaces/projet_info/input/"
shutil.move(str(graph_produit.creation_des_ponts(liste_grilles_possibles)), destination_path) # déménage le fichier avec le fichier de la liste des ponts entre les noeuds
# LE BON NOMBRE DE PONTS EST CREE   
graph1 = Graph.graph_from_file(destination_path +'nouveau.in') # crée un objet de la classe graph (sur lequel appliquer le bfs) à partir du fichier crée plus haut avec l'ensemble des ponts possibles entre les différents états d'une matrice de taille 2*2


print(graph1.bfs(source,cible), 'resultats 2')# applique le bfs à ce fichier et renvoie le chemin pour aller de noeud source à noeud cible


os.remove("/workspaces/projet_info/input/nouveau.in")# supprime le fichier généré et appelé 'nouveau.in' qui n'est plus utile 




# BUT : AJOUTER UN CONTROLE DE DIFFICULTE AVEC EN ENTREE L'ELOIGNEMENT MINIMAL (BFS) ET LA TAILLE DE LA MATRICE 

destination_path = "/workspaces/projet_info/input/"
auxilliaire = Grid(1,1)

acces_difficulte = destination_path + "difficulte_control.in"

print(auxilliaire.difficulte_control(acces_difficulte))




#TEST DE A*



#INTERFACE GRAPHIQUE UTILISATION PYGAME
