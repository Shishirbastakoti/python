"""
It offers a shorter syntax when you want to create a new list based in the values is an existing list.
"""

fruits=["apple", "banana", "papaya", "pomegranate", "grapes"]

newlist=[x for x in fruits if "a in x"]
print(newlist)

new1=[y for y in fruits if "g" in y]    #prints items in list which have g in them
print(new1)