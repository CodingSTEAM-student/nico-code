import random

import pygame
pygame.init()


images = [
    pygame.image.load(f"assets/isometric-nature-pack/grass{x}.png")
    for x in range(1, 7)
]

rows = 7
columns = 10
size = images[0].width
v_gap = -20
h_gap = -10
perspective = 0.85

resolution = ((size // 2 + h_gap) * (columns + 0.5) * 2, (size + v_gap * 2) * (rows + 2) * 0.5)
screen = pygame.display.set_mode(resolution)
screen_r = screen.get_rect()
clock = pygame.time.Clock()

speed = 0
_speed = 0.1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                v_gap -= 0.1
            elif event.key == pygame.K_DOWN:
                v_gap += 0.1
            elif event.key == pygame.K_RIGHT:
                h_gap += 0.1
            elif event.key == pygame.K_LEFT:
                h_gap -= 0.1
            elif event.key == pygame.K_SPACE:
                if speed:
                    _speed = speed
                    speed = 0
                else:
                    speed = _speed
            elif event.key == pygame.K_RETURN:
                pygame.image.save(surface, "assets/ground_flat_gen.png")

            print(f"{h_gap = } {v_gap = }")
    
    surface = pygame.Surface((screen.size[0] * 1.2, screen.size[1] * 1.2), pygame.SRCALPHA)

    # random.seed(0)
    for j in range(0, rows):
        h_offset = j % 2 == 0
        for i in range(h_offset, columns * 2, 2):
            image = random.choice(images)
            x = i * (size // 2 + h_gap)
            v_offset = j * (size // 2 + v_gap)
            surface.blit(image, image.get_frect(bottomleft=(x, v_offset + size * 1.1)))
    surface = pygame.transform.smoothscale(surface, (surface.width, surface.height * perspective))
    
    screen.fill("black")
    screen.blit(surface)

    pygame.display.update()
    clock.tick(60)

    if speed:
        h_gap += speed
        v_gap += speed / 2
        if h_gap >= 20 or h_gap <= -10:
            speed *= -1
