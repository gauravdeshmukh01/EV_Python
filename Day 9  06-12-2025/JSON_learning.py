# import json

# x = {
#     "name":"Gaurav",
#     "age":21,
#     "city":"New York"
# }

# # conversion - dumping Python data into JSON string form

# y = json.dumps(x)

# print(y)

# print(json.dumps(["Ganga","Narmadha"]))

# print(json.dumps(("apple","grapes")))

# print(json.dumps("Welcome"))

# print(json.dumps(42))

# print(json.dumps(45.53))

# print(json.dumps(True))      #true in json

# print(json.dumps(False))     #false

# print(json.dumps(None))      #null


# *******************************************************************

import json

people_string = '''
{
    "people" : [
        {
            "name":"Smith",
            "phone":"676739380",
            "emails":["smith34@gmail.com", "smith5678@infosys.com"],
            "has_license": false
        },
        {
            "name":"Deva",
            "phone":"676739387",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

data = json.loads(people_string)
print(data)
print(type(data))

print(type(data['people']))

for person in data['people']:
    print(person)

for person in data['people']:
    print(person['name'])

for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys= True)
print(new_string)

