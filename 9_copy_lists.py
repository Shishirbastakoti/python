"""
we cannot copy lists by list1=list2.
If any changes is made in list1, the change will also be seen in list2.
"""

#using copy() function

fruits=["apple", "banana", "papaya", "pomegranate", "grapes"]
myfruits=fruits.copy()
# print(myfruits)

#can also be copied by using built-in list() function
yesfruits=list(fruits)
print(yesfruits)

#copy by the use of slice operator
theirfruits=fruits[:]
print(theirfruits)

