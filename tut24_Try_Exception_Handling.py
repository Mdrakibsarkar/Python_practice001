## Simple example
#a=5
#try:
#     print(a)
#except SyntaxError:                       # NameError is a keyword here
#     print("Variable x is not defined")
#except:                               # Default Except it must be last
#     print("Something else wen wrong")

## With else
#str1="Hello"
#try:
#    print(str1)
#except:
#    print("error in string")
#else:                                ## if try gets error then else block will not executed
#     print("All good")

## finally (keyword) will be executed regardless if the try block raises and error or not
#try:
#     # print(b)
#     print("hello")
#except:
#     print("some error")
#finally:
 #    print("This will printed for sure")



## Using as Exceptiona and as
#try:
#   num1 = int(input("Enter num1: "))
#   num2 = input("Enter num2: ")
#   print("sum =",num1+num2)
#except Exception as e:
#   print(e)
#print("This line is very important")

# Lets try entering alphbetic value first for num1 and then for num2 see the line number will change,
# Error, Problem ?

# print("This line is very important")    # This line doesn't print if above is error

## Solution
#num1 = int(input("Enter num1: "))
#num2 = input("Enter num2: ")
#try:
#     print("sum =",int(num1 )+ int(num2))
#except Exception as e:      # Error is catched in e
#    print(e)

#print("This line is very important")

## Practical use-case for finally
#try:
#     f = open("abc.txt")
#     f.write("did file opened")
#except:
#     print("somethin might have went wrong")
#finally:
#     f.close()

## Using raise: raise an error and stop the program if count if less than 0
#count = -1

#if count < 0:
#     print("worked till here")
#     raise Exception("unable to consider count below 0")

## Excercise
# Using raise with TypeError
#num="hello"
#if type(num) is not int:
#    print("worked till here")
#    raise Exception("only integer show because num is not integer")

#num1 = 5
#num2 = 4
#sum=num1+num2
#print(sum)
#if type(sum) is not str:
#    raise Exception("only show str")
