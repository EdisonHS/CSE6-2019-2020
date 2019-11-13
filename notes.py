print("Hello World")

print(True)
print(15)

# print(TRUE)
# This is a comment
# Nothing here will be executed

print('hello')
# print("world')
# Print("things")


# Data Types
print("hello")  # This is a string
print(13.543)  # This is a float
print(False)  # This is a boolean
print("seven")  # This is a string
print(-81)  # This is a integer

# This is a comment
'''
This is a multi-line comment
I can type anything here

'''

"""
I can also use quotation marks
to indicate a multi-line comment
"""

# ----------
# Math
# ----------

print()  # This creates a blank line
print()
print(3 + 5)
print(8 - 7)
print(4 * 3)
print(20 / 5)

print()
print()
print(2 ** 4)  # The result is 16
print(3 ** 2)  # The result is 9
print(4 ** 2)  # The result is 16
print(2 ** 10)  # The result is 1024
# The double star is the symbol for _______

print()
print()
# Floor Division (It rounds down)
print(12 // 3)
print(9 // 3)
print(10 // 3)
print(11 // 3)
print(15 // 4)  # The result is 3
print(-8 // 3)  # The result is -3

# Modulus
print()
print()
print(13 % 12)  # The answer is 1
print(14 % 12)  # The answer is 2
print(25 % 12)  # The answer is 1
print(7 % 4)  # The answer is 3
print(155 % 50)  # The answer is 5

print()
print()
# Mixed Review
print(3 ** 3)  # The answer is 27
print(27 % 5)  # The answer is 2
print(11 % 3)  # The answer is 2
print(18 // 10)  # The answer is 1

# --------
# Variables
# --------
print()
print()
the_number = 3
print(the_number)
the_number = the_number + 3
the_number = the_number * 100
print(the_number)

print()
screens = 4
screens + 2
print(screens)

drinks = 5
drinks = drinks + 10
drinks += 15
print(drinks)

food = 110
food -= 10  # Food is now 100
food *= 10  # Food is now 1000
food /= 100  # Food is now 10
food %= 5  # Find the remainder if you divide by 5
print(food)

# Review
# Do not run these
balance = 5000
balance -= 1000  # 4000
balance *= 2  # 8000
print(balance)

# --------
# Strings
# --------

first_word = "wiebe"
second_word = "computer science"
third_word = "money"
print(first_word, second_word)

# This is concatenation
print("I have a lot of fun in " + second_word)
print(first_word + " makes the class great.")

# Format Print
print("I have fun in {}'s class".format(first_word))

# Comparators

print(5 == 5)  # Is 5 equal to 5?
print(7 != 4)  # Is 7 not equal to 4?
print(5 > 2)  # Is 5 greater than 2?
print(10 >= 41)  # Greater than or equal to
print(-10 <= 9)  # -10 is less than or equal to 9?

first_variable = "the first thing"
second_variable = "the second thing"
print("{} and {}".format(first_variable, second_variable))

pizza = 5
slices = 10
pepper = 2
# Make this print
# "I want 5 pizzas, 2 peppers, and 10 slices"
print("I want {} pizzas, {} peppers, and {} slices"
      .format(pizza, pepper, slices))

current_class = "Computer Science"
teacher = "Mr. Wiebe"
# I enjoy Mr. Wiebe's Computer Science class.
print("I enjoy {}'s {} class".format(teacher, current_class))

# -----
# Inputs
# -----

name = input("What is your name?")
print("Hello {}".format(name))

# Inputs are the ONLY way to interact

age = input("How old are you?")
print("{}?!?!?! WOW, you belong in a museum!".format(age))