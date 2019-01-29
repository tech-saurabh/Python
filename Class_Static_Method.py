print("Python program to demonstrate use of class method and static method")
from datetime import date
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
     
    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
     
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
print("Printing persons age by class method")
person1 = Person('mayank', 17)
person2 = Person.fromBirthYear('mayank', 1996)
 
print (person1.age)
print (person2.age)
 
# print the result
print("Checking if a person is adult or not by static method")
print (Person.isAdult(22))
