fruits=["apple", "banana", "papaya", "pomegranate", "grapes"]

# fruits.remove("pomegranate")
# print(fruits)

#pop() removes specified index
fruits.pop(3)
print(fruits)
#to remove last items use pop()
print(fruits.pop())
del fruits[2]
print(fruits)

"""
clear() method empties the list.
but the list still remains,but has no content
"""