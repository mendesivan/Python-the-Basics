import Modules

Modules.greeting("Ivan")

#Note: When using a function from a module, 
#use the syntax: module_name.function_name.

age = Modules.person1["age"]
print(age)

# Built-in Modules

import platform as pltf

x = pltf.system()
print(x) #Windows

# Using the dir() function
y = dir(pltf)
#print(y)

# Import from Module example above
from Modules import person3

print(person1)