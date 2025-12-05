#()

myTuple =('Gaurav', 42, True)
print(myTuple)  # Output: ('Gaurav', 42, True)

yourTuple = (1,2,2,3,4,6)
print(yourTuple)

#print(type(myTuple))  # Output: <class 'tuple'>

#yourTuple[0] = 10  # This will raise a TypeError because tuples are immutable


# newList = list(yourTuple)
# newList.append(8)
# print(newList)
# print(type(newList))

# newTuple = tuple(newList)
# print(newTuple)
# print(type(newTuple))


print("unpacking tuple items")
(one, *two, three) = yourTuple
print(one)
print(two)
print(three)
print(type(two))


print("counting 2 in yourTuple")
print(yourTuple.count(2))


print("Accessing tuple items using index")
print(yourTuple[3])  # Output: 3