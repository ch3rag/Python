
myTuple = (1, 2, 3, 5)

# myTuple[0] = 3
# ERROR tuples are immutable
# However

myList = list(myTuple)

myList[0] = 3

myTuple = tuple(myList)

print(myTuple)

print(max(myTuple))

print(min(myTuple))

print(len(myTuple))

# TUPLE CAN CONTAIN MUTABLE ELEMENTS

list_1 = [1,2,3]

list_2 = [4,5,6]

myTuple = (list_1, list_2)

print(myTuple)

list_2[1] = 99

print(myTuple)

# EMPTY TUPLE

empty = ()

# SINGLETON TUPLE 

# singleton = ("one")  ==> WRONG CONSIDERED AS AN STRING

singleton = ("one",) # ==> NOTICE THAT COMMA

print(singleton[0])

