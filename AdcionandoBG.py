import pygame

pygame.init()

window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption("Futebal Pong")

field = pygame.image.load("assets/assets/field.png")
window.blit(field, (0, 0))


loop = True
while loop:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

    pygame.display.update()