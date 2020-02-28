def say_hi():
    print("Hello!")


say_hi()
say_hi()


def create_divide():
    print()
    print("---------------")
    print()


create_divide()


def party(cheese, crackers):
    print("We have {} blocks of cheese and {} "
          "boxes of crackers".format(cheese, crackers))


party(15, 20)
party(10, 12)
party(7, 5)
create_divide()


def add_stuff(num1, num2):
    print("{} + {}".format(num1, num2))
    answer = num1 + num2
    print("The answer is {}".format(answer))

# This is a local variable
# It only exists in the function
# print(answer)


def subtract(num1, num2):
    print("SUBTRACTING {} and {}".format(num1, num2))
    return num1 - num2


age = subtract(10, 7)


def f(x):
    return x ** 2 + 3 * x + 9


print(f(3))
print(f(9))
print(f(700))


def divisible_by_2(number):
    if number % 2 == 0:
        return True
    return False


def divisible_by_7(number):
    return number % 7 == 0


for i in range(1000):
    if divisible_by_7(i) and divisible_by_2(i):
        print(i)

create_divide()


def can_sleep_in(weekday, vacation):
    """This function returns true if I can sleep in"""
    if vacation:
        return True
    elif not weekday:
        return True
    return False
