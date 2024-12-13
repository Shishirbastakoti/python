"""
Tuple cannot be updated or changed directly as it immutable.
We can first convert tuple into lists and make changes then can be converted into tuple again. 
"""

fruits=("apple", "banana", "durian", "grapes", "pomegranate")
x=list(fruits)
print(x)

x[1]="kiwi" #change the value of item in index[0]
fruits=tuple(x)
print(fruits)

#adding items
y=list(fruits)
y.append("pineapple")
fruits=tuple(y)
print(fruits)

#two tuple can be added to one tuple
fruits=("apple", "banana", "durian", "grapes", "pomegranate")
fruit=("lemon", "oranges", "watermelon")
fruiit=fruits+fruit
print(fruiit)

#removing items from tuple
z=list(fruiit)
z.remove("watermelon")
fruiit=tuple(z)
print(fruiit)
