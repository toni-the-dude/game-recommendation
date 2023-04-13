class Game:
  # Unit of graph, contains information on a game  
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
  # Unit of graph, contains information on a category of game
  def __init__(self, tagName=""): 
      self.tagName = tagName
      self.edges = []
  def add_edge(self, vertex): 
      Game.add_edge(self, vertex)
  def get_edges(self): 
      Game.get_edges(self)

class Graph:
  # Here is where the games and tags will connect
  def __init__(self): pass
  def add_vertex(self, vertex): pass
  def add_edge(self, from_vertex, to_vertex, weight = 0): pass
  def find_path(self, start_vertex, end_vertex): pass