from graphs import *
from data import *
# Define functions


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
# currentNode = None

while(1):
    graph.user_menu()
    # userChoice = input("If you want to explore similar games ")
    # print("See other games with similar tags...")