class Node:
  # Unit of graph, contains information on a game  
  def __init__(self, name="Missing name", tags=[], description="No description", price="NA"): 
      self.name = name # May override how this gets printed
      self.tags = tags # These could be the edges
      self.description = description # May override how this gets printed
      self.price = price
      self.edges = []
      if self.name[0] == '#':
        print("Created Node object '{}'. It represents a category.".format(self.name))
      else:
        print("Created Node object '{}'. It represents a game.".format(self.name))
  def __str__(self):
    return self.name
  def add_edge(self, vertex): 
      self.edges.append(vertex)
  def get_edges(self): 
      for edge in self.edges:
          print(edge)

class Graph:
  # Here is where the games and tags will connect
  def __init__(self): 
    self.nodes = []
    print("Created Graph object.")
#   def __str__(self):
    # return self.nodes
  def add_vertex(self, vertex): 
    self.nodes.append(vertex)
    print("The graph now looks as such:", [node.name for node in self.nodes])
  def add_edge(self, from_vertex, to_vertex, weight = 0): pass
  def find_path(self, start_vertex, end_vertex): pass