# Using one parameter
price = 49
txt = "The price is {} dollars"
print(txt.format(price))


# using multiple parameters
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {} dollars."
print(myorder.format(quantity, itemno, price))
