#!/usr/bin/env python3
class Person(object):
	"""
	return a object of person
	"""

	def __init__(self,name):
		self.name = name
	def get_details(self):
		"""
		return a string which include person's name
		"""
		return self.name

class Student(Person):
	"""
	return a object of student
	"""
	def __init__(self,name,branch,year):
		Person.__init__(self,name)
		self.branch = branch
		self.year = year
	def get_details(self):
		"""
		return a string which include student's name
		"""
		return "{} studies {} and is in {} year.".format(self.name,self.branch,self.year)

class Teacher(Person):
	"""
	return a object of Teacher
	"""
	def __init__(self,name,papers):
		Person.__init__(self,name)
		self.papers = papers
	def get_details(self):
		return "{} teaches {}".format(self.name,','.join(self.papers))

person1 = Person('Sachin')
student1 = Student('Kusha1','CSE',2005)
teacher1 = Teacher('Prashed',['C','C++'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())


