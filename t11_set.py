# sets value dosent change, define via () but access via [], retain only unique values -- imp
s = set()
#print(type(s))
l = [1,2,3,4,4,4]
l = [1,2,2,3,4,4,4]
set_list = set(l)
#print(set_list)
#print(type(set_list))

#set_list.add(5)
set_list.add(100)
#print(set_list)
#set_list.add(10)
#s1 = set_list.union({11,21})
# set_list.add(10)
#s1 = set_list.union({11,99,21})     # values are in dictionary, union add in descending order
#s2 = set_list.intersection({1,2})
s3 = {1,6,7}
#print(set_list)
#print(s1)
#print(s2)
#print(len(set_list))
#print(max(set_list))
#print(min(set_list))
#print(set_list)
# print(s1)
# print(s2)
# print(len(set_list))
# print(max(set_list))
# print(min(set_list))
#print(s3.isdisjoint(set_list))  # True if they do not have any common element in between them.