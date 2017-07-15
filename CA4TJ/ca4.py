
import math

# Addition

add = lambda x,y: x+y

x = (2, 2, -2, 2, 3, 0.5)
y = (2, 4, 2, -2, 0, 0.5)
adding = map(add, x, y)
print adding
print round(add(2/4.0, 2/6.0), 4)

# Addition by reduce function

addbyred = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print addbyred

# Addition by mapping 3 sets

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [-2, -4, -6, -8]

map (lambda x, y, z: x + y + z, a, b, c)
print map (lambda x, y, z: x + y + z, a, b, c)


# Subtraction

subtract = lambda x,y: x-y

x = (2, 3, 2, -2, -2, 0.5)
y = (2, 2, 3, -3, 2,  0.2)
sub = map(subtract, x, y)
print sub 
print round(subtract(2/4.0, 2/6.0), 4) 

# Subtraction by reduce function

subbyred = reduce(lambda x, y: x - y, [1, 2, 3, 4])
print subbyred

# Subtraction by mapping 3 sets
map (lambda x, y, z: x + y - z, a, b, c)
print map (lambda x, y, z: x + y - z, a, b, c)


# Multiplication

multiply = lambda x,y: x*y
x = (2, 0, 2, -2, 2, -2, 0.5)
y = (2, 2, 0, 0, -2, -2, 0.5)
mult = map(multiply, x, y)
print mult
print round(multiply(2/4.0, 2/6.0), 4)

# Multiplication by reduce function

multbyred = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print multbyred

# Multiplication by mapping 3 sets

map (lambda x, y, z: x * y * z, a, b, c)
print map (lambda x, y, z: x * y * z, a, b, c)


# Division

def divide(x, y):
	if y == 0:
		print "Can't divide by zero"
	else:
		return x/y

x = (6, -6, 2, 16, 0, 4)
y = (3, 3, 2, 8, 4, 0)
div = map(divide, x,y)
print div

# Division by reduce function

divbyred = reduce(lambda x, y: x / y, [24, 2, 2, 2])
print divbyred

# Division by mapping 3 sets
a = (8, 27, 64, 125)
b = (2, 3, 4, 5)
c = (2, 3, 4, 5)

map (lambda x, y, z: x/y/z, a, b, c)
print map (lambda x, y, z: x/y/z, a, b, c)


# Factorial

def factorial(x):
	if x > 1:
		return x * factorial(x-1)
	if x < 0:
		return "inf"
	return 1
	
x = (-1, 0, 1, 3, 5, 10)
fact = map(factorial, x)
print fact


# Squaring a number

def squared(x):
	return x*x
	
x = (-1, 0, 1, 3, 5, 10, 0.5)
square = map(squared, x)
print square


# Squaring using a Generator

x = (x ** 2 for x in range(20))
x = list(x)
print (x)



# Cubed Numbers

def cubed(x):
	return x*x*x
	
x = (-1, 0, 1, 3, 5, 10, 0.5)
cube = map(cubed, x)
print cube

# Cubing using a Generator

x = (x ** 3 for x in range(10))
x = list(x)
print (x)


# Square root

def root(x):
	if x >= 0:
		return x**(0.5)
	if x < 0:
		return "imaginary number"
		
x = (4, 9, 0, -9, 2.25)
sroot = map(root, x)
print sroot
	
	
# Cubed root

def cubedroot(x):
	if x >= 0:
		return x**(1/3.0)
	if x < 0:
		return -(-x)**(1/3.0)
		
x = (8, -8, 0, 0.125)
croot = map(cubedroot, x)
print croot


# Exponent 

def exp (x, y):
	return x ** y
	
x = (0, 1, 1, 2, 5, -5)
y = (10, 0, 6, 5, -3, 3)
exponent = map(exp, x, y)
print exponent


# Radians, Convert degrees to radians

def rad (x):
	return (x*math.pi)/180
	
x = (50, 100, -10, 0, 57.2958)
radians = map(rad, x)
print radians


# Sine

def sine (x):
	return math.sin(x)
	
x = (100, 90, 250, -50)
Sine = map(sine, x)
print Sine


# Cosine

def cos (x):
	return  math.cos(x)
	
x = (90, 100, 190, 300, -50)
Cos = map(cos, x)
print Cos


# Tangent

def tan (x):
	return math.tan(x)
	
x = (45, 100, 300, -10)
tangent = map(tan, x)
print tangent


# Celsius and Fahrenheit

Celsius = [-17.8, -10, -5, 0, 10, 20, 50]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print Fahrenheit

C = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)
print C