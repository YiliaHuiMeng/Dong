#!/usr/bin/env python3

import sys
from collections import Counter

cj = sys.argv[2]

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name
    def get_grate(self):
        if sys.argv[1] == 'teacher':
            cc = dict(Counter(cj).most_common(4))
            print("A:{},B:{},C:{},D:{}".format(cc['A'],cc['B'],cc['C'],cc['D']))
        if sys.argv[1] == 'student':
            cc = dict(Counter(cj).most_common(4))
            print("Pass:{},fail:{}".format(cc['A']+cc['B']+cc['C'],cc['D']))


class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)


class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))


person1 = Person('Sachin')
student1 = Student('Kushal', 'CSE', 2005)
teacher1 = Teacher('Prashad', ['C', 'C++'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())
