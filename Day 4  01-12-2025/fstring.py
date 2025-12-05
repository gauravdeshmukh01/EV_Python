# person = "Pushkar"
# Goldmedal = 3

# print("\n" + person + " have " + str(Goldmedal) + " Gold Medals")

# # Old-Style Formatting (Percent (%) Formatting)
# message = "\n %s have %d Gold medals" % (person, Goldmedal)
# print(message)

# # string.format() method
# message2 = "\n {} have {} Gold medals".format(person, Goldmedal)
# print(message2)

# # Positional arguments
# message3 = "\n {1} have {0} Gold medals".format(Goldmedal, person)
# print(message3)

# # Keyword arguments
# message4 = "\n {person} have {medals} Gold medals".format(medals=Goldmedal, person=person)
# print(message4)

# # Dictionary Unpacking with str.format()
# player = {
#     'person': 'Pushkar',
#     'Goldmedal': 3
# }

# message = "\n {person} have {Goldmedal} Gold medals".format(**player)
# print(message)

# ***************************************************************************

# f-Strings (Literal String Interpolation)

person = "Pushkar"
Goldmedal = 3

player = {
    'person': 'Pushkar',
    'Goldmedal': 3
}

message5 = f"\n {person} have {Goldmedal} Gold medals"
print(message5)

message6 = f"\n {person} have {2*5} Gold medals"
print(message6)

message7 = f"\n {player['person']} has {2*5} Goldmedals"
print(message7)

num = 10
print(f"\n 2.25 times {num}, {(2.25*num):.2f}")
