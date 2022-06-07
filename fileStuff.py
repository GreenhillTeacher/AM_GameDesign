#Maria Suarez
# Files"
# r read
# w write
# a append
# 
# open files make sure you close the file

import os, datetime
os.system('cls')
name="Maria"
score=120
date=datetime.datetime.now() #todays date and time
print(date.strftime("%m/%d/%Y"))
print(date.strftime("%Y   %m   %d"))
screLine= str(score) + "\t"+name+"\t"+ date.strftime("%m/%d/%Y"+"\n")
print(screLine)
#To  open a file we must create an object
myFile=open("scre.txt", 'w') #open a file to write it clear the file if it exists
myFile.write(screLine)
myFile.close()
myFile=open("scre.txt", 'a') #open a file to write it clear the file if it exists
myFile.write(screLine)
myFile.close()
myFile=open("scre.txt", 'r') #open a file to read
#lines=myFile.readline()
print()
stuff=myFile.readlines()
for line in stuff:
    print(line)
myFile.close()
