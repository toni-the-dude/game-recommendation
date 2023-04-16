class Node: # Might be sufficient to build the entire program

  def __init__(self, name="Missing name", tags=[], description="No description", price="NA"): 
      self.name = name
      self.tags = tags
      self.description = description
      self.price = price
      self.edges = []
      if self.name[0] == '#':
        print("Created Node object '{}'. It represents a category.".format(self.name))
      else:
        print("Created Node object '{}'. It represents a game.".format(self.name))

  def __str__(self):
    # print("Overrode str method.")
    return self.name

  def get_edges(self): 
      print("Node {} has a total of {} edges. They lead to:".format(self.name, len(self.edges)))
      for edge in self.edges:
          print(edge)
  
  def print_details(self):
    print("On steam, {} has the following description:\n{}\nIt is listed at {}.\nThe game is tagged with: {}\n".format(self.name, self.description, self.price, self.tags))

class Graph:
  # Might be useful for navigating the menu
  def __init__(self): 
    self.games = []
    self.tags = []
    print("Created Graph object.")

#   def __contains__(self, node_name):
#     print("Succesfully overrode 'in' keyword.")
#     return any(node_name == tag.name for tag in self.tags)

  def add_vertex(self, vertex): 
    if vertex.name[0] == '#':
        self.tags.append(vertex)
    else:
        self.games.append(vertex)
    print("The games-side of the graph now looks as such:", [node.name for node in self.games])
    print("The category-side of the graph now looks as such:", [node.name for node in self.tags])

  def add_edges(self): # Looks amongst tag objects and appends them accordingly
      for game in self.games:
        print("Adding edges for {}...".format(game))
        for tag in game.tags:
            print("Checking existence of tag {}...".format(tag))
            for tagObj in self.tags:
                if tag == tagObj.name:
                    print("Correctly matched tag.")
                    game.edges.append(tagObj) # Append edge for game
                    tagObj.edges.append(game) # Append edge for tag too since it is undirected
                    break # Optimize
                else:
                    print("Still searching...")

  def print_games(self): 
    for game in self.games:
      print(game)

  def print_tags(self): 
    for tag in self.tags:
      print(tag)
#   def find_path(self, start_vertex, end_vertex): pass