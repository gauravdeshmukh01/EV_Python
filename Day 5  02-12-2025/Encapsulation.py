# class Company():
#     def __init__(self):
#         self.__company_name = "Infosys"  # Private attribute
    
# c1 = Company()
# c1.company_name = "Google"  # New attribute
# print(c1.company_name)      # Prints Google
# print(c1._Company__company_name)  # Prints Infosys (private variable)

# **********************************************************************

# Data Hiding / Encapsulation

# self.companyname  => public
# self.__companyname => private
# self._companyname => protected


# class Company():
#     def __init__(self):
#         # self.companyname="Infosys"   #public
#         # self.__companyname="Infosys"    #private
#         self._companyname="Infosys"     #protected

#     def companyName(self):
#         print(self._companyname)


# c1=Company()
# c1.companyName()

# **********************************************************************

# class Company():
#     def __init__(self):
#         # self.companyname="Infosys"  #public
#         # self.__companyname="Infosys"  #private
#         self._companyname="Infosys"   #protected

# cl=Company()
# print(cl._companyname)


# class b(Company):
#     pass

# print("derived class")
# bl=b()
# print(bl._companyname)

# **********************************************************************

