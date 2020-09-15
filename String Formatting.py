# String formatting -- Examples

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

txt = "The price is {:.2f} dollars"
print(txt.format(price))

# Multiple values

quantity = 3
itemno = 567
price = 49
myorder = "\nI want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Index place holder
myorder = "\nI want {0} pieces of item number {1} for {2:.2f} dollars"
print(myorder.format(quantity, itemno, price))

# Named indexes

mycar = "\nI have a {carname}, it is a {model}."
print(mycar.format(carname="Ford", model="Mustang"))
