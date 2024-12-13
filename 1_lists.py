"""
list is used to store multiple items in a single variable.
 It is one of the built in data types.It is created using square brakets.

 Lists items are indexed as [0] just like in arrays.
"""

#creating a list
fruits=["apple", "orange", "banana", "kiwi", "grapes"]
print(fruits) #prints items in list

#list length
print(len(fruits))  #prints number of items in a list

# a list can contain any data types
detail=["ram", "is", 29, "years", "old",True,"man"]
print(detail)
print(len(detail))
print(type(detail))

food=list(("basmati","jeera masina", "anadi",))
print(food)