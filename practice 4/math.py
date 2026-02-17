#1
import math
a = int(input())
print(math.radians(a))

#2 
height = 5
first_value = 5
second_value = 6
print("area: ",((first_value + second_value)/2)*height)

#3
import math
number_sides = 4
length_side = 25
perim = number_sides * length_side
apothem = length_side / (2 * math.tan(math.radians(180 / number_sides)))
area = (perim * apothem) / 2
print(int(area))

#4
l = 5
h = 6
print(float(l * h))