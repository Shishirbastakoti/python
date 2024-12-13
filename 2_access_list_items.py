books=["physics", "mathematics", "chemistry", "english", "nepali"]
print(books[2]) # prints item number 2 present in a list

"""
negative indexing: 
It starts from end and last item is indexed as -1 and so on.
"""
print(books[-1])

# printing a range
print(books[1:4]) #1 is included and 4 is not included

print(books[:3]) #prints item from start to item 3
print(books[0:]) # prints item from 0 to end(last)

print(books[-4:-2])

if "physics" in books:
  print("Yes, physics is a book")
  