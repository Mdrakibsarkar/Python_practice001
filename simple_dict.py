# Exercise
# # Create a dictionary and take input from user and return the meaning of word from dictionary

marketing={ "Rice":1200,"Dal":100,"Oil":100,"Soap":"50",
                               "Solt":40,"Safed":90,
                                        "other":{"biskut":30,"Sugar":30},1740:"Total"}
print(marketing)
print(type(marketing))
Customer=(input("Enter the item:"))
print("The item is:"+Customer)
print(" price :",marketing[Customer]) #doubt why don't run like marketing[Customer][Customer]