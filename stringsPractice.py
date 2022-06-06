#Maria Isabel
#We are going tV learn abt Strings   '' or ""
import os
import random
os.system('cls')
print('Hi')
print("Hi")
print("Hi, let's go tthe park")
message="You are awesome" #A string is an array characters
#     0  1  2  3  4  5    al arrays begin in zero
#     H  e  l  l  o
print(message)
print(message[5]) # print the letter in position 5
print(message[0:5])  #print all letter from position 0 to 4  5 characters
if message.isdigit(): # isdigit is a method you must use it with a dot
    sum=message +3   #if the statement is true
else:                #if it is false
    print(message+" I say so") #concatenation
print(message.upper())
print(message)
if message.isupper():
    print(message)
else:
    #print("i am in false") #use only for debugging I will delete or com when I am done
    message=message.upper()
    print(message)
print(type(message))
print(help(message.index)) #list  all methods in string
print(help(random.randint))
