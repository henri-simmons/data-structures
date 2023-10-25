"""
Object oriented programming

what is self:
    self is used when creating a function from within a class so that it refers to the object itself.
    so the function can be called from inside the class like 'student1.gpa()'
"""
'''
#dont need to write object when making class in python3
class Students:
    programme = "DS"
    module = "CA268"
    name = "Jack"

    def gpa(self, mark_a, mark_b):
        return((mark_a + mark_b) // 2)

student1 = Students()
student2 = Students()
print(student1.module)
print(student2.gpa(mark_a=50, mark_b=30))
'''
class Students():
    def __init__(self, name, module, programme):
            self.name = name
            self.module = module
            self.programme = programme
            self.avg_mark = 0
    def gpa(self, mark_a, mark_b):
          self.avg_mark = (mark_a+mark_b)/2

student1 = Students("Adam", "ca170", "comsci1")
student1.gpa(50, 100)
print(student1.module)