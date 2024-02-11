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
            self.nodes.append(node1)
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

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
        Trouve = False # On va faire la recherche tant que l'on n'a pas trouvé le noeud cible
        chemin = [] # A chaque noeud exploré on va le mettre dans le chemin parcouru
        if src != dst : #elimine le cas trivial ou arrivée = départ
            file = [src] # on commence le chemin avec le noeud source
            ajout = self.graph[src] # renvoie une liste de noeuds atteignables à partir du noeud source nommé src
            for noeud in ajout : 
                if (noeud in file) == False : # cela ne sert à rien de mettre deux fois un même noeud dans la liste de ceux à explorer
                    file.append(noeud)

            if dst in file == True :  
                Trouve = True 
                chemin.append(dst) # si, après avoir exploré le noeud source on a le noeud cible : fin de l'algo : on ajoute noeud cible au chemin 
                return(chemin, Trouve)
                
            for element in file :  # sinon, on boucle tant que dans la file il n'y a pas le noeud cible
                ajout = self.graph[element] # renvoie une liste de noeuds atteignables à partir du noeud nommé element, tiré de la file 
                for noeud in ajout : # ajout des noeuds atteignables à partir de element 
                    if (noeud in file) == False : 
                        file.append(noeud)
                chemin.append(element)# après exploration des noeuds adjacents à element on dit qu'on est passé par element en ajoutant element dans chemin
                if (dst in file) == True:  # si l'exploration de element a été concluante : on ajoute noeud destination à chemin et on renvoie chemin
                    Trouve = True 
                    chemin.append(dst)
                    return(chemin)
        else : # cas où destination = source : le chemin est égal à noeud source 
            return(chemin)
            
                


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
