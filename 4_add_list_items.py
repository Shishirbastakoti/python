"""
To add items in a list use append()
"""

fruits=["apple", "banana", "papaya", "pomegranate", "grapes"]
fruits.append("durian")
print(fruits)

"""
use insert() to insert a list at a specified index.
"""
fruits.insert(4,"tomato")
print(fruits)

food=["soft drinks", "hard drinks", "rice", "curry"]
food.extend(fruits)
print(food)