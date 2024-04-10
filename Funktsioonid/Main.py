# Kristjan Moora
import pygame
import sys
import random

pygame.init()  

# Määrame mõned värvid RGB kujul
red = [255, 0, 0]  
green = [0, 255, 0]  
blue = [0, 0, 255]  
pink = [255, 153, 255]  
lGreen = [153, 255, 153]  

# Seadistame ekraani mõõtmed 640x480 pealkirja Harjutamine
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Harjutamine")

# Täidame ekraani heleda rohelise värviga
screen.fill(lGreen)

# Defineerime funktsiooni drawHouse, mis joonistab maja
def drawHouse(x, y, width, height, screen, color):
    # Määrame maja nurkade koordinaadid
    points = [(x, y - ((3 / 4.0) * height)), (x, y), (x + width, y), (x + width, y - (3 / 4.0) * height),
              (x, y - ((3 / 4.0) * height)), (x + width / 2.0, y - height), (x + width, y - (3 / 4.0) * height)]
    lineThickness = 2  # Määrame joonte paksuse
    pygame.draw.lines(screen, color, False, points, lineThickness)  # Joonistame maja

# Kutsume funktsiooni välja ja joonistame maja
drawHouse(100, 400, 300, 200, screen, red)

pygame.display.flip()  # Värskendame akent
