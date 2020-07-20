# Dictionary -- represented by {}, Key - Value pair , try to keep keys as immutalble
#d1 = {}
#print(type(d1))
d3 = {'Kapil':"Fruits", "vinod":"Roti", "james":"Biryani",
        "rohan":{"B":"maggie","L":"rice","D":"Chicken"}} #keys---->Kapil like ana value--->Fruits
#print(d3)
#print(hex(id(d3)))
#del d3["Kapil"]
#print(d3)
print(hex(id(d3)))
# print(d3["Kapil"]) #key show where value is the output
# print(d3["rohan"]["B"])
# print(d4["rohan"]["B"])
d3[420] = "Junk Food"
#print(d3)
d3["Salman"] = "Kebabs"
#print(d3)
#del d3["rohan"]
#print(d3)
#d4 = d3 # d3 and d4 are pointing to same location
#print(d4)
#print(d3)
#print(d3.copy)
#print(d3)
#print(d4)
#del d3['Kapil']
#print(d4) # it deletes from both so better use .copy

#----------------------------------------------------------#
d4 = {'Kapil':"Fruits", "vinod":"Roti", "james":"Biryani",
        "rohan":{"B":"maggie","L":"rice","D":"Chicken"}}

d3 = d4.copy()
del d4['vinod']
#print(d3) # both adress are different so,
#print(d4)
d4.update({'heema':'chocolate'})
#print(d4)
#print(d4.keys())
#print(d4.values())
#print(d4.items())

# Exercise
# # Create a dictionary and take input from user and return the meaning of word from dictionary