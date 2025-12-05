# list is the built-in Python module that provides a variety of functions and methods to work with lists,
# which are ordered collections of items. Lists can contain items of different data types, 
# including other lists. Here are some common operations and methods associated with lists in Python:



# Python Collections List: [ ] mutable 
# Allows Duplicate 
# Any type of data can be stored 
# We modify the list item. 
# we can add or remove 
# ex. insert(), append(), extend(), pop()



grocery_list = ["eggs", "milk", "bread", "butter"]


print('eggs' in grocery_list)  # True

print(grocery_list[1])  # milk
print(grocery_list[-1])  # butter

print(grocery_list.index('bread'))  # 2

print(grocery_list[0:2])  # ['eggs', 'milk']        

print(grocery_list[-3: -1])  # ['milk', 'bread']

print(len(grocery_list))  # 4




grocery_list.append('cheese')  # None
print(grocery_list)  # ['eggs', 'milk', 'bread', 'butter', 'cheese']

grocery_list += ['coconunt']
print(grocery_list)  # ['eggs', 'milk', 'bread', 'butter', 'cheese', 'coconunt']

grocery_list.extend(['cookies', 'chocolates'])
print(grocery_list)  # ['eggs', 'milk', 'bread', 'butter', 'cheese', 'coconunt', 'cookies', 'chocolates']

demoList = ['1', '2']

grocery_list.extend(demoList)
print(grocery_list)  # ['eggs', 'milk', 'bread', 'butter', 'cheese', 'coconunt', 'cookies', 'chocolates', 1, 2, 3, 4, 5]    

grocery_list.insert(2, 'Yogurt')
print(grocery_list)




grocery_list.remove('butter')
print(grocery_list)

popped_item = grocery_list.pop()
print(grocery_list)

del grocery_list[1]
print(grocery_list)

# demoList.clear()
# print(demoList)  # []

# grocery_list.clear()
# print(grocery_list)  # []

grocery_list.sort()
print(grocery_list)