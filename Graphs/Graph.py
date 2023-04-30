"""
# @File    :    Graph.py
# @Time    :    29/04/2023 22:20
# @Author  :    Xinyao Qian
# @Description: 
"""


class Graph:
    def __init__(self, directed=False):
        self.graph_dict = {}
        self.directed = directed

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:  # if is bidirectional
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value,weight)
        print(f'Adding edge from {from_vertex.value} to {to_vertex.value}')
