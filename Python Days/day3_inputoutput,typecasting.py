#1. getting input from the user
#input() function is used to take input from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name, "good to know you are", age , "years old")

#2. Convert the input to an integer
age = input("Enter your age: ")
age = int(age) 
# or you can do it in one line
# age = int(input("Enter your age: "))

#3. Arithmetic Operations
# +, -, *, /, //, %, **
num1 = float(input("Enter first number: "))
num2 = float(input("Enter the second number: "))
sum =  num1 + num2
diff = num1 - num2
product = num1 * num2
quotient = num1 / num2
remainder = num1 % num2
power = num1 ** num2
print("Sum:", sum)
print("Difference:", diff)
print("Product:", product)
print("Quotient:", quotient)
print("Remainder:", remainder)
print("Power:", power)

#--------practice task----------------
# Convert Celsius to Fahrenheit
celcius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celcius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)
