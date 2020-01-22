"""
Things on the final:
Print statements
Math functions
Exponents
Floor Division
Modulus
Booleans
variables
printing with variables
inputs
recasting (    int() or str()    )
Escape Characters***
rounding
keywords (input, print)
concatenation
"""

# Basic Prints
print("Hello World")

# Basic Math
print(5 + 3)
print(8 * 234)
print(11 / 4)

# Exponents
print(15 ** 2)  # This is 15 to the power of 2

# Floor Division
print(13 // 4)  # This divides, and rounds down

# Escape Characters
print("The cow says: \"Moo\"")
print('Welcome to Mr. Wiebe\'s class')
print("This is the first line. \nThis is the second line.")
print("\tThis is a tab.")
print("AM\\PM")


print("\tIndent this line. \nPut this on a new line.")

# Rounding
number = 5.68546435468454198128
print("The number is approximately {:.2f}".format(number))

# Worksheet Solutions
"#3"
print("{:.4f}".format(22/7))

"#5"
print("{:.3f}".format(33/7))

# Modulus
print(17 % 5)  # 2
print(599 % 100)  # 99
print(57 % 15)  # 12
print(38 % 2)  # 0

# Booleans
print(5 > 1)  # True
print(5 == 5)  # 5 is equal to 5
print(5 != 6)  # 5 is not equal to 6
print(7 >= 10)  # 7 is greater than or equal to 10

# Variables
num1 = 15
num1 += 5
print(num1)  # 20

number1 = 500
number1 %= 100
print(number1)  # 0

first_num = 15
second_num = 4
third_num = 12
first_num = third_num - second_num  # First_num is 8
first_num += 2  # first_num is 10
third_num -= 7  # third_num is 5
second_num /= 2  # second_num is 2
print(first_num)   # 10
print(second_num)  # 2
print(third_num)  # 5

# Inputs
on_task = input("Are you on task?")
print(on_task)

# Recasting
age = input("How old are you?")
age = int(age)
print("Next year, you will be {} years old"
      .format(age + 1))

cost = input("How much does it cost?")
tax = 1.0795  # Sales tax in Fresno is 7.95%
cost = float(cost)
print("The item costs ${}".format(cost * tax))

# Keywords
'''
These are special keywords:
(These are in blue, 
and you cannot name a variable these)
print
int
input
float
str
False
True
'''

# Concatenation
thing1 = "a"
thing2 = "b"
print(thing1 + thing2)  # ab

thing3 = "65"
thing4 = "12"
print(thing3 + thing4)  # 6512

print(int("5") + int("15") + 5)  # 25


