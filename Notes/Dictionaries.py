#Dictionaries

telephones = {"Chirag" : 12345, "Karan" : 56778,
"Amar" : 45673, "Vishal" : 45678}

#Adding New Entries

telephones["Vikas"] = 56789

print(telephones)

#Accessing a member

print(telephones["Chirag"])

#Using Get

print(telephones.get("Chirag"))

#Deleting an entry

del telephones["Vikas"]

#Making a shallow copy

tel_copy = telephones.copy()

print(tel_copy)

#Deleting all the Entries

tel_copy.clear()

print(tel_copy)

#Getting all the keys

print(telephones.keys())

#Getting all the values

print(telephones.values())

#Creating List or Tuples using keys or values

key_list = list(telephones.keys())

values_tuple = tuple(telephones.values())

print(key_list)

print(values_tuple)

#Getting Length of Dictionaries

print(len(telephones))

#Python Dictionary Comprehension

squares = {x : x ** 2 for x in range(1,10)}

print(squares)

#Creating Dictionaries

#From Tuples

new_tuple = (("Fruit", "Apple"), ("Vegetable", "Potatoes"), ("Nut","Walnut"))

new_dictionary = dict(new_tuple)

print(new_dictionary)

new_dict =  dict(Fruit = 'Apple', Vegetable = 'Potatoes', Nut = 'Walnut')

print(new_dict)


#From Keys

'''
The fromkeys() method creates a new dictionary from the given sequence of elements with a value provided by the user.
'''

keys = {"a", "e", "i", "o", "u"}

value = [1]

new_dict = dict.fromkeys(keys, value)

print(new_dict)

value.append(2)

print(new_dict)

print(new_dict.values())

for (k,v) in telephones.items():
  print("Key : ", k , "Value : ", v)

#POP(item, default) ==> Pops item, or if the item is not found then default is returned

print(new_dict.pop("e", "Not Found!"))

print(new_dict.pop("e", "Not Found!"))

#POPITEM() ==> The popitem() returns and removes an arbitrary(random) element (key, value) pair from the dictionary



print(new_dict.popitem())

'''
The setdefault() method returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
'''

person = {'name' : "Chirag" , 'Age' : 18}

age = person.setdefault("Age", 20)

print(age)

#AGE DOESN'T CHANGE BECAUSE IT WAS FOUND IN DICTIONARY

id = person.setdefault("ID", 1)

#ID WILL BE ADDED TO DICTIONARY

print(id)

print(person)

#UPDATE METHOD UPDATE THE VALUE OF KEYS FROM OTHER DICTIONARY

numbers = {"one" : 1, "two" : 3}

update = {"two" : 2}

numbers.update(update)

three = {"three" : 3}

numbers.update(three)

print(numbers)

#MEMBERSHIP TEST (KEYS ONLY)

print("three" in numbers)

print(3 in numbers)

#SORTED RETURNS SORTED LIST OF KEYS

print(sorted(telephones))
