class Node: # Will either contain game data or tag data. In the latter case, only 2 attributes get used

  def __init__(self, name="Missing name", tags=[], description="No description", price="NA"): 
      self.name = name               # String
      self.tags = tags               # Array of strings
      self.description = description # String
      self.price = price             # String
      self.edges = []                # Array of Node objects
      # if self.name[0] == '#': # Distinguish games from tags based on .name attribute (for testing purposes)
      #   print("Created Node object '{}'. It represents a category.".format(self.name))
      # else:
      #   print("Created Node object '{}'. It represents a game.".format(self.name))

  def __str__(self): # Used exclusively for presentation & testing
    # print("Overrode str method.") # Testing
    return self.name

  def get_edges(self): 
      # print("Node {} has a total of {} edges. They lead to:".format(self.name, len(self.edges))) # Testing
      for edge in self.edges:
          print(edge)
  
  def print_details(self):
    print("On steam, {} has the following description:\n{}\nIt is listed at {}.\nThe game is tagged with: {}\n".format(self.name, self.description, self.price, self.tags))

class Graph: # Connects Nodes. Tags can be connected to any number of games, but not to other tags directly. Likewise, games can be connected to any number of tags, but not to other games directly.

  def __init__(self): 
    self.games = [] # Array of Node objects
    self.tags = []  # Array of Node objects
    # print("Created Graph object.") # Testing

#   def __contains__(self, node_name): # Faulty
#     print("Succesfully overrode 'in' keyword.")
#     return any(node_name == tag.name for tag in self.tags)

  def add_vertex(self, vertex): # Distinguish games from tags based on .name attribute
    if vertex.name[0] == '#':
        self.tags.append(vertex)
    else:
        self.games.append(vertex)
    # print("The games-side of the graph now looks as such:", [node.name for node in self.games]) # Testing
    # print("The category-side of the graph now looks as such:", [node.name for node in self.tags]) # Testing

  def add_edges(self): # Connects all Nodes based on game objects' .tags attribute
      for game in self.games:
        # print("Adding edges for {}...".format(game)) # Testing
        for tag in game.tags:
            # print("Checking existence of tag {}...".format(tag)) # Testing
            for tagObj in self.tags:
                if tag == tagObj.name:
                    # print("Correctly matched tag.") # Testing
                    game.edges.append(tagObj) # Append edge for game
                    tagObj.edges.append(game) # Append edge for tag too since the graph is undirected
                    break # Optimize
                # else: # Testing
                #     print("Still searching...") # Testing

  def print_games(self): # Prints game names
    for game in self.games:
      print(game) 

  def print_tags(self): # Prints tag names
    for tag in self.tags:
      print(tag)

  def user_menu(self): 
    print("Here are the actions you can perform:\n1 - {}\n2 - {}\n3 - {}\n".format("View categories", "View games", "Search"))
    userChoice = input("Your choice: ")
    menu = {
        "1": self.print_tags,
        "2": self.print_games,
        "3": self.find_pattern, # See below
    }
    try:
      menu[userChoice]()
    except KeyError:
      print("Invalid choice.")
  
  def find_pattern(self): # Naive pattern search
    ### Determine where to look
    arrayOfStrings = None # Array of strings containing either tag or game names
    whereToLook = None    # Holds 1 if we are searching in tags, 2 if in games
    while True:
      whereToLook = input("You can search in:\n1 - {}\n2 - {}\n".format("Categories", "Games"))
      if whereToLook == "1": 
        arrayOfStrings = [tag.name for tag in self.tags]
        break
      elif whereToLook == "2":
        arrayOfStrings = [game.name for game in self.games]
        break
      print("Please choose one of the provided options.")
    ### Determine pattern
    pattern = input("Type in part of the word you are looking for:")
    pattern = pattern.lower() # Working with lower characters so that results are not case-sensitive
    displayIndex = 1 # Used to index displayed options
    compiledChoices = [] # Array of strings
    try:
      for string in arrayOfStrings:
          if len(pattern) > len(string): continue
          index = 0
          for chr in string.lower():
              if chr == pattern[index]:
                  index += 1
              else:
                  index = 0
              if index == len(pattern):
                  print("{} - {}".format(displayIndex, string))
                  compiledChoices.append(string)
                  displayIndex += 1
                  break
    except IndexError:
      print("Either the pattern has no matches, or an error has occurred.")
      return
    ### Choosing an option from results
    ## Validation
    try:
      userChoice = input("You may choose from the results above. Awaiting your input: ")
      userChoice = compiledChoices[abs(int(userChoice)) - 1]
    except IndexError:
      print("Index not found. Did you make sure to choose one from the presented list?")
      return
    currentNode = None # Holds Node object
    ## Distinction
    if whereToLook == "1": # We are dealing with tags
      print("Here are games listed with the tag {}.".format(userChoice))
      for tag in self.tags:
        if tag.name == userChoice:
          currentNode = tag
        # print(currentNode) # Testing
      currentNode.get_edges() # Prints names of games with matching tag
    elif whereToLook == "2": # We are dealing with games
      for game in self.games:
        if game.name == userChoice:
          currentNode = game
      currentNode.print_details() # Prints all available details of a game
      ### Implement suggestion system
      print("See games with similar tags:")
      suggestions = [] # Array of (game Node, tag Node) tuples
      for tag in currentNode.edges:
        for game in tag.edges:
          if game not in suggestions and game is not currentNode:
            suggestions.append((game, tag))
      displayIndex = 1
      for su in suggestions:
        print("{} - {} (matched on at least 1 tag: {})".format(displayIndex, su[0].name, su[1].name))
        displayIndex += 1
