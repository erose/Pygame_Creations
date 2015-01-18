import pygame, sys, math
from pygame.locals import *
mouseIsDown = False
white = (255, 255, 255)

#integer between 0 (everything is black) and 255 (maximally bright)
brightness = 255

class Brush:
    size = 0
    color = white
    
    def cycleColor(self):
        r, g, b = self.color
        r = (r + 3) % 255
        g = (g + 2) % 255
        b = (b + 1) % 255
        self.color = (r, g, b)
    
    def incrementSize(self):
        self.size += 1
        if self.size > 30: self.size -= 1

#set up screen
pygame.init()
screen = pygame.display.set_mode((640, 480))

#set up background (a white rectangle)
background = pygame.Surface(screen.get_size()).convert()
background.fill(white)

screen.blit(background, (0, 0))
pygame.display.flip()

def norm_cos(x, offset):
    return int((brightness // 2) * (math.cos(x + (offset * math.pi)) + 1))

def cycleColor():
    global brightness

    x = 0
    while True:
        for brightness in range(0, 255, 1):
            x += (1.0/255) * (2 * math.pi)

            r = norm_cos(x, 0)
            g = norm_cos(x, 2.0 / 3.0)
            b = norm_cos(x, 4.0 / 3.0)

            yield r, g, b

b = Brush()
colorCyclingGenerator = cycleColor()
while True: # loop forever (or at least until someone generates a QUIT event)
    if mouseIsDown:
        b.incrementSize()
        pygame.draw.circle(background, b.color, (event.pos[0], event.pos[1]), b.size)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION and mouseIsDown:
            b.color = next(colorCyclingGenerator)
        if event.type == MOUSEBUTTONDOWN:
            mouseIsDown = True
            pygame.draw.circle(background, b.color, (event.pos[0], event.pos[1]), b.size)
        if event.type == MOUSEBUTTONUP:
            mouseIsDown = False
    screen.blit(background, (0, 0))
    pygame.display.flip()