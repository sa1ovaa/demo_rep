#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the actual value that is sent to the function when it is called.
#def my_function(name): # name is a parameter
  #print("Hello", name)
#my_function("Emil") # "Emil" is an argument

# default parameter
def my_function(country = "Norway"):
  print("I am from", country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#2 keyword argument 
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function(animal = "dog", name = "Buddy")


#3 Sending a dictionary as an argument:
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])
my_person = {"name": "Emil", "age": 25}
my_function(my_person)


#4 To specify positional-only arguments, add , / after the arguments:
def my_function(name, /):
  print("Hello", name)
my_function("Emil")


# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
def my_function(name):
  print("Hello", name)
my_function(name = "Emil")

#5 To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, name):
  print("Hello", name)
my_function(name = "Emil")

#Without *,, you are allowed to use positional arguments even if the function expects keyword arguments:
def my_function(name):
  print("Hello", name)
my_function("Emil")