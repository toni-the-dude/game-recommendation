from graphs import *
from data import *

game1 = Node(gameData[0][0], gameData[0][1], gameData[0][2], gameData[0][3])
print(game1.name)
print(game1.tags)
print(game1.description)
print(game1.price)

tag1 = Node(tagData[0])
tag2 = Node(tagData[1])
tag3 = Node(tagData[2])
print(tag1.name)
print(tag2.name)
print(tag3.name)