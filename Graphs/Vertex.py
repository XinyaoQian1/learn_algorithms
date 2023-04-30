"""
# @File    :    Vertex.py
# @Time    :    29/04/2023 22:21
# @Author  :    Xinyao Qian
# @Description: 
"""


class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight

    def get_edges(self):
        return list(self.edges.keys())
