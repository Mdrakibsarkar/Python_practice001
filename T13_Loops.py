#For Loop
#for x in range(6): # list in [0,1,2,3,4,5]
#    print(x)

#list1 = ['potato','tomato','chillies']
#print(list1[0],list1[1],list1[2])

#for item in list1:  # : means entering inside the for loop
     #print(item)

#list2 = [['potato',1],['tomato',2],['chillies',3]] # list of list

#for item,count in list2:
    #print(item)
    #print("item =",item,"::count =",count)

## using dictionaries
## The items() method returns a view object. The view object contains the key-value pairs of the dictionary,
# as tuples in a list. The view object will reflect any changes done to the dictionary,
#list3 = [['potato',1],['tomato',2],['chillies',3]] # list of list
#dict2 = dict(list3) #typecasting list to dict
#print(dict2)
#for item,count in dict2.items(): # using only dict2 will give only keys in dict2
#   print("item =", item,"::count=",   count)

list3 = [ ["Biscuit",1], ["Namkeen",5], ["Bread",3] ] # list of list
# for item in list3:
#     print(item)
# print(list3[0])
# for item,count in list3:
#     print("item =",item,",count =",count)

# Working with dict in loops
# [ ["Biscuit",1], ["Namkeen",5], ["Bread",3] ]
#   0              1              2
dict1 = dict(list3)         #Type casting list to dictionary
# print(dict1)
# print(dict1[1])            # it cannot work as print(list3[0]) as it tries to look for keyword 0 in the dict,
                            # where list tries to resolve its subscript [0]
# for item in dict1:
#     print(item)

# Problem: Will the following work?  Ans: nop because ['Biscuit', 1] is at 0th location ["Namkeen",5] is at 1st location
                                    # so its dificuilt to traverse between 0th and 1st location to get value "1" for biscuit
# for item,count in dict1:
#     print("item =",item,",count =",count)

# Solution
# for item,count in dict1.items():
#     print(item,count)


## Quiz : Print only numbers which are greater than 6 from a list
list4 = [1,'golu', int, float, 10]

for i in list4:
    print("i=", i)     #first i=1,golu,......(vertical way)
    if str(i).isnumeric() and i>6 :
    #The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
       print(i)

#   str(i).isnumeric() and i>6
#    str(1).isnumeric() and  1>6
#        True            and false --->false
#      '''''''''
#   str(10).isnumeric() and i>6
#       true            and true---->



## While loop

#i=0
#while (i<5):
#      print(i)
#      i=i+1

#counter = 0
#while(counter < 3):
#     counter = counter + 1
#     print(counter)

#num = [1,2,3,4,5]
#while num:
#    print(num.pop())

# # 1st itr
# num = [1, 2, 3, 4]      # 5
# # 2st itr
# num = [1, 2, 3]         # 4
# # 3st itr
# num = [1, 2]            # 3
# # 4st itr
# num = [1]   # 2
# # 5st itr
# num = []   # 1
# # while num conditional false(0)
