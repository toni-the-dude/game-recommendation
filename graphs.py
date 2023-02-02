class Vertex:
  """Key methods of Vertex class"""
  def __init__(self, value): pass
  def add_edge(self, vertex, weight = 0): pass
  def get_edges(self): pass

class Graph:
  """Key methods of Graph class"""
  def __init__(self, directed = False): pass
  def add_vertex(self, vertex): pass
  def add_edge(self, from_vertex, to_vertex, weight = 0): pass
  def find_path(self, start_vertex, end_vertex): pass
