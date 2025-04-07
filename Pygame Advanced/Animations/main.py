import pygame
pygame.init()


screen = pygame.display.set_mode((400, 400))
screen_r = screen.get_rect()
clock = pygame.time.Clock()

sheet = pygame.image.load("animations\Male_spritesheet_run.png").convert_alpha()
sheet = pygame.transform.smoothscale_by(sheet, 2)

columns = 10
total = 18
frame_size = sheet.width // columns
animation = []
for i in range(total):
    frame = pygame.Surface((frame_size, frame_size), pygame.SRCALPHA)
    x = frame_size * (i % columns)
    y = frame_size * (i // columns)
    frame.blit(sheet, (0, 0), (x, y, frame_size, frame_size))
    animation.append(frame)

index = 0.0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    index += 0.1
    if index >= len(animation):
        index = 0
    frame = animation[int(index)]
    
    screen.fill("black")
    screen.blit(frame, frame.get_rect(center=screen_r.center))

    pygame.display.update()
    clock.tick(60)
