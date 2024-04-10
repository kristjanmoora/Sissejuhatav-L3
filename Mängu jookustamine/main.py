import pygame
import sys
pygame.init()

# Määrame mõned värvid RGB kujul
lGreen = [153, 255, 153]  
lBlue = [153, 204, 255]  


screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Harjutamine")

# Täidame ekraani heleda rohelise värviga
screen.fill(lGreen)

# Mäng jätkub seni, kuni gameover muutuja väärtus on False
gameover = False

while not gameover:
    # Lisame pildid
    youWin = pygame.image.load("youwin.png")  # Laeme pildi failist youwin.png
    youWin = pygame.transform.scale(youWin, [540, 360])  # Muudame pildi suurust
    screen.blit(youWin, [50, 100])  # Kuvame pildi ekraanile teatud asukohas

    pygame.display.flip()  # Värskendame akent

    # Mängu sulgemine ristist
    for event in pygame.event.get():  # Käime läbi kõik sündmused
        if event.type == pygame.QUIT:  # Kui sündmuse tüüp on "QUIT"
            sys.exit()  # Siis väljume programmist
