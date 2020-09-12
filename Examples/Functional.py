# MAPPING IS APPLYING FUNCTION TO A LIST

def myMap(seq, func):
    newList = []
    for item in seq:
        newList.append(func(item))
    return newList


# EXAMPLE: OF SQUARES OF ALL NUMBER IN A LIST
def square(x):
    return x*x

randomNumbers = [1, 8, -2, 7, 12, 66]

# MAP SQUARE FUNCTION ONTO LIST
squaresOfRandomNumbers = myMap(randomNumbers, square)

print(squaresOfRandomNumbers)

# EXAMPLE: SQUARE ROOT OF ALL NUMBERS
def squareRoot(x):
    return x ** (1/2)

randomNumbers2 = [1, 2, 4, 76, 82, 64, 100]
roots = myMap(randomNumbers2, squareRoot)
print(roots)