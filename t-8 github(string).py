#6.	String Slicing And Other Functions In Python  # These are immutable
# Search in string, its a datatype
#-14                             -3 -2 -1
#  W e     r i s e      a s      o  n  e
#  0 1  2  3 4 5 6  7   8 9  10  11 12 13
mystr = "We rise as one" # indexation starts from zero
#print (mystr)
#print(mystr.replace("We" , "I"))
# print(len(mystr)) # 14 as from 0 to 13
# print (mystr[14]) # Error because index is from 0 to 13
#print (mystr[13]) #index numbers in square brackets

# String Slicing
# print(mystr[0:14]) # [including: excluding(total)] [start : end-1 ]we saw 14th index is error so ?
# print(mystr[3:7])
# print(mystr[0:])
# print(mystr[:])
# print(mystr[:6])
# print(mystr[:78])
# print(mystr[78]) # let see how it works
# print(mystr[:14]) # will be [0:14])
# print(mystr[10:14]) # then ?

#  W e     r i s e      a s      o  n  e
#  0 1  2  3 4 5 6  7   8 9  10  11 12 13

# Extented Slicing
# # 3rd parameter stride, which refers to how many characters to move forward
# print(mystr[0::1]) # str[start:end-1:jump]
# print(mystr[0::2])
# print(mystr[0:7:3])
# print(mystr[0::5555])

#-14                             -3 -2 -1
#  W e     r i s e      a s      o  n  e
#  0 1  2  3 4 5 6  7   8 9  10  11 12 13
#print(mystr)

# Negative indexing
# print(mystr[-1:0])
# print(mystr[-3:-1]) # [including: excluding(total)] #start:end-1
# print(mystr[11:13])
# print(mystr[-14])
# print(mystr[::])
print(mystr[::-1])
print(mystr[::-2])

# String functions
#str2 = "hello"
# print(type(str2))
# print(str2.isalnum()) # as we have spaces in str2
# #if all are number or letter or both #its dont check underscore,space--->false(output)

str2="hello one"
#print(str2.endswith("one"))
#print(str2.count("e"))
#print(str2.capitalize()) # first letter would be capital
print(str2.find("on"))
#print(str2.replace("one","team"))

