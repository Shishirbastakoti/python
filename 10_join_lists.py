
"""
it joins or merges a list.
"""
fruits=["apple", "banana", "papaya", "pomegranate", "grapes"]
food=["soft drinks", "hard drinks", "rice", "curry"]
foods=fruits+food
print(foods)

number=[34, 56, 23, 3, 87]
alphanum=fruits+number
print(alphanum)

#extend() can be used
food.extend(fruits)
print(food)