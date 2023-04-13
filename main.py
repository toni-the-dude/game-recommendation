from graphs import *
from data import *
# Create tags
tag1 = Node(tagData[0])
tag2 = Node(tagData[1])
tag3 = Node(tagData[2])
# Test tags
print(tag1)
print(tag2)
print(tag3)
# Create games
game1 = Node(gameData[0][0], gameData[0][1], gameData[0][2], gameData[0][3])
# Test games
print(game1.name)
print(game1.tags)
print(game1.description)
print(game1.price)
# Create graph
graph = Graph()
graph.add_vertex(game1)
graph.add_vertex(tag1)
graph.add_vertex(tag2)
graph.add_vertex(tag3)
# Add edges
graph.add_edges()
game1.get_edges()