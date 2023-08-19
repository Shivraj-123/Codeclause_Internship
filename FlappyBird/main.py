import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

bird = pygame.image.load('bird.png')
pipe = pygame.image.load('pipe.png')
background = pygame.image.load('background.png')

bird_x = 100
bird_y = 300
bird_vy = 0
pipe_x = 800
pipe_y = random.randint(100, 500)
score = 0
font = pygame.font.SysFont('Arial', 32)
ch = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_vy = -6

    bird_y += bird_vy
    bird_vy += 0.5
    pipe_x -= 5

    if bird_y > 600:
        bird_y = -50

    if pipe_x < -50:
        pipe_x = 800
        pipe_y = random.randint(100, 500)
        score += 1

    if bird_x + 50 > pipe_x and bird_x < pipe_x + 50 and (bird_y < pipe_y or bird_y + 50 > pipe_y + 150):
        screen.blit(font.render('Game Over', True, (255, 255, 255)), (300, 180))
        screen.blit(font.render('Would you like to restart ?', True, (255, 255, 255)), (230, 230))
        screen.blit(font.render('Yes Y      no N', True, (255, 255, 255)), (280, 280))
        pygame.display.flip()
        clock.tick(60)
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        bird_x = 100
                        bird_y = 300
                        bird_vy = 0
                        pipe_x = 800
                        pipe_y = random.randint(100, 500)
                        score = 0
                        waiting = False
                    if event.key == pygame.K_n:
                        waiting = False
                        running = False




    else:
        background = pygame.transform.scale(background, (800, 600))
        screen.blit(background, (0, 0))
        bird = pygame.transform.scale(bird, (50, 50))
        screen.blit(bird, (bird_x, bird_y))
        pipe = pygame.transform.scale(pipe, (50, pipe_y))
        screen.blit(pipe, (pipe_x, 0))
        pipe = pygame.transform.scale(pipe, (50, 600 - pipe_y))
        screen.blit(pipe, (pipe_x, pipe_y + 150))
        text = font.render('Score: ' + str(score), True, (255, 255, 255))
        screen.blit(text, (10, 10))
        pygame.display.flip()
        clock.tick(60)

pygame.quit()
