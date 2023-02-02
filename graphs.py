class Game:
  """Key methods of Vertex class"""
  def __init__(self, title="", tags=[], description=""): 
      self.title = title
      self.tags = tags
      self.description = description
      self.edges = []
  def add_edge(self, vertex): 
      self.edges.append(vertex)
  def get_edges(self): 
      for edge in self.edges:
          print(edge)

class Tag:
  """Key methods of Vertex class"""
  def __init__(self, tagName=""): 
      self.tagName = tagName
      self.edges = []
  def add_edge(self, vertex): 
      Game.add_edge(self, vertex)
  def get_edges(self): 
      Game.get_edges(self)

class Graph:
  """Key methods of Graph class"""
  def __init__(self): pass
  def add_vertex(self, vertex): pass
  def add_edge(self, from_vertex, to_vertex, weight = 0): pass
  def find_path(self, start_vertex, end_vertex): pass
