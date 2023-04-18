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
# game1.get_edges() # Testing

print("Browse games by category")

while(1):
    graph.user_menu()