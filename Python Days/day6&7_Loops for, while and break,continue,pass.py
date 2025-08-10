# the for loop
for i in range(5):
    print(i)
#the range function
range(5)         # 0 to 4
range(1, 6)      # 1 to 5
range(1, 10, 2)  # 1, 3, 5, 7, 9

# the while loop
x = 0
while x < 5:
    print(x)
    x += 1
# the break statement
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)
# the continue statement
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # This will print only odd numbers
# the pass statement
for i in range(5):
    if i == 2:
        pass  # Do nothing for i == 2
    print(i)  # This will print all numbers from 0 to 4, but do nothing for 2

#------practice task----------------
# Print numbers from 1 to 10, but stop when number = 7 (break)
for i in range(1, 11):
    if i == 7:
        break
    print(i)
 #Print numbers from 1 to 10, but skip 5 and 6 (continue)
for i in range(1, 11):
    if i == 5 or i == 6:
        continue
    print(i)
# Print numbers from 1 to 10, but do nothing for 3 (pass)
for i in range(1, 11):
    if i == 3:
        pass  # Do nothing for 3
    print(i)  # This will print all numbers from 1 to 10, but do nothing for 3
#Create a basic menu loop using while:
#1. Add  
#2. Subtract  
#3. Exit
#User selects an option — loop should `break` on "3"
while True:
    print("Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Exit")
    
    choice = input("Select an option (1/2/3): ")
    
    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 + num2)
    elif choice == '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Exiting the menu.")
        break
    else:
        print("Invalid option, please try again.")
    print("----------------")  # Print a blank line for better readability