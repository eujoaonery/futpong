import pygame

pygame.init()

window = pygame.display.set_mode([1280, 720])
window_title = pygame.display.set_caption("Futeball Pong")

field = pygame.image.load("assets/assets/field.png")
window.blit(field, (0, 0))

player1 = pygame.image.load("assets/assets/player1.png")
window.blit(player1, (50, 280))

player2 = pygame.image.load("assets/assets/player2.png")
window.blit(player2, (50, 1150))

ball = pygame.image.load("assets/assets/ball.png")
window.blit(ball, (617, 337))


loop = True
while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    pygame.display.update()