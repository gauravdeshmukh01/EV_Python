# f1 = open("file_1.txt", "r")
# print(f1.read())


# f1 = open("file_2.txt", "w")
# f1.write("Hardwork Never Fails!")

# *******************************************************************************

# r+ file is exist already

# first reads info in terminal and then write in file, see changes in file1.txt

# f1=open("file_1.txt","r+")
# print(f1.tell())
# print(f1.read())
# print(f1.tell())
# f1.write("Practice makes perfect")
# print(f1.tell())
# print(f1.read())
# print(f1.tell())


# ********************************************************************************

#w+ --> if file already exists? rewrite it, we have content previously so its overwrite
# .tell() tells where the file handler is present at which location

# f1=open("file_1.txt","w+")
# print(f1.tell())
# f1.write("Hi Welcome")
# f1.write(" This is Python Session for PDA Batch1")
# f1.seek(0)  # to take handler at beginning of file so it can print data in terminal
# print(f1.read())
# f1.close()


# ********************************************************************************

# a+  => creates file if not present, we don't have so it created and also added text
# only a will not work for print(f1.read()) line
# 

# f1=open("file_3.txt","a+")
# f1.write("Hello Students")
# f1.seek(0)                          # brings file handler at beginning as here in a+ it is at end of file
# print(f1.read())


# ********************************************************************************

# f1=open("IMG_4704.JPG", "rb")
# print(f1.read())


# f1=open("IMG_4704.JPG", "rb") # binary read mode
# f2=open("IMG_4713.JPG", "wb") # binary write mode
# for i in f1:
#     f2.write(i)

# above loop read byte by byte data of 4704 and written
# into 4713, hence now we can see ,both images as same 


# ********************************************************************************
