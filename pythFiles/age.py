#Maria Suarez
#Calculate age
#get user year and current year
import os  #library to clear screen
os.system('cls')
by=2001 #assign this value as a number   
#by = input('year you were born, ') give us a string
by = int( input('year you were born, ')) #typecast
currentYear=2022 #alsa number
age =currentYear-by
print('Your age is ',age)
#Selection
if age >50:
    print('You are old')