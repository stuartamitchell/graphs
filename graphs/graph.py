'''
Graph class for representing simple graphs with the following optional attibutes:
    - directed
    - colored nodes
    - colored edges 
    - weighted edges
'''

__all__ = ['Graph']

class Graph:
    '''
    '''

    def __init__(self, directed=False, graph_data=None):
        '''
        Initialises a (directed) graph with graph data

        Parameters
        ----------
        directed : bool (optional, default: False)
            Is the graph a directed graph? Default value is false.

        graph_data : dict (optional, default: None)
            A dictionary of graph data

        '''

        self.nodes = {}
        self.directed = directed
        
        if graph_data is None:
            self.graph = {}
        else:
            self.graph = self.__read_graph_data(graph_data)
        
    def __read_graph_data(self, graph_data):
        '''
        Read graph data supplied to constructor and produce our graph representation

        Paramaters
        ----------
        graph_data : dict
            a dictionary of graph data

        Returns
        -------
        graph
            a dictionary representing the graph
        '''
        graph = {}

        return graph

    def add_node(self, node, color=None):
        '''
        Adds a node to the graph with the supplied color

        Parameters
        ----------
        node : int
            the name of the node

        color : str (optional, default: None)
            the color of the node
        '''
        attr = { 'adj': {}, 'color': color }
        
        self.nodes[node] = attr
    
    def add_edge(self, node1, node2, color=None, weight=None):
        '''
        Adds an edge to the graph with the supplied color and weight.

        Prints error to console if a node does not exist

        Parameters
        ----------
        node1 : int
            the name of a node in the graph

        node2 : int
            the name of a node in the graph

        color : str (optional, default: None)
            the color of the edge
        
        weight : numerical (optional, default: None)
            the weight of the edge
        '''
        attr = { 'color': color, 'weight': weight}

        if all(key in self.nodes for key in [node1, node2]):
            self.nodes[node1]['adj'].update({ node2: attr })

            if not self.directed:
                self.nodes[node2]['adj'].update({ node1: attr })
        else:
            print('Cannot create edge between {} and {} as one of the nodes does not exist.'.format(node1, node2))
       
    def color_node(self, node, color):
        ''''
        Colors a node

        Paramters
        ---------
        node : int
            the node to be colored, throw exception if node doesn't exist

        color : str
            the color of the node
        '''
        try:
            self.nodes[node].update({ 'color': color })
        except KeyError as e:
            print('No node named {}'.format(e))

    def color_edge(self, node1, node2, color):
        '''
        Colors an edge

        Prints error to console if edge does not exist

        Parameters
        ----------
        node1 : int
            the first node of the edge

        node2 : int
            the second node of the edge

        color : str
            the color of the edge
        '''

        if all(key in self.nodes for key in [node1, node2]):
            self.nodes[node1]['adj'][node2].update({ 'color': color })
        else:
            print('Cannot color edge ({}, {}) since it does not exist.'.format(node1, node2))

    def weigh_edge(self, node1, node2, weight):
        '''
        Ads weight to an edge

        Prints error to console if edge does not exist

        Parameters
        ----------
        node1 : int
            the first node of the edge

        node2 : int
            the second node of the edge

        color : str
            the color of the edge
        '''

        if all(key in self.nodes for key in [node1, node2]):
            self.nodes[node1]['adj'][node2].update({ 'weight': weight })
        else:
            print('Cannot add weight to edge ({}, {}) since it does not exist.'.format(node1, node2))

    # TO DO: remove_node, remove_edge

if __name__ == '__main__':
    graph = Graph()
    
    graph.add_node(0)
    graph.add_node(1)
    print(graph.nodes)

    graph.add_edge(0,1)
    print(graph.nodes)

    graph.color_edge(0, 1, 'blue')
    graph.color_edge(0, 2, 'red')
    print(graph.nodes)

    graph.weigh_edge(0, 1, '17.0')
    graph.weigh_edge(0, 2, '12')
    print(graph.nodes)
        

