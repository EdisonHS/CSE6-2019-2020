# Creating a list
groceries = ["milk", "eggs", "bread", "oranges", "milk"]
boring_list = [7, 7, 7, 7, 7, 0]
numbers = [12, 2, 3.5, 1]
empty_list = []

# Counting items in a list
length = len(groceries)
print("Our groceries list has {} items".format(length))
length2 = len(boring_list)
length3 = len(numbers)

# Accessing items in a list (we do this by index)
print(groceries[2])
print(groceries[3])
print(groceries[0])  # Index starts at 0 not 1
print(groceries[-1])
print(groceries[-2])

# Adding items to a list
print(groceries)
groceries.append("Apples")  # Adds to the END of the list
print(groceries)

groceries.insert(1, "Soda")  # Adds to index 1
print(groceries)

# print(groceries[1000])

# Removing items from a list
groceries.remove("milk")  # Only removes the first one!
print(groceries)

groceries.pop(2)  # Removes the item at index 2
print(groceries)

# Finding items in a list
spot = groceries.index("oranges")
print("Oranges are at index {}".format(spot))

print(boring_list)
position = boring_list.index(7)  # Its the first one
print("The number 7 is at index {}".format(position))

# sorting a list
print(groceries)
groceries.sort()
print(groceries)

print(numbers)
numbers.sort()
print(numbers)

for i in groceries:
    print(i)
