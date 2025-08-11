#A function is a reusable block of code that performs a specific task.
# Functions are defined using the def keyword
#def function_name(parameters):
    # code block
    
# Defining & Calling Functions

def greet():
    print("Hello, Tanmay!")

greet()  # calling the function

# Function with parameters
def greet_user(name):
    print(f"Hello", {name},"!")
greet_user("Tanmay")  # calling the function with an argument

#--------practice task----------------
#Create a function add(a, b) that returns their sum
a = int(input("1st num: "))
b= int(input("2nd num: "))
def add(a, b):
    return a + b
result = add(a, b)
print("Sum:", result)

#. Create a function factorial(n) and test it for 5, 7
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print("Factorial of 5:", factorial(5))  # Output: Factorial of 5: 120
print("Factorial of 7:", factorial(7))  # Output: Factorial of 7: 5040

#Create a function area_circle(r) that returns the area
def area_circle(radius):
    pi = 3.14159
    return pi * radius * radius

print(area_circle(7))  # Output: ~153.94
# Create a function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print("Is 11 prime?", is_prime(11))  # Output: True

#try writing a function square(n) that returns the square of a number
def square(n):
    return n * n
print("Square of 4:", square(4))  # Output: Square of 4: 16

#Create a function multiply(a, b) that returns their product
a = int(input("1st num: "))
b= int(input("2nd num: "))
def multiply(a,b):
    return a*b
result= multiply(a,b)
print(multiply(a,b))

#Write a function is_even(n) that returns True or False
n = int(input("Enter the num: "))
def is_even(n):
    return n % 2 == 0   
print("Is",n, "even? -->", is_even(n))  