# import yaml

# yaml_string = """
# name: Alice
# age: 30
# city: New York
# """

# data = yaml.safe_load(yaml_string)
# print(data)

# *********************************************************************

import yaml

python_data = {
    'product': 'Laptop',
    'price': 1200,
    'features': ['SSD', '8GB RAM', 'Full HD']
}

# To a String
yaml_output = yaml.dump(python_data)
print(yaml_output)

# To a file
with open('output.yaml', 'w') as file:
    yaml.dump(python_data, file)
