"""
It is used to store multiple items in a single variable.
Items are indexed as [0] for first, [1] for second and so on.

It is ordered and unchangeable.
-Ordered means items has defined order and that order will not change.

-Unchangeable means items in a tuple cannot be added, removed or changed.

It is written in round brackets.
"""

first_tuple=("hello", "world", "this", "is", "tuple")
print(first_tuple)

#printing class
print(type(first_tuple))

#tuple allows duplicate values
fruits=("apple", "banana", "durian", "apple", "grapes", "pomegranate")
print(fruits)
print(len(fruits))

#tuple with one item
one_tuple=("tuple",)
print(one_tuple)
"""
but this is not tuple
one_tuple=("tuple")
"""

#tuple can be any data types
anytuple=("this", "is", "tuple", 1, 2, 3, True, False)
print(anytuple)