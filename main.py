import pygame
import random

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра тир')
icon = pygame.image.load('assets/image/gunman.jpeg')
pygame.display.set_icon(icon)


target_img = pygame.image.load("assets/image/apple.png")
crosshair_img = pygame.image.load("assets/image/crosshair.jpg").convert_alpha()
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
pygame.mixer.init()
click_sound = pygame.mixer.Sound('assets/sounds/click.wav')

pygame.mouse.set_visible(False)

run = True
while run:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            click_sound.play()

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x+target_width and target_y < mouse_y < target_y+target_height:
                target_x = random.randint(0,SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            crosshair_rect = crosshair_img.get_rect(center=(mouse_x, mouse_y))





    # Отрисовка цели
    screen.blit(target_img, (target_x, target_y))

    # Получение позиции мыши и отрисовка прицела
    mouse_x, mouse_y = pygame.mouse.get_pos()
    crosshair_rect = crosshair_img.get_rect(center=(mouse_x, mouse_y))
    screen.blit(crosshair_img, crosshair_rect)

    pygame.display.update()





pygame.quit()