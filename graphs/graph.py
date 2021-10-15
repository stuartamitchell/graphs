class Graph:
    '''
    A class to represent a graph - directed or undirected, weighted or unweighted
    '''
    def __init__(
            self, adj_mat=None, edges=None, directed=False, weighted=False, sparse=True):
        self.directed = directed
        self.weighted = weighted
        self.graph = None

        if edges and sparse:
            self.graph = self.__sparse_from_edges(edges)

    def __get_nodes(self, edges):
        '''
        Gets a list of the nodes from a list of edges

        Parameters
        ----------
        edges : list
            a list of the edges in the graph

        Returns
        -------
        list
            a list of the nodes in the graph
        '''
        first = [edge[0] for edge in edges]
        second = [edge[1] for edge in edges]

        return sorted(set(first + second))

    def __sparse_from_edges(self, edges):
        '''
        Creates the graph as a dictionary of nodes and their
        neighbours

        Parameters
        ----------
        edges : list
            a list of the edges in the graph

        Returns
        -------
        dict
            a dictionary keyed by the nodes of the graph whose
            values are the node's neighbours
        '''

        nodes = self.__get_nodes(edges)

        graph = {}

        # create an empty dictionary of all the nodes
        for node in nodes:
            graph[node] = []

        if self.weighted:
            for node1, node2, weight in edges:
                graph[node1].append((node2, weight))

                if not self.directed:
                    graph[node2].append((node1, weight))
        else:
            for node1, node2 in edges:
                graph[node1].append(node2)

                # if not a directed graph and the edge isn't a loop
                if not self.directed and node1 != node2:
                    graph[node2].append(node1)

        return graph

    def __dense_from_edges(self, edges):
        '''
        Creates the graph as an adjacency matrix
        '''

if __name__ == '__main__':
    edges = [(1,2), (3,1), (2,2), (4,1)]
    graph_edges = Graph(edges=edges)
    graph_edges_directed = Graph(edges=edges, directed=True)
    print(graph_edges.graph)
    print(graph_edges_directed.graph)

