import random
for x in range(6):
    guess=input("enter the number 0 to 5:")
    randomnumber= random.randint(1,5)
    if guess==randomnumber:
        print("you have win")
    else:
        print("you have lost")

