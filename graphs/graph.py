class Graph:
    '''
    A class to represent a graph - directed or undirected, weighted or unweighted
    '''
    def __init__(self, adjacency_matrix=None, edges=None, directed=False, weighted=False):
        self.directed = directed
        self.weighted = weighted
        self.adjacency_matrix = adjacency_matrix
        self.edges = edges

        self.graph = {}

        if edges:
            self.graph = self.__build_from_edges(edges)

    def __build_from_edges(self,edges):
        ''''''
            

    def add(self, node1, node2):
        ''''''

        