a=100
print (a)

# Declare a variable and initialize it
f = 101
print (f)
# Global vs. local variables in functions
def someFunction():
# global f
    f = 'I am learning Python'
    print (f)
someFunction()
print (f)

#using backslash:
print("\"Rakib\"")

#using comments:
"""
I am a good boy
a
apple
bird
"""
#using sum:
sum =  123 +  456 + 100

print(sum);

#using type
print(float(100))
a = 200
b = 33

print(b>a);
print(a>b)
print(a==b)
print(a!=b)
print(10 > 9)
print(10 == 9)
print(10 < 9)

x = 4
x = "Sally"
print(x)

def myfunc():
  global x
  x = "fantastic"
  print(x)

myfunc()

print("Python is " + x)

#multiple strings use:
a='''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#use of libary functio:
print(pow(5,2))
from math import *
print(sqrt(25))

#largest number find in three numbers:

num1= 30
num2=60
num3=40

if num1>num2 :
    if num1>num3:
        print("num1")
    else:
        print(num3)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)

#vowel or consonant check:

ch= str(input( "enter the character:"))
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("vowel")
else:
    print("consonant")






