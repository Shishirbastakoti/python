#variable created outside the function is global variable

y="Wow!!"

def myfun():
  print(y+" this is the right way")
myfun()

x="dangerous"
def hello():
  x="lovely"
  print("Cobra is "+x)#in this case variable inside function i.e. local variable is executed
hello()

print("cobra is "+x)#in it global variable is executed

#to create global variable inside function we use GLOBAL(lowercase) keyword

def meow():
  global p   #create global variable inside function
  p="great"
meow()

print("Python is "+p)