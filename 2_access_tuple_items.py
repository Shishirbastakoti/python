"""
Tuples items can be accessed by index number, inside square brackets.
"""

fruits=("apple", "banana", "durian", "grapes", "pomegranate")
print(fruits[3])

#negative indexing
print(fruits[-1])

#printing range of indexes
print(fruits[3:4])

#printing items from beginning
print(fruits[:4]) #[4] is not included

#printing items upto end
print(fruits[3:])

#range of negative indexes
print(fruits[-4:-1])

#check if any item exists in tuple
if "apple" in fruits:
  print("Sweet!, apple is here.")