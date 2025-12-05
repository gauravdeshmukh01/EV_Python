# import re

# text =  "The rain in SriLanka"

# y = re.search("^The .* SriLanka$", text)

# if y:
#     print("They need our help!")
# else:
#     print("They are safe!")

# *******************************************************

# search, findall,  split,  sub,   ., *, +, ?, ^, $, {} --> specified no of occurrances

# search – Finds the first location where the regex pattern matches in the string.

# findall – Returns all occurrences of the pattern as a list.

# split – Splits the string wherever the pattern matches.

# sub – Replaces all matches of the pattern with another string.


# . – Matches any single character except newline.

# * – Matches 0 or more repetitions of the preceding pattern.

# + – Matches 1 or more repetitions of the preceding pattern.

# ? – Matches 0 or 1 repetition (makes something optional).

# ^ – Matches the start of the string.

# $ – Matches the end of the string.

# {} – Specifies exact or range of repetitions (e.g., {2}, {2,5}).

#*************************************************************************

# import re 

# text = "The rain in SriLanka"
# y = re.findall("in", text)

# print(y)

#*************************************************************************

# import re 

# text = "The rain in SriLanka"
# x = re.split("\s", text, 1)

# print(x)


# \s  → matches any space
# 1   → split only 1 time

#*************************************************************************

# import re 

# text = "The rain in SriLanka"
# x = re.sub("\s","6", text)

# print(x)

# T h e _ r a i n _ i n _ S r i L a n k a
#                     ↑ ↑ ↑
#                  these are spaces

#*************************************************************************

import re 

text = "The rain in SriLanka"
x = re.sub("\s","6", text)

print(x)