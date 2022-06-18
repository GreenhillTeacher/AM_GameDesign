#MAria Suarez
#06/17/22
#get user name in pygame
import pygame, sys,os

pygame.init()
os.system('cls')

clock= pygame.time.Clock()
backgrndClr=(255,255,255)
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Get Name")
screen.fill(backgrndClr)

run=True #run the while
user_name=''
nameClr=(0,105,105)  #text  the name
bxClr= (200,200,200)  #text b

TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//25)

title=TITLE_FONT.render("Enter Name", 1, bxClr)
screen.blit(title,(200,50))
#make bx
#create rectangle
input_rect = pygame.Rect(WIDTH//3, HEIGHT//3, 140, 32)
while run:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #Menu(mainTitle,messageMenu)
            pygame.quit()
            sys.exit()
            print("You quit")
        if event.type == pygame.MOUSEBUTTONDOWN:
            #drab
            print()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                print(user_name)
                #run main menu
                pygame.quit()
                sys.exit()

            if event.key==pygame.K_BACKSPACE:
                user_name=user_name[:-1]
            else:
                user_name += event.unicode
        pygame.draw.rect(screen, bxClr, input_rect)
  
        text_surface = MENU_FONT.render(user_name, True, nameClr)
        #use your rect x,y to allign ,y text
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
           
        pygame.display.flip()
        
        # clock.tick(60) means that for every second at most
        # 60 frames should be passed.
        clock.tick(60)
