#1If you do not know how many arguments will be passed into your function, add a * before the parameter name.
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

#2 combine regular parameter with *args 
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)
my_function("Hello", "Emil", "Tobias", "Linus")

#3A function that calculates the sum of any number of values:

def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total
print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

#4 Finding the maximum value:

def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num
print(my_function(3, 7, 2, 9, 1))


#If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")



def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)
my_function(name = "Tobias", age = 30, city = "Bergen")

#4 combine regular parameter with *kwargs 
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)
my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

# regualar parameter *ards **kwards 
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)
my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

