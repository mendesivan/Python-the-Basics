#Inheritance

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
  pass

#passes function of Person to Student.

x = Student("Mike","Olsen")
x.printname()

