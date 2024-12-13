"""
sort() function sorts items in a list alphanumerically.
"""
#alphabetically
fruits=["apple", "banana", "papaya", "pomegranate", "grapes"]
fruits.sort()
print(fruits)

#numerically
number=[34, 56, 23, 3, 87]
number.sort()
print(number)

#sort descending
fruits.sort(reverse=True)
print(fruits)

number.sort(reverse=True)
print(number)

#sorting in reverse order
fruits.reverse()
print(fruits)

number.reverse()
print(number)