# -*- coding: utf-8 -*-

"""The try block lets you test a block of code for errors.

The except block lets you handle the error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

"""

try:
    print(q)
except NameError:
    print("Variable q is not defined")
except:
    print("Something else went wrong")
finally:
    print("the 'try except' is finished")
#print(q)

# Example 1

# try:
#   f = open("demofile.txt")
#   f.write("Lorum Ipsum")
# except:
#   print("Something went wrong when writing to the file")
# finally:
#   f.close()


# Raise an exception

#Example 1

x = int(input("Insert a number --> "))
if x < 0:
    raise Exception ("Sorry, no numbers below zero")
print(x)


#Example 2

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")