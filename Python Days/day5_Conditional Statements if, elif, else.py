# 1.basic "if" statement
age = 18
if age >= 18:
    print("You are eligible to vote.")
    
#if else statement
num = 5
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#if elif else statement
marks = 85

if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >= 60:
    print("C Grade")
else:
    print("Fail")
# Nested if statement
num = 10
if num > 0:
    print("Positive")
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
# Ternary operator
age = 16
status = "Adult" if age >= 18 else "Minor"
print(status)
# Practice Task
# Ask the user for age:
#If age < 13 → Child
#If 13–19 → Teenager
#If 20–59 → Adult
#Else → Senior
age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif 13 <= age <= 19: 
    print("Teenager")
elif 20 <= age <= 59:
    print("Adult")  
else:
    print("Senior")
    
#Ask for username and password, and check:
#If username is "admin" and password is "1234" → Access granted
#Else → Access denied
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Access granted")
else:
    print("Access denied")

# Check if a number is positive, negative, or zero
x = int(input("Enter a number: "))
print("Positive") if x > 0 else print("Negative or Zero")

    