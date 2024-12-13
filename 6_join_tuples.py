"""
Two or more tuples can be joined together using '+' operator
"""

fruits=("apple", "banana", "grapes", "pomegranate")
food=("rice", "noodles", "momo", "pepsi")
foods=fruits+food

number=(1, 2, 3, 4, 5)
alphanum=fruits+number    #first prints fruits then number in same tuple
print(alphanum)
print(foods)

#multiply tuples
numbers=2*number #repeat the tuple items in same order in same tuple
print(numbers)