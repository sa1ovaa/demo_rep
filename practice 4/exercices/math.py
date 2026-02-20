import math

# 1. Degree to Radian
degree = float(input("Input degree: "))
radian = degree * (math.pi / 180)
print("Output radian:", round(radian, 6))

# 2. Area of a Trapezoid
h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))
trapezoid_area = 0.5 * (a + b) * h
print("Expected Output:", trapezoid_area)

# 3. Area of Regular Polygon
n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
polygon_area = (n * s ** 2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", polygon_area)

# 4. Area of Parallelogram
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
parallelogram_area = base * height
print("Expected Output:", parallelogram_area)
