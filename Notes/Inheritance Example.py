class Animal :
	name = ""
	age  = 0

	def __init__ (self, name, age) :
		self.name = name
		self.age  = age

	def printDetails (self) :
		return "My name is {} and my age is {}".format(self.name, self.age)

class Cat (Animal) :
	__owner = ""
	testVar = 1

	def __init__ (self, name, age, owner) :
		Animal.__init__(self, name, age)
		self.owner = owner
		

	def printDetails (self) :
		return "My name is {}, mt age is {} and my owner is {}.".format(self.name, self.age, self.owner)

myCat = Cat("Kitti", 3, "Chirag")


print myCat.printDetails()
