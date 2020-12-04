# Graph: An efficient graph.
# A graph implementation that uses an adjacency list to represent vertices
# and edges.
# Your implementation should pass the tests in test_graph.py.
# Nick Morris

import functools

class Graph:

    def __init__(self):
        self.data = {}
    
    def adjacent(self, node1, node2):
        return self.data
    
    def neighbors(self, node1=None, node2=None):
        if self.empty():
            return []
    
    def empty(self):
        return self.data == {}

