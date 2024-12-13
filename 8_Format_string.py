# string formatting is done to add number and string in a single line
"""
we cannot combine string and numbers like this

distance=55
result="The distance to school from my home is"+ distance+" km."
print(result)

"""

"""
rather we prefer F-Strings for string formatting

It can be done as:
"""

distance=55
statement=f"The distance to school from my home is {distance} km."
print(statement)

"""
By using f before literal of string we can add braces {} as placeholder.

This method is useful to add integer to different data type
"""

"""
placeholder and modifiers

modifiers can be added by colon(:)

The example is given as:
"""

length=5
line=f"The length of a metal plate is {length:.3f} meters"
print(line)

"""
In the above example .3f represents the floating type having precision
value of three digits
"""

"""
It is also possible to perform mathematical calculation inside placeholder {}
"""

prize_money=f"The prize money of winning the code marathon is {100*134} rupees."
print(prize_money)