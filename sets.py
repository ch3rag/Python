from __future__ import print_function

vowels = {"a" , "e", "i", "o", "u", "a"}

print(vowels)

print("a" in vowels)

# PRINTS TRUE (CHECKS MEMBERSHIP)

# DUPLICATES ARE REMOVED AUTOMATICALLY

a = {1, 5, 8, 9, 17, 15, 21}

b = {5, 34, 17, 18, 19, 21, 24, 36}

print(a - b)

print(a & b)

print(a | b)

print(a ^ b)

multiples = {x * 2 for x in range(1,10)}

print(multiples)
