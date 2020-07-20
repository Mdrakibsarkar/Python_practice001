

#Exercise
# Design a calulator which solves the problem for all except the following
# 25 * 3 = 75, 59 + 9 =77, 22/3 =7.0



#solution:
#Num1 = int(input("enter the first number:"))
#Num2 = int(input("enter the second number:"))
#oper=input("enter '+','*','/':")
#if(oper=='+'and (Num1==59 and Num2==9)) or(oper=='*'and (Num1==25 and Num2==3)) or (oper=='/'and (Num1==22 and Num2==3)):
#    print("Error!")
#elif(oper=="+"):
#    print("result of add:",Num1+Num2)
#elif(oper=="*"):
#    print("result of multiply:",Num1*Num2)
#elif(oper=="+"):
#    print("result of divison:",Num1/Num2)
#else:
#    print("Wrong input")

#Solution:
Num1 =input("enter the first number:")
Num2 =input("enter the second number:")
oper=input("enter opertaors:")
faulty_dict={"25*3":"Error!","59+9":"Error!","22/3":"Error"}
expression=Num1 + oper +Num2
           #25      *    3
           #25*3
if expression in faulty_dict.keys():
    print(faulty_dict[expression])
    pass
else:
    print(eval(Num1 + oper +Num2))
             # 25         *        4=100