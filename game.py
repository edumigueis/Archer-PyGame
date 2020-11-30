import os
import sys
import pygame

pygame.init()
bitSmall = pygame.font.Font('assets/8bitOperatorPlus-Bold.ttf', 20)
bit = pygame.font.Font('assets/8bitOperatorPlus-Bold.ttf', 60)

scr_size = (width, height) = (1018, 549)
width = 1018
height = 549
FPS = 60

errMsg = "Pygame display surface not rendering."

white = (240, 240, 240)
background_col = (142, 192, 215)

screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()
pygame.display.set_caption("Archer Game")
bg = pygame.image.load("assets/bg.png")
player = pygame.image.load("assets/archer1.png")
playerShoot = pygame.image.load("assets/archer2.png")
player = pygame.transform.scale(player, (300, 300))
playerShoot = pygame.transform.scale(playerShoot, (300, 300))
arrow = pygame.image.load("assets/arrow.png")
target = pygame.image.load("assets/target.png")
target = pygame.transform.scale(target, (170, 279))
isShooting = False
rect_change_y = 2
rect_y = 50

def gameplay():
    playery = 0
    playerx = -80

    gQuit = False
    screen.blit(bg, (0, 0))
    global isShooting
    isShooting = False
    while not gQuit:
        if pygame.display.get_surface() == None:
            print(errMsg)
            return True
        else:
            keys = pygame.key.get_pressed()  # checking pressed keys

            if keys[pygame.K_UP] or keys[pygame.K_w]:
                if playery > -50:
                    playery -= 3.5

            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                if playery < 300:
                    playery += 3.5

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gQuit = True
                    return True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        screen.blit(bg, (0, 0))
                        screen.blit(playerShoot, (playerx, playery))
                        pygame.display.update()
                        isShooting = True
                        pygame.event.set_blocked(pygame.KEYDOWN)
                        shoot(playery, playerx + 30)

                    if event.key == pygame.K_ESCAPE:
                        gQuit = True
                        introScreen()
                        return True

            if not isShooting:
                pygame.event.set_allowed(pygame.KEYDOWN)
                screen.blit(bg, (0, 0))
                screen.blit(player, (playerx, playery))

            global rect_change_y
            global rect_y
            rect_y += rect_change_y
            if rect_y > height - 275 or rect_y < 0:
                rect_change_y = rect_change_y * -1
            
            screen.blit(target, (width - 200, rect_y))
            pygame.display.update()

        clock.tick(FPS)


def shoot(yStart, xStart):
    arrowX = xStart + 70
    global rect_change_y
    global rect_y
    while arrowX < width:
        arrowX += 20
        screen.blit(bg, (0, 0))
        screen.blit(playerShoot, (xStart - 30, yStart))
        screen.blit(arrow, (arrowX, yStart + 90))
        rect_y += rect_change_y * 0.5
        if rect_y > height - 275 or rect_y < 0:
            rect_change_y = rect_change_y * -1
        screen.blit(target, (width - 200, rect_y))
        pygame.display.update()

        """if arrowX > width - 100 and yStart == rect_y: # DETECTAR COLISÃO
            print("colide")"""

        if arrowX > width - 100:
            global isShooting
            isShooting = False


def introScreen():
    backToMain = False
    while not backToMain:
        screen.blit(bg, (0, 0))
        if pygame.display.get_surface() == None:
            print(errMsg)
            return True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    gameplay()
                    backToMain = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    gameplay()
                    backToMain = True
        if pygame.display.get_surface() != None:
            title = bit.render("Archer Game", True, (250, 250, 250))
            screen.blit(title, (width/3 - 25, height/2 - 30))
            text = bitSmall.render(
                "Press space or enter to star the game.", True, (250, 250, 250))
            screen.blit(text, (width/3 - 25, height/2 + 60))
            pygame.display.update()
        else:
            print(errMsg)

        clock.tick(FPS)


def main():
    introScreen()


main()
