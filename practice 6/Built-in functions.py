#1Use map() and filter() on lists
nums = [1,2,3,4]
squares = list(map(lambda x: x**2, nums))
print(squares)

nums = [1,2,3,4,5,6]
even = list(filter(lambda x: x%2==0, nums))
print(even)

#2Aggregate with reduce() (from functools)
from functools import reduce

nums = [1,2,3,4]
sum_all = reduce(lambda a,b: a+b, nums)
print(sum_all) 

#3Use enumerate() and zip() for paired iteration
names = ["Ali", "Aruzhan", "Dana"]

for i, name in enumerate(names):
    print(i, name)
    
    
names = ["Ali","Dana"]
scores = [90,85]

for n, s in zip(names, scores):
    print(n, s)
#4Demonstrate type checking and conversions
x = "10"
print(type(x))
x = int(x)
print(type(x))