def q1_sum(array):
    ans = 0
    for item in array:
        if type(item) == list:
            for i in item:
                if i % 2 == 0:
                    ans += i
        elif item % 2 == 0:
            ans += item
    return ans

def move_vow(line):
    v = ""
    c = ""
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    for char in line:
        if char in vowels:
            v = v + char
        else:
            c = c + char
    return v + c

class Memories:
    def __init__(self, name="NA", age="NA", salary=0):
        self.name = name
        self.age = age
        self.salary = salary
    def remember(self, arg):
        if arg == "salary":
            return self.salary
        elif arg == "age":
            return self.age
        elif arg == "name":
            return self.name
        else:
            return False
        

class Test:
    def __init__(self, subject_name, correct_answers, passing_mark):
        self.subject_name = subject_name
        self.correct_answers = correct_answers
        self.passing_mark = passing_mark
        

class Student:
    def __init__(self, name):
        self.name = name
    def take_test(self, paper, answers):
        correct = 0
        passing = float((paper.passing_mark).strip("%"))
        for i in answers:
            if i in paper.correct_answers:
                correct +=1
        grade = (correct / len(paper.correct_answers)) * 100
        if grade >= passing:
            return "Pass"
        else:
            return "Fail"

def histogram(nums, chr):
    for num in nums:
        print(num*chr)

def filter_star(dic, number):
    for objects in dic:
        if dic[objects] == number * '*':
            print(f'{objects}:{dic[objects]}')