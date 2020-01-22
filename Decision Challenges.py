order_amt = float(input("What is the order amount?"))
state = input("Which state?")
tax = 0
if state == 'CA':
    tax = 0.08
print("The subtotal is {:.2f}".format(order_amt))
tax_amt = order_amt * tax
print("Tax: {:.2f}".format(tax_amt))
total = order_amt + tax_amt
print("The total cost is {:.2f}".format(total))

