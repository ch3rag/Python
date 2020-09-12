myList = [1, 2, 3]
newList = [[x] for x in myList]
permutations = []

for k in range (0, len(myList) - 1):
    for i in range(0, len(myList)):    
        for j in range(0, len(newList)):
            if myList[i] not in newList[j]:
                temp = newList[j].copy()
                temp.append(myList[i])
                permutations.append(temp)
    newList = permutations
    permutations = []


print(newList)

            
















sentence = "my my saloni name is saloni is my"
listOfWords = sentence.split(" ")
uniqueWords = []
[uniqueWords.append(x) for x in listOfWords if x not in uniqueWords]
print(" ".join(uniqueWords))