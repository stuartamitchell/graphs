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

        Parameters
        ----------
        node1 : int
            the name of a node in the graph, created if not in graph

        node2 : int
            the name of a node in the graph, created if not in graph

        color : str (optional, default: None)
            the color of the edge
        
        weight : numerical (optional, default: None)
            the weight of the edge
        '''
        attr = { 'color': color, 'weight': weight}

        if node1 not in self.nodes.keys():
            self.add_node(node1)

        if node2 not in self.nodes.keys():
            self.add_node(node2)
        
        self.nodes[node1]['adj'].update({ node2: attr })

        if not self.directed:
            self.nodes[node2]['adj'].update({ node1: attr })
    
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

        Parameters
        ----------
        node1 : int
            the first node of the edge

        node2 : int
            the second node of the edge

        color : str
            the color of the edge
        '''



if __name__ == '__main__':
    graph = Graph()
    
    graph.add_node(0)
    print(graph.nodes)

    graph.color_node(1, 'green')

    graph.add_edge(0,1,'blue', 17.0)
    graph.add_edge(0,2)

    graph.color_node(0, 'blue')
    graph.color_node(1, 'red')

    print(graph.nodes)

    graph.color_node(1, 'green')

    print(graph.nodes)
        

