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