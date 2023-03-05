import pygame

pygame.init()

window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption("Futeball Pong")

field = pygame.image.load("assets/assets/field.png")

player1 = pygame.image.load("assets/assets/player1.png")
player1_y = 310

player2 = pygame.image.load("assets/assets/player2.png")

ball = pygame.image.load("assets/assets/ball.png")
ball_x = 617
ball_y = 337


def move_ball():
    global ball_x
    global ball_y

    ball_x += 1


def draw():
    window.blit(field, (0, 0))
    window.blit(player1, (50, player1_y))
    window.blit(player2, (1150, 310))
    window.blit(ball, (ball_x, ball_y))


loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                player1_y -= 10
            if events.key == pygame.K_s:
                player1_y += 10

    draw()
    move_ball()
    pygame.display.update()