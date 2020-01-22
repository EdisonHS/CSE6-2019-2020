score = 40
if score > 50:
    print("High Score!")
    print("End Program")

number = 3
if number > 10:
    print("You Win!")

grade = 80
if grade >= 60:
    print("You passed the test")
if grade >= 80:
    print("You got at least a B")
if grade == 0:
    print("You got a zero")

grade2 = 90
if grade2 > 60:
    print("You passed the test")
else:
    print("You did not pass")

if True:
    print("This will always print")

cost = int(input("How much does it cost?"))
if cost < 5:
    print("Pay with a couple dollar bills")
elif cost < 20:
    print("Use a $20 bill")
else:
    print("You can't afford it")

your_grade = int(input("Enter your percentage:"))
if your_grade >= 90:
    print("You got an A.")
elif your_grade >= 80:
    print("You got a B")
elif your_grade >= 70:
    print("You got a C")
elif your_grade >= 60:
    print("You got a D")
else:
    print("You got an F")

num = int(input("Enter a number"))
if num < 0:
    print("Invalid Number")
if num > 10:
    print("Output 1")
elif num > 4 and num < 8:
    print("Output 2")
else:
    print("Output 3")

x = int(input("Enter a number"))
if x < 5:
    print("Output 1")
elif x > 10:
    print("Output 2")
if x == 3:
    print("Output 3")
elif x > 12:
    print("Output 4")

