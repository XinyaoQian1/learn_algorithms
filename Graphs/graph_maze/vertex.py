"""
# @File    :    vertex.py
# @Time    :    30/04/2023 23:09
# @Author  :    Xinyao Qian
# @Description: 
"""
class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, adjacent_value, weight = 0):
    self.edges[adjacent_value] = weight

  def get_edges(self):
    return self.edges.keys()
