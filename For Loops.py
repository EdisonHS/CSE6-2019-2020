for variable in range(10):
    print("Hello World")

for iterator in range(1500):
    print('Computer Science')

for i in range(2, 5):
    print("How many times will this print?")

for i in range(4, 10):
    print("Magic")

for i in range(8):
    print(200)

for i in range(5):
    print(i)

for i in range(12):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(20, 25):
    print(i + 4)

for i in range(20, 25):
    print("The value of 'i' is: ")
    print(i)
    print("But it prints this instead: ")
    print(i + 4)
    print()

for i in range(0, 16, 2):
    print(i)

for i in range(1, 17, 2):
    print(i)

for i in range(1, 8, 2):
    print(i)

for i in range(10, 0, -1):
    print("Time Left: {}".format(i))

# ----------
# For Loops Day 2
# ----------
print()
print("Day 2 notes")
print()
# Adding the numbers 1 through 100
# Could you imagine trying to do this by hand?
# It is tedious. Annoying. Long.
# For loops make it easy.
total = 0
for i in range(1, 101):  # How do I get 1 through 100?
    total += i
    print("The total so far is {}".format(total))
print("The final total is {}".format(total))
# You should have 5050.

# Divisibility
# We will attempt to print out ONLY numbers
# divisible by 2 between 1 and 100.
for i in range(1, 101):
    if i % 2 == 0:  # If i is evenly divisible by 2
        print(i)

for i in range(1, 101):
    if i % 3 == 0:  # If i is evenly divisible by 3
        print(i)

for i in range(1, 101):
    if i % 2 == 0 and i % 3 == 0:
        print(i)
