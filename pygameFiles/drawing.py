#Maria 
#Drawing lines
import pygame


import pygame
pygame.init()

WIDTH=600
HEIGHT=600
line_width = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

colors={"lightyellow":(252, 243, 207),"black":(51,0,102),"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51), "cream":(255, 255, 210),"cyan":(5, 156, 150)}
bg = colors.get("cream")
gridClr = colors.get("cyan")
while True:
    screen.fill(bg)
    for x in range(1,3):
        #horizontal line
        pygame.draw.line(screen, gridClr, (0, WIDTH//3 * x), (WIDTH,WIDTH//3 * x), line_width)
        #vertical  line
        pygame.draw.line(screen, gridClr, (HEIGHT//3 * x, 0), (HEIGHT//3 * x, HEIGHT), line_width)
        pygame.time.delay(1000)
        pygame.display.update()
    pygame.time.delay(1000)
    break