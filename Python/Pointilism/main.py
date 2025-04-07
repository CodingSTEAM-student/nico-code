import pygame
import random

pygame.init()

image = pygame.image.load("moonwalk.jpg")
image = pygame.transform.smoothscale_by(image, 2)

screen = pygame.display.set_mode(image.get_size())
screen_r = screen.get_rect()
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # pick an x and y coordinate
    x = 100
    y = 100
    # sample the image at that coordinate
    colour = image.get_at((x, y))

    # draw a circle (or other shape) at that coordinate
    pygame.draw.circle(screen, colour, (x, y), 4)

    pygame.display.update()
    clock.tick(60)
