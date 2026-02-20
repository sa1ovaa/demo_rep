# 1. Generator to yield squares up to n
def squares_up_to(n):
    for i in range(n + 1):
        yield i * i

n = int(input())
print(",".join(str(x) for x in squares_up_to(n) if x % 2 == 0))

# 2. Generator for numbers divisible by 3 and 4
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for num in divisible_by_3_and_4(n):
    print(num, end=" ")
print()

# 3. Generator to yield squares from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a, b = map(int, input().split())
for val in squares(a, b):
    print(val, end=" ")
print()

# 4. Generator to yield numbers from n down to 0
def countdown(n):
    for i in range(n, -1, -1):
        yield i

for val in countdown(n):
    print(val, end=" ")
print()
