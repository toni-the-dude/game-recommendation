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

  def user_menu(self):
    print("Here are the actions you can perform:\n1 - {}\n2 - {}\n3 - {}\n".format("View categories", "View games", "Search"))
    userChoice = input("Your choice: ")
    menu = {
        "1": self.print_tags,
        "2": self.print_games,
        "3": self.find_pattern,
        # "4": self.
    }
    try:
      menu[userChoice]()
    except KeyError:
      print("Invalid choice.")
  
  def find_pattern(self):
    arrayOfStrings = None
    whereToLook = None
    while True:
      whereToLook = input("You can search in:\n1 - {}\n2 - {}\n".format("Categories", "Games"))
      if whereToLook == "1": 
        arrayOfStrings = [tag.name for tag in self.tags]
        break
      elif whereToLook == "2":
        arrayOfStrings = [game.name for game in self.games]
        break
      print("Please choose one of the provided options.")
    pattern = input("Type in part of the word you are looking for:")
    displayIndex = 1
    compiledChoices = []
    for string in arrayOfStrings:
        if len(pattern) > len(string): continue
        index = 0
        for chr in string:
            if chr == pattern[index]:
                index += 1
            else:
                index = 0
            if index == len(pattern):
                print("{} - {}".format(displayIndex, string))
                compiledChoices.append(string)
                displayIndex += 1
                break
    userChoice = input("You may choose from the results above. Awaiting your input: ")
    userChoice = compiledChoices[int(userChoice) - 1]
    currentNode = None
    if whereToLook == "1":
      print("Here are games listed with the tag {}.".format(userChoice))
      for tag in self.tags:
        if tag.name == userChoice:
          currentNode = tag
      tag.get_edges() # Use try-except
    elif whereToLook == "2":
      for game in self.games:
        if game.name == userChoice:
          currentNode = game
      currentNode.print_details() # Use try-except
