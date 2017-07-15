
# Addition

add <- function(x, y)
{return (paste("The sum of the two numbers is", (x + y)))}
  
# test addition

add(2, 2)
add(2, 4)
add(-2, 2)
add(2, -2)
add(4, -1)
add(3, 0)
add(0.5, 0.3)

# Subtraction

subtract <- function(x, y)
{return (paste("The result of", x, "minus", y, "is", (x - y)))}

# test subtraction

subtract(2, 2)
subtract(3, 2)
subtract(2, 3)
subtract(-2, -3)
subtract(-2, 2)
subtract(0.5, 0.4)

# Multiplication

multiply <- function(x, y)
{return (paste("The product of the two numbers is", (x*y)))}

# test multiplication

multiply(2, 2)
multiply(2, 3)
multiply(0, 2)
multiply(2, 0)
multiply(-2, 0)
multiply(2, -2)
multiply(-2, -2)
multiply(0.5, 0.25)
  
# Division

divide <- function(x, y)
{return(paste("The result of", x, "divided by", y, "is", (x/y)))}

# test division

divide (6, 3)
divide (-6, 3)
divide (0.5, 0.5)
divide (0, 4)
divide (4, 0)
divide (0.5, 0.25)
divide (0.5, -0.25)


# Factorial

fact <- function(x)
{return(paste("The factorial of", x, "is", (factorial(x))))}

# test factorial

fact(5)
fact(0)
fact(1)
fact(6)
fact(10)
fact(-3)


# Squared

squared <- function(x)
{return(paste(x, "squared is", (x*x)))}

# test squared

squared(10)
squared(-10)
squared(0)
squared(0.25)
squared(-1.25)


# Cubed

cubed <- function(x)
{return(paste(x, "cubed is", (x*x*x)))}

# test cubed 

cubed(10)
cubed(-10)
cubed(0)
cubed(0.5)
cubed(-0.5)
cubed(1.25)


# Square Root

root <- function(x)
{return(paste("The square root of", x, "is", (x**0.5)))}

# test square root

root(9)
root(5)
root(-9)
root(0)


# Exponent

exp <- function(x, y)
{return(paste(x, "to the power of", y, "is", (x**y)))}

# test exponent

exp(2,9)
exp(2, -9)
exp(-2, -9)
exp(0.3,4)
exp(0.3, 0.2)
exp(0.3, -0.2)


# Sine 

sine <- function(x)
{return(paste("The sine of", x, "is", (sin(x)), "radians"))}

# test sine

sine(100)
sine(90)
sine(250)
sine(-50)


# Cosine

cosine <- function(y)
{return(paste("The cosine of", y, "is", (cos(y)), "radians"))}

#  test cos

cos(90)
cos(100)
cos(190)
cos(300)
cos(-50)


# Tangent

tangent <- function(x)
{result(paste("The tan of", x, "is", (tan(x)), "radians"))}

# test tan

tan(45)
tan(100)
tan(300)
tan(-10)

