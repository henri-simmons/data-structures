'''
class Memories:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

person1 = Memories(name="Tom", age=32, address="fdfdf", salary=50000)
"""
setattr (can pass object to function and get new attribute)
getattr (return value of specified attribute)
delattr (deletes attribute from specific object)
hasattr (returns true or false depending on if specified object has attribute)
"""
print(person1.age)
'''
# INHERITANCE

class Person:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def is_student(self):
        return False
# student class inherits all properties of parent class and can override its methods
class Student(Person):
    def is_student(self):
        return True

person1 = Person("Tom")
print(person1.is_student())
student1 = Student("Jack")
print(student1.is_student())
person1 = Student(person1)
print(person1.is_student())
# double underscore before variable name __ makes it private, meaning it can only be used within the class that holds it

