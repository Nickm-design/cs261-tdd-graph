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
        return [node1, node2]
        
    def add_vertex(self, key):
        self.data[key] = []

    def remove_vertex(self, key):
        if self.empty():
            pass
    
    def add_edge(self, node1, node2):
        if self.empty():
            pass

    def empty(self):
        return self.data == {}

