#1 example of using function
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#2 A function that returns a value:
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)


#3 Using the return value directly:
def get_greeting():
  return "Hello from a function"

print(get_greeting())
