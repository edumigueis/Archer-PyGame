import os
import sys
import pygame

pygame.init()
os.chdir(os.path.dirname(__file__))
bitSmall = pygame.font.Font(os.getcwd() + '\\assets\\8bitOperatorPlus-Bold.ttf', 20)
bit = pygame.font.Font(os.getcwd() + '\\assets\\8bitOperatorPlus-Bold.ttf', 60)
bitExtraSmall = pygame.font.Font(os.getcwd() + '\\assets\\8bitOperatorPlus-Bold.ttf', 15)

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
player_shoot = pygame.image.load("assets/archer2.png")
player = pygame.transform.scale(player, (300, 300))
player_shoot = pygame.transform.scale(player_shoot, (300, 300))
arrow = pygame.image.load("assets/arrow.png")
target = pygame.image.load("assets/target.png")
target = pygame.transform.scale(target, (170, 279))
target_lightning = pygame.image.load("assets/target_lightning.png")
target_lightning = pygame.transform.scale(target_lightning, (215, 690))
is_shooting = False
rect_y = 270
is_moving_down = True
shock_x = 1
points = 0

def gameplay():
    playery = 0
    playerx = -80

    gQuit = False
    screen.blit(bg, (0, 0))
    global is_shooting
    is_shooting = False
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
                        screen.blit(player_shoot, (playerx, playery))
                        pygame.display.update()
                        is_shooting = True
                        pygame.event.set_blocked(pygame.KEYDOWN)
                        shoot(playery, playerx + 30)

                    if event.key == pygame.K_ESCAPE:
                        gQuit = True
                        introScreen()
                        return True

            if not is_shooting:
                pygame.event.set_allowed(pygame.KEYDOWN)
                screen.blit(bg, (0, 0))
                screen.blit(player, (playerx, playery))

            global rect_change_y
            global rect_y
            global is_moving_down
            global shock_x

            shock_x = -shock_x
            if is_moving_down == True:
                rect_y += 2
                if rect_y > height/7:
                    rect_y += 1
                if rect_y > height/5:
                    rect_y += 1
                if rect_y > height/4:
                    rect_y += 2
                if rect_y > height/3:
                    rect_y += 2
            else:
                rect_y -= 2

            if rect_y > height - 275:
                is_moving_down = -is_moving_down
                rect_y = 275
            elif rect_y < 0:
                is_moving_down = -is_moving_down
                rect_y = 0

            if is_moving_down == True:
                screen.blit(target, (width - 174, rect_y))
            else:
                screen.blit(target_lightning, (width - 200 - shock_x, rect_y))
            
            global points
            pt = bitSmall.render(str(points), True, (250, 250, 250))
            screen.blit(pt, (width - 75, 20))

            pygame.display.update()

        clock.tick(FPS)


def shoot(yStart, xStart):
    arrowX = xStart + 70
    global is_moving_down
    global rect_y
    global shock_x
    global points
    crashed = False

    while arrowX < width:
        screen.blit(bg, (0, 0))
        screen.blit(player_shoot, (xStart - 30, yStart))
        screen.blit(arrow, (arrowX, yStart + 90))
        pt = bitSmall.render(str(points), True, (250, 250, 250))
        screen.blit(pt, (width - 75, 20))

        arrowX += 20
        shock_x = -shock_x

        if is_moving_down == True:
                rect_y += 2
                if rect_y > height/7:
                    rect_y += 1
                if rect_y > height/5:
                    rect_y += 1
                if rect_y > height/4:
                    rect_y += 2
                if rect_y > height/3:
                    rect_y += 2
        else:
            rect_y -= 2

        if rect_y > height - 275:
            is_moving_down = -is_moving_down
            rect_y = 275
        elif rect_y < 0:
            is_moving_down = -is_moving_down
            rect_y = 0

        if is_moving_down == True:
            screen.blit(target, (width - 174, rect_y))
        else:
            screen.blit(target_lightning, (width - 200 - shock_x, rect_y))

        pygame.display.update()
 
        if arrowX > width - 100 and yStart + 90 > rect_y - 40 and yStart + 90 < rect_y + 150 and crashed == False:
            if yStart >= rect_y and yStart < rect_y + 40:
                points+=10;
            elif yStart <= rect_y and yStart > rect_y - 30:
                points+=20;
            elif yStart <= rect_y and yStart > rect_y - 50:
                points+=30;
            elif yStart <= rect_y and yStart > rect_y - 60:
                points+=40;
            elif yStart <= rect_y and yStart > rect_y - 70:
                points+=30;
            elif yStart <= rect_y and yStart > rect_y - 100:
                points+=20;
            elif yStart <= rect_y and yStart > rect_y - 170:
                points+=10;
            crashed = True

        if arrowX > width - 100:
            global is_shooting
            is_shooting = False


def introScreen():
    backToMain = False
    while not backToMain:
        global points
        points = 0
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
            screen.blit(text, (width/3 - 37, height/2 + 60))
            sub = bitExtraSmall.render(
                "Points: yellow- 40, red- 30, black- 20, white- 10", True, (250, 250, 250))
            screen.blit(sub, (20, height - 30))
            pygame.display.update()
        else:
            print(errMsg)

        clock.tick(FPS)


def main():
    introScreen()


main()
