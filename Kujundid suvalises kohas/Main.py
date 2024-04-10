# Kristjan Moora
import pygame
import random 

pygame.init()  

# Määrame värvid RGB kujul
red = [255, 0, 0]  
lGreen = [153, 255, 153]  

# Seadistame ekraani mõõtmed 640x480 pealkirjaga Harjutamine
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Harjutamine")

# Täidame ekraani heleda rohelise värviga
screen.fill(lGreen)

# Juhuslikult valime 10 korda ruudu asukoha ja joonistame selle punaseks. Iga ruut on suurusega 20x20 pikslit.
for i in range(1, 10):
    x = random.randint(0, 620)  # Genereerime juhusliku x-koordinaadi
    y = random.randint(0, 460)  # Genereerime juhusliku y-koordinaadi
    pygame.draw.rect(screen, red, [x, y, 20, 20])  # Joonistame ruudu ekraanile

    pygame.display.flip()
