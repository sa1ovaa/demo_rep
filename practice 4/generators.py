#1
def square(a):
    for i in range(a):
        yield i**2
a = int(input())
print(list(square(a)))

b = int(input())
generat = (i**2 for i in range(b))
print(list(generat))
#2
def even_nums(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
n = int(input())
print(list(even_nums(n)))

#3
def divisible(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
listik = divisible(n)
for i in listik:
    print(i,end = " ")

#4
def square(a1,b1):
    for i in range(a1,b1+1):
        yield i**2
a1 = int(input())
b1 = int(input())
gen = square(a1,b1)
for i in gen:
    print(i,end=" ")

#5
n = int(input())
gen = (x for x in range(n,0,-1))
print(list(gen))

def nums(n1):
    for i in range(n1,0,-1):
        yield i
n1 = int(input())
print(list(nums(n1)))