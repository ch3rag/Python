from __future__ import print_function
import sys


class Animal :
	__name = ""		# data memeber with "__" at the beginning are private members
	__type = ""
	__height = 0
	__weight = 0

	#Constructor Definition
	def __init__(self, name, type_, height, weight) :
		self.__name = name
		self.__type = type_
		self.__height = height
		self.__weight = weight

	def setName(self, name) :
		self.__name = name

	def getName(self):
		return self.__name

	def setType(self, type_) :
		self.__type = type_

	def getType(self) :
		return self.__type

	def setHeight(self, height) :
		self.__height = height

	def getHeight(self) :
		return self.__height

	def setWeight(self, weight) :
		self.__weight = weight

	def getWeight(self) :
		return self.__weight

#Creating Objects
myCat = Animal("Julie", "Cat", 10, 10)

print("NAME :  %s" %(myCat.getName()))
print("TYPE : %s" %(myCat.getType()))
print("HEIGHT : %d" %(myCat.getHeight()))
print("WEIGHT : %d" %(myCat.getWeight()))
print("ENTER NEW NAME : ", end = "")
myCat.setName(sys.stdin.readline())
print("NEW NAME : %s" %(myCat.getName()))


