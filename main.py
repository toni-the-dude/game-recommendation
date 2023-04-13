from graphs import *
from data import *

game1 = Game(gameData[0][0], gameData[0][1], gameData[0][2], gameData[0][3])
print(game1.name)
print(game1.tags)
print(game1.description)
print(game1.price)

tag1 = Tag(tagData[0])
tag2 = Tag(tagData[1])
tag3 = Tag(tagData[2])
print(tag1.name)
print(tag2.name)
print(tag3.name)