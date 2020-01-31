value = 0
while value <= 10:
    print(value)
    value += 1

start = 100
while start > 0:
    print("Start is {}".format(start))
    start -= 10
    print("Start is now {}".format(start))
    print()

name = ""
while len(name) < 2:
    print("Your full name")
    name = input("Enter your name: ")

number = 0
while number != 3:
    print("Type the number 3.")
    number = int(input(">_ "))
print("You typed the number 3!")
print("Good Job!")

import random  # This only has to happen once!
num = 0
counter = 0
while num != 6:
    num = random.randint(1, 100)
    counter += 1
    print("Our random number is {}".format(num))
print("We got the number 6!")
print("It took us {} tries to get the number 6"
      .format(counter))
