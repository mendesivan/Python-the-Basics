# create a class


class myclass:
    x = 5

# create an object


p1 = myclass()
print(p1.x)

#__init__() function (real world usage)


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name + " and I am", self.age, "years old")


p1 = person("John", 34)

print(p1.name)
print(p1.age)
p1.myfunc()

# delete object property by using the "del" function.
