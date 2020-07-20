def read_file(name):
       try:
           with open(name + ".txt", 'a') as f:
               abc = f.read()
               print(abc)
       except Exception as e:
           print("Error:",e)
       finally:
           with open(name + ".txt", 'r') as f:
               abc = f.read()
               print(abc)

#def read_file(name):
#    with open(name + ".txt", 'r+') as f:
#        abc = f.write("Member's name:"+name)
#        print(abc)


print("HEALTH TRACKER")
print("------------------------")
user_name = input("Enter the name: \n")
#print("Enter the member: ",user_name.lower())
user_name = user_name.lower()
print("Enter the member name: " + user_name)
age=int(input("Enter your age:"))
print(age)

if user_name == "rahul" or user_name == "shyam":
    read_file(user_name)
#    print("Enter the gender\n"\
#      "1.MALE\n"\
#      "2.FEMALE\n")
#    select=input("enter 1,2 option:")

