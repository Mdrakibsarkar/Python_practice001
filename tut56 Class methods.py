# example 1 : How to change class varibale by decorator without using self
## Constructor = to make Employee class to take argument

class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole): # This is constructor
        self.name=aname       # name is instance variable and aname is just an argument
        self.salary=asalary
        self.role=arole
        print("enter counstruct name:",aname)

    # classmethond used to reduce latency as self is not used , example games
    # Benifit of classmethod is that it can be used as an alternative constructor
    @classmethod       # way to give access to class objects/instances to change class variable ie. no.of.leaves
    def change_leaves(cls,new_leaves):    # cls is just a class which is called by class name or instance name
        cls.no_of_leaves=new_leaves
kapil= Employee("kapil","4000","manager")
# rohan = Employee() # Employee("rohan",3000,"Principal")
print(kapil.no_of_leaves) #before

kapil.change_leaves(45)
print(kapil.no_of_leaves) #after

Employee.change_leaves(23)
print(kapil.no_of_leaves)

