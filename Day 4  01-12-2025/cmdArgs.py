# import argparse

# parser = argparse.ArgumentParser(
#     description="Provides a personal greeting based on user input."
# )

# parser.add_argument(
#     "-n", "--name", 
#     metavar="name", 
#     required=True,
#     help="the name of the person to greet"
#     )

# args = parser.parse_args()

# msg = f"Hello! {args.name}"

# print(msg)

#***************************************************************************

# import argparse

# # Create argument parser
# parser = argparse.ArgumentParser(description="Greeting program")

# # Add arguments
# parser.add_argument("-n", "--name", metavar="name", required=True,
#                     help="The name of the person to greet")

# parser.add_argument("-l", "--lang", metavar="language", required=True,
#                     help="The language of the greeting (english, spanish, german, hindi)")

# # Parse arguments
# args = parser.parse_args()

# # Build message using f-string and dictionary
# greetings = {
#     "english": "Hello",
#     "spanish": "Hola",
#     "german": "Hallo",
#     "hindi": "Namaskar"
# }

# msg = f"{greetings[args.lang]} {args.name}!"
# print(msg)

# # # Function using the same logic
# # def hello(name, lang):
# #     greetings = {
# #         "english": "Hello",
# #         "spanish": "Hola",
# #         "german": "Hallo",
# #         "hindi": "Namaskar"
# #     }
# #     return f"{greetings[lang]}, {name}"

# # # Print function output
# # print(hello(args.name, args.lang))

#***************************************************************************

