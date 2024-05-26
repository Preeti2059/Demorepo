import pygame
import sys
#initialize pygame
pygame.init()
#setup the display
WIDTH, HEIGHT=800,600
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint circle  Algorithm")
#colors
WHITE=(123, 231, 111)
BLACK=(10,20,30)




def draw_circle_points(xc, yc, x, y):
    # Draw the eight symmetrical points
    screen.set_at((xc + x, yc + y), WHITE)
    screen.set_at((xc - x, yc + y), "Blue")
    screen.set_at((xc + x, yc - y), "Green")
    screen.set_at((xc - x, yc - y), "Yellow")
    screen.set_at((xc + y, yc + x), "Red")
    screen.set_at((xc - y, yc + x), "Orange")
    screen.set_at((xc + y, yc - x), "Pink")
    screen.set_at((xc - y, yc - x), "Brown")

def midpointCircle(xc,yc,r):
    x=0
    y=r
    p=1-r

    draw_circle_points(xc, yc, x, y)
    while(x<y):
        x=x+1
        if(p<0):
            p=p+2*x+1
        else:
            y=y-1
            p=p+2*x-2*y+1
        draw_circle_points(xc, yc, x, y)


#main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        #clear the screen
        screen.fill(BLACK)
        #draw aline using DDA algorithm
        midpointCircle(300,300,100)
        midpointCircle(400,300,100)
        midpointCircle(500,300,100)
        midpointCircle(350,350,100)
        midpointCircle(450,350,100)
        
        #update the diplay
        pygame.display.flip()

if name== "main":
    main()