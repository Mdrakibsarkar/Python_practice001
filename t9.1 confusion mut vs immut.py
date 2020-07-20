# Case 1: Mem loc: 100
tup = (1, 2, 3) # Tuples are immutable, elements cannot be modified ,
#tup[0] = 10
#print(id(tup))
#print(tup[0])
#tup[0].append(10) # as elements are immutable, here tup is bhehaving as a tuple
#print(tup)

# Case 2: Mem loc: 200, Contentents are not changed refrence is changed
a = [1, 2]  # its a list which is mutable
b = [3, 4]  # # its a list
tup = (a, b)
#print(tup)
#print(id(tup))
#tup[0]=10
#tup[0].append(10)   # here tup is bhehaving as a list, as elements are mutable[List]
print(tup)
#print("Before",tup)
#print(id(tup))

#a.append(5)
#b.append(6)
#print("After",tup)  # Mem loc: 200, Here tuple is immutable but its elements are not. Object reference in the
#                     # tuple did not change but the reference objects did mutate
# print(id(tup))