#arithmatic operators
a = 10
b = 3
print(a / b)   # 3.333...
print(a // b)  # 3  *division ans without float
print(a % b)   # 1 *remainder
print(a ** b)  # 1000
# Comparison operators
print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
print(a >= b)  # True
print(a <= b)  # False
# Logical operators
# Operator | Meaning               |
# -------- | --------------------- |
#`and`    | True if both are True |
# `or`     | True if any is True   |
# `not`    | Reverses result       |

print(a > 5 and b < 5)  # True
print(a > 5 or b < 5)   # True
print(not (a > 5))       # False
# Identity operators
# Operator | Meaning               |                    

# -------- | --------------------- |
# `is`     | True if both are same objects |
# `is not` | True if both are not same objects |
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)        # False, different objects
print(x == y)        # True, same content
print(x is not y)    # True, different objects
print(x is not [1, 2, 3])  # True, different objects
# Membership operators  
# Operator | Meaning               |
# -------- | --------------------- |    
# `in`     | True if value is found in sequence |
# `not in` | True if value is not found in sequence |
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)        # True
print(6 in my_list)        # False
print(3 not in my_list)    # False
print(6 not in my_list)    # True
# Bitwise operators
# Operator | Meaning               |
# -------- | --------------------- |
# `&`      | Bitwise AND          | 
# `|`      | Bitwise OR           |
# `^`      | Bitwise XOR          |
# `~`      | Bitwise NOT          |
# `<<`     | Left shift           |
# `>>      | Right shift          |
a = 5  # 0101 in binary 
b = 3  # 0011 in binary
print(a & b)  # 1  (0001 in binary)
print(a | b)  # 7  (0111 in binary)
print(a ^ b)  # 6  (0110 in binary)
print(~a)     # -6 (inverts bits)
print(a << 1)  # 10 (1010 in binary, left shift)
print(a >> 1)  # 2  (0010 in binary, right shift)
# Assignment operators
# Operator | Meaning               |    
# -------- | --------------------- |
# `=`      | Assigns value         |
# `+=`     | Adds and assigns      |
# `-=`     | Subtracts and assigns |
# `*=`     | Multiplies and assigns |
# `/=`     | Divides and assigns   |
# `//=`    | Floor divides and assigns |
# `%=`     | Modulus and assigns   |
# `**=`    | Exponentiates and assigns |
x = 10
x += 5  # x = x + 5
print(x)  # 15
x -= 3  # x = x - 3 
print(x)  # 12
x *= 2  # x = x * 2
print(x)  # 24
x /= 4  # x = x / 4
print(x)  # 6.0
x //= 2  # x = x // 2

#------practice task----------------
#check  is user above 18? check is age between 13 and 19
age = int(input("Enter your age: "))
print("You are teenager")
print(age >= 13 and age <= 19) # True 
print("----------")
print("You are above 18 years")
print(age > 18)

#check if two numbers are equal, not equal, less than or equal, greater than or equal
num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))
print("is equal: ", num1==num2)
print( "is not equal: ",num1!=num2)
print( "is less or equal: ",num1<=num2)
print( "is greater or equal: ",num1>=num2)

#Combine multiple conditions using and, or, not
num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))
print("Both numbers are greater than 10:", num1 > 10 and num2 > 10)
print("At least one number is greater than 10:", num1 > 10 or num2 > 10)
print("Neither number is greater than 10:", not (num1 > 10 or num2 > 10))
print("Both numbers are equal:", num1 == num2 and num2 == num1)
print("At least one number is not equal:", num1 != num2 or num2 != num1)
print("Both numbers are not equal:", not (num1 == num2 and num2 == num1))
print("Both numbers are less than or equal to 20:", num1 <= 20 and num2 <= 20)
print("At least one number is greater than 20:", num1 > 20 or num2 > 20)
print("Both numbers are greater than or equal to 5:", num1 >= 5 and num2 >= 5)      
print("At least one number is less than 5:", num1 < 5 or num2 < 5)
print("Both numbers are not less than 5:", not (num1 < 5 or num2 < 5))
print("Both numbers are not greater than 10:", not (num1 > 10 or num2 > 10))
print("Both numbers are not equal to 0:", num1 != 0 and num2
!= 0)
print("At least one number is equal to 0:", num1 == 0 or num2 == 0)
print("Both numbers are not equal to 1:", num1 != 1 and num2 != 1)
print("At least one number is equal to 1:", num1 == 1 or num2 == 1)
print("Both numbers are not equal to 2:", num1 != 2 and num2 != 2)
print("At least one number is equal to 2:", num1 == 2 or num2 == 2)
print("Both numbers are not equal to 3:", num1 != 3 and num2 != 3)