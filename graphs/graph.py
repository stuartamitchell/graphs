__all__ = ['Graph']

class Graph:
    '''
    Class for representing simple graphs (loops allowed) with the following optional attibutes:
    - directed
    - colored nodes
    - colored edges 
    - weighted edges

    Colors and weights can be updated by setter functions.

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

        self.directed = directed
        
        if graph_data is None:
            self.nodes = {}            
        else:
            self.nodes = self.__read_graph_data(graph_data)
        
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

        if all(k in graph_data for k in ['directed', 'nodes']):
            self.directed = graph_data['directed']
            
            nodes = {}

            for node in graph_data['nodes']:
                nodes[node] = graph_data['nodes'][node]

            return nodes
        else:
            print('Cannot create graph from given input. Creating empty, undirected graph.')
            
            return {}

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

    def is_node(self, node):
        '''
        Checks if a nodes is in the graph or not

        Parameters
        ----------
        node : int
            the node to check

        Returns
        -------
        bool
            true if the node is in the graph, false otherwise
        '''

        if node in self.nodes:
            return True
        else:
            return False
    
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
        attr = { 'color': color, 'weight': weight} # note: this means when updating both adj dicts get updated

        if self.is_node(node1) and self.is_node(node2):
            self.nodes[node1]['adj'].update({ node2: attr })

            if not self.directed:
                self.nodes[node2]['adj'].update({ node1: attr })
        else:
            print('Cannot create edge between {} and {} as one of the nodes does not exist.'.format(node1, node2))
       
    def color_node(self, node, color):
        ''''
        Colors a node

        Prints error to console if node does not exist

        Paramters
        ---------
        node : int
            the node to be colored

        color : str
            the color of the node
        '''
        if self.is_node(node):
            self.nodes[node].update({ 'color': color })
        else:
            print('No node named {}'.format(node))

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

        if self.is_node(node1) and self.is_node(node2):
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

        if self.is_node(node1) and self.is_node(node2):
            self.nodes[node1]['adj'][node2].update({ 'weight': weight })
        else:
            print('Cannot add weight to edge ({}, {}) since it does not exist.'.format(node1, node2))

    def remove_edge(self, node1, node2):
        '''
        Removes an edge from the graph

        Prints error to console if edge does not exist.

        Parameters
        ----------
        node1 : int
            the first node of the edge

        node2 : int
            the second node of the edge
        '''

        if self.is_node(node1) and self.is_node(node2):
            del self.nodes[node1]['adj'][node2]

            if not self.directed:
                del self.nodes[node2]['adj'][node1]
        else:
            print('Cannote remove edge ({}, {}) since it does not exist.'.format(node1, node2))

    def remove_node(self, node):
        '''
        Removes a node from the graph

        Prints error to console if the node does not exist

        Parameters
        ----------
        node : int
            the node to be removed
        '''

        if self.is_node(node):
            del self.nodes[node]

            for n in self.nodes:
                del self.nodes[n]['adj'][node]
        else:
            print('Cannote remove a node {} as it does not exist.'.format(node))
