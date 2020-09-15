# -*- coding: utf-8 -*-

# Technically, in Python, an iterator is an
# object which implements the iterator
# protocol, which consist of the methods
# __iter__() and __next__().


# Example 1 from a tuple
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Example 2 from a string

mystr = "Apple"
myit2 = iter(mystr)

print(next(myit2))
print(next(myit2))
print(next(myit2))
print(next(myit2))
print(next(myit2))

# Looping through an iteration. Through a tuple
mytuple = ("apples","bananas","mangos")
for i in mytuple:
    print(i)
    
# Create an iterator w/ StopIteration

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

    
Myclass = MyNumbers()
myiter = iter(Myclass)

for x in myiter:
    print(x)
