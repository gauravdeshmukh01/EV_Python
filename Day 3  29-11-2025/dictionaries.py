# {}

car={
    "brand":"Ford",
    "model":"Mustang",  
    "year":1964
}

# method 2
car2 = dict(brand="Ford", model="Mustang", year=1964)  # no quotes for keys

# print(car)
# print(car2)
# print(type(car))
# print(type(car2))


# print(car["brand"])  # accessing value using key
# print(car.get("model"))  # accessing value using get method


# # listing all keys
# print(car.keys())

# # listing all values
# print(car.values())


# # list of key/value pair as tuples
# print(car.items())

# #verify a key exists
# print("model" in car)  # True
# print("color" in car)  # False

# #change value
# car["brand"] = "Tata"
# car.update({"price":50000})  # adding new key-value pair
# print(car)

# # remove item
# car.pop("model")
# del car["year"]
# print(car)

# # clear dictionary
# car.clear()
# print(car)


# # copy dictionary - first method
# car4 = car.copy()
# print("Good copy")
# print(car4)
# print(type(car4))


# car3 = car
# print("Bad copy")
# print (car3)


# # method 2 
# car5 = dict(car)
# print("Good copy method 2")
# print(car5)



# nested dictionaries

member1 = {
    "name": "Gaurav",
    "age": 21
}

member2 = {
    "name": "Karthik",
    "age": 22
}

Group = {
    "member1": member1,
    "member2": member2
}

print(Group)

print(Group["member1"])

print(Group["member1"]["name"])