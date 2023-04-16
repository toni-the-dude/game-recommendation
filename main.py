from graphs import *
from data import *

# Create graph
graph = Graph()
# Create & add games
for entry in gameData:
    graph.add_vertex(Node(entry[0], entry[1], entry[2], entry[3]))
# Create & add tags
for tag in tagData:
    graph.add_vertex(Node(tag))
# Add edges
graph.add_edges()
# game1.get_edges()

print("Browse games by category")
print("Here are the available categories:")
graph.print_tags()
currentNode = None

while(1):
    userChoice = input("What do you choose?\n")
    print("You chose... {}.".format(userChoice))
    for tag in graph.tags:
        if tag.name == userChoice:
            print("That is a valid choice!")
            currentNode = tag
            break
        else:
            print("Searching...")
    if currentNode != None:
        # print("Here are some games tagged with {}.".format(currentNode.name))
        currentNode.get_edges()
        print("Which one do you want to read more about?")
        userChoice = input()
        print("You chose... {}.".format(userChoice))
        for game in graph.games:
            if game.name == userChoice:
                print("That is a valid choice!")
                currentNode = game
                break
            else:
                print("Searching...")
    currentNode.print_details()
    # userChoice = input("If you want to explore similar games ")
    # print("See other games with similar tags...")