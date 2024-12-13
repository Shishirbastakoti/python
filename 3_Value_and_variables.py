"""
      Most value is evaluated TRUE except it is empty values, 0.
"""
print(bool("human resource")) #it gives boolean value TRUE as it contains something inside paranthesis 
print(bool()) #it returns FALSE boolean value as it is empty inside paranthesis

print(bool("object"))
print(bool(print))
print(bool(345))
print(bool(["hero", "honda","boolean"]))
print(bool((1,2,3,4,5,6)))

print(bool(()))
print(bool([]))
print(bool((0)))
print(bool({}))

# function can return boolean
def my_function():
  return True
print(my_function())