#Maria Suarez
#6/9/2022
#We are learning pygame basic functins, 
# creating screens, clrs, shape
# K_UP                  up circle
# K_DOWN                down circle
# K_RIGHT               right circle
# K_LEFT                left circle
# K_a                   left square
# K_d                   right square
# K_w                   up square
# K_s                   down square

import random
import pygame, time,os, math
clock=pygame.time.Clock()    #optimizing the speed of the game  look at last statement

#initialize the pygame package
os.system('cls')
WIDTH=900 #like constant
HEIGHT=600
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51),"purple":(127,0,255)}
clr=colors.get("limeGreen")
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  #change the title of my window
#var for the square
hb=50
wb=50
xb=100
yb=300
square=pygame.Rect(xb,yb,wb,hb)# create the object to draw
squareClr=colors.get("pink")


#var for the circle
cx=350
cy=350
rad=25
#inscribe square
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)
insSquare=pygame.Rect(xig,yig, ibox,ibox)
speed=5
circleClr=colors.get("blue")
#keep running create a lp
backgrnd=clr
run = True
while run:
    screen.fill(backgrnd)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            print("Y quit")
    keys=pygame.key.get_pressed() #prvide a list ll keys
    if keys[pygame.K_a ] and square.x> speed:
        square.x -=speed
    if keys[pygame.K_d] and square.x < WIDTH-(wb+speed):
        square.x +=speed
    if keys[pygame.K_w ] and square.y> speed:
        square.y -=speed
    if keys[pygame.K_s] and square.y < HEIGHT-(hb+speed):
        square.y +=speed
    if keys[pygame.K_LEFT ] and cx> (speed+rad):
        cx -=speed
        insSquare.x -=speed
    if keys[pygame.K_RIGHT] and cx < WIDTH-(rad+speed):
        cx +=speed
        insSquare.x +=speed
    if keys[pygame.K_UP] and cy> (rad+speed):
        cy -=speed
        insSquare.y -=speed
    if keys[pygame.K_DOWN] and cy < HEIGHT-(rad+speed):
        cy +=speed
        insSquare.y +=speed
    #rect(surface, color, rect) -> Rect
    #if square.collidepoint((cx,cy)):
    if square.colliderect(insSquare):
        print("BOOM")
        cx=random.randint(rad,WIDTH-rad)
        cy=random.randint(rad, HEIGHT-rad)
        rad +=5
        ibox = rad*math.sqrt(2)
        xig = cx-(ibox/2)
        yig = cy-(ibox/2)
        insSquare=pygame.Rect(xig,yig, ibox,ibox)

    pygame.draw.rect(screen, squareClr,square)
    #circle(surface, color, center, radius)
    pygame.draw.rect(screen, backgrnd, insSquare)
    pygame.draw.circle(screen, circleClr, (cx,cy), rad)  #circle is not an object use variables 

    pygame.display.update()
    clock.tick(60)


