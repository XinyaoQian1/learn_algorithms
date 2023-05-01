"""
# @File    :    Graph.py
# @Time    :    29/04/2023 22:20
# @Author  :    Xinyao Qian
# @Description: 
"""
from collections import deque


class Graph:
    def __init__(self, directed=False):
        self.graph_dict = {}
        self.directed = directed


    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:  # if is bidirectional
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)
        print(f'Adding edge from {from_vertex.value} to {to_vertex.value}')

    def print_graph(self):
        print('------------------------')
        print('Graph adjacent list')
        for val, vertex in self.graph_dict.items():
            print(f' {val} -> {vertex.get_edges()}')
        print('------------------------')

    def find_path(self, start_vertex_val, end_vertex_val):
        print('Finding path')
        queue = deque([start_vertex_val])
        visited = set(start_vertex_val)
        while queue:
            current_vertex_val = queue.popleft()
            if current_vertex_val == end_vertex_val:
                # this assumes that the vertex value is unique.
                print('Found path')
                return True
            vertex = self.graph_dict[current_vertex_val]
            for next_vertex in vertex.get_edges():
                if next_vertex in visited:
                    # circle found
                    print("circle!")
                    continue

                queue.append(next_vertex)
                visited.add(next_vertex)

        return False
