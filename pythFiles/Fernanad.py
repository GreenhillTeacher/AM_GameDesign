# Fernando Guota
# Number Guessing game
    # pseudocode. make menu, give option to input number for each option in menu.
    # each will be guided by a function, ex: if choice == 1 print rules or smthn like that
    # for the actual game make lists of numbers and have function to bring player to it, let the player have 25 guesses max(thats is a lot may chaneg later)
    # for soreboard, make file and desplay that when they go to view score, will do top 10 high score displayed
    # to exit game will program so when input 6 code simply stops running 
#steps: 1.instructions 2.level1 num 1-25 3.level2 num 1-50 4.level3 num 1-100 5.prt score 6.exit
import random
import os, datetime
date=datetime.datetime.now()
os.system('cls')
Game=True
cnt=0
high=0
score=0
check=False
cscore=0
name=input("What is your name? ")
def Menu(choice):#function to make menu work
    global check, num, Game
    if choice ==1:
        print("In this game your goal is to guess a number. There are 3 different lvls, numbers 1-25, 1-50 and 1-100")
        print("you have 5 guesses")
        input("press enter to return to menu") #this displays the instuctions 
        check=False 
    
    if choice ==2:
        num = random.randint(1,25)
        check=True
    if choice ==3:
        num = random.randint(1,50) #these here will generate the number for the different lvl 
        Check=True
    if choice ==4:
        num = random.randint(1,100)
        Check=True
    if choice ==5:
        File=open("scre.txt",'r') #this opens a file to read
        stuff=File.readlines() #should show highscore,r n not work
        File.close()
        for line in stuff:
            print (line)
        check=False 
    if choice ==6:
        Game=False
        check=False
        print("thanks for playing")
        input("press enter to play again?") #this is the exit part of the function 
        # with open("cscore.txt",'r') as f:
        #     f.truncate(0) #this clears the  cscore file which keeps the score from teh different levels and ads it up to make the total score 
        
while Game:
    print("|****************************************|")
    print("|         NUMBER GUESSING GAME           |")
    print("|            1.Instructions              |")
    print("|              2.Level 1                 |")
    print("|              3.Level 2                 |")
    print("|              4.Level 3                 |")
    print("|            5.Score Board               |")
    print("|                6.EXIT                  |")
    print("|****************************************|")

    print(name, end=", ")
    choice= input("what would you like to do. imput number here: ")
    choice=int(choice)
    Menu(choice)
    cnt=0
    while check and cnt <5:
        guess=int(input("plese put your guess here: "))
        print()
        if guess == num:
            print("Congrats, You got it")
            check=False
        cnt+=1   
        if cnt ==5:
            print("sorry! Thats the max guesses")            
    cscore=2000-cnt*100
    #Highest

    input("press enter to return to menu")
# File=open("cscores.txt",'w') #this creates a score from this game 
# File.write (str(cscore)) #scores are together in a seperate file
# File.close()
#with open("cscores.txt") as f:
  #  score=(sum(float(line)for line in f))#added together to make a total score 
  #  if score > high:
   #         high=score  
File=open("scre.txt",'a')
screline=str(score)+"\t"+name+"\t"+ date.strftime("%m/%d/%Y")
File.write=(screline)
File.close() #this adds that score to the scoreboard 