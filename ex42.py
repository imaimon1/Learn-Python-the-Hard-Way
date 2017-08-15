class Animal(object):
	pass
##is a
class Dog(Animal):
	
	def __init__(self,name):
		## has a
		self.name = name
		
class Cat(Animal):
	
	def __init__(self, name):
		##has a
		self.name = name

class Person(object):
	def __init__(self,name):
		##has a 
		self.name = name
		
		self.pet= None
##isa
class Employee(Person):
	def __init__(self,name,salary):
		super(Employee,self).__init__(name)
		self.salary=salary
class Fish(object):
	pass

class Salmon(Fish):
	pass
class Salmon(Fish):
	pass
class Halibut(Fish):
	pass
Rover= Dog("rover")

Satan = Cat("satan")

mary= Person("Mary")

mary.pet = Satan

frank = Employee("Frank",1200000)

frank.pet = Rover
flipper = Fish()
crouse = Salmon()
harry = Halibut()



