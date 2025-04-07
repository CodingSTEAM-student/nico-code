import pygame
import math
pygame.init()


screen = pygame.display.set_mode((1200, 600))
screen_r = screen.get_rect()
clock = pygame.time.Clock()

sheet = pygame.image.load("animations/GandalfHardcore Archer/GandalfHardcore Archer red sheet.png").convert_alpha()
scale = 2
sheet = pygame.transform.scale_by(sheet, scale)

def extract(sheet, frame_size, indexes):
    frames = []
    columns = sheet.width // frame_size[0]
    rows = sheet.height // frame_size[1]

    for index in indexes:
        i = index % columns
        j = index // columns
        x = i * frame_size[0]
        y = j * frame_size[1]
        frame = pygame.Surface(frame_size, pygame.SRCALPHA)
        frame.blit(sheet, (0, 0), (x, y, *frame_size))
        frames.append(frame)
    return frames
idle = extract(sheet, (64 * scale, 64 * scale), [0, 1, 2, 3, 4])
fire = extract(sheet, (64 * scale, 64 * scale), [11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
# shadow = pygame.image.load("assets/shadow.png")
shadow = pygame.Surface((48, 48), pygame.SRCALPHA)
pygame.draw.circle(shadow, (0, 0, 0, 100), (24, 24), 24)
shadow = pygame.transform.scale(shadow, (48, 20))

crosshair = pygame.image.load("animations/crosshairs/Outline/crosshair110.png").convert_alpha()
crosshair = pygame.transform.smoothscale_by(crosshair, 0.5)
# pygame.mouse.set_visible(False)

ground = pygame.image.load("assets/ground_flat_gen.png").convert_alpha()
ground_r = ground.get_rect(bottomleft=screen_r.bottomleft).move(25, 50)

arrow_i = pygame.image.load("animations/GandalfHardcore Archer/arrow.png").convert_alpha()
arrow_i = pygame.transform.scale_by(arrow_i, scale)
arrow_images = {angle: pygame.transform.rotate(arrow_i, angle) for angle in range(-90, 91)}

arrows = []
arrow_speed = 1

archer_r = idle[0].get_rect(center=(160, screen.height * 0.45))
arrow_head = archer_r.move(34, 9).center

goku = pygame.image.load("assets/Goku Blue Whis Gi/Goku-SSJBlue_38.png").convert_alpha()
for x in range(35):
    for y in range(54):
        colour = goku.get_at((x, y))
        if colour == (237, 249, 255):
            goku.set_at((x, y), (0, 0, 0, 0))

goku = pygame.transform.scale_by(goku, 3)
goku = pygame.transform.flip(goku, True, False)
goku_r = goku.get_frect(midbottom=(1150, 500))

animation = idle
index = 0.0
rate = 0.2

arrow_fired = False
arrow_max = 16
arrow_min = 1

gravity = 0.02

mouse = None


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            if animation == idle:
                animation = fire
                index = 0.0
                arrow_fired = False
        if event.type == pygame.MOUSEMOTION:
            _mouse = pygame.math.Vector2(event.pos)
            if _mouse.x > screen_r.width * 0.1:
                mouse = _mouse
    

    for arrow in arrows:
        pos, vel, img = arrow
        vel.y += gravity
        pos.move_ip(*vel)
        if pos.left > screen_r.right or pos.top > screen_r.bottom:
            arrows.remove(arrow)
    
    index += rate
    if index >= len(animation):
        index = 0.0
        if animation == fire:
            animation = idle
    frame = animation[int(index)]

    if animation == fire and index > 8 and not arrow_fired:
        arrow_fired = True
        time_to_target = 2 * clock.get_fps()
        arrow = arrow_i.get_frect(midright=arrow_head)
        arrow_v = pygame.math.Vector2(mouse) - pygame.math.Vector2(arrow.center)
        x_speed = arrow_v.x / time_to_target
        y_speed = time_to_target / 2 * gravity * -1
        delta_y = (arrow_v.y - (1/2) * gravity * time_to_target ** 2) / time_to_target * 2
        y_speed -= delta_y
        angle = math.degrees(math.atan(arrow_v.y / arrow_v.x))
        mapped = (arrow_v.x / screen_r.width) * (arrow_max - arrow_min) + arrow_min 
        # x_speed = math.cos(math.radians(angle)) * mapped
        # y_speed = math.sin(math.radians(angle)) * mapped
        arrow_v.update(x_speed, y_speed)
        arrows.append((arrow, arrow_v, angle))
    
    goku_r.move_ip(-0.2, 0)

    for arrow in arrows:
        if goku_r.colliderect(arrow[0]):
            print("Shot goku", arrow[1])

    screen.fill("skyblue")
    screen.blit(ground, ground_r)

    if mouse:
        pygame.draw.aaline(screen, (255, 255, 255, 50), arrow_head, mouse)

    for arrow  in arrows:
        pos, vel, angle = arrow
        img = arrow_images[int(-angle)]
        screen.blit(img, pos)
    screen.blit(shadow, shadow.get_rect(center=archer_r.midbottom).move(-15, 0))
    screen.blit(frame, archer_r)

    screen.blit(goku, goku_r)
    if mouse:
        screen.blit(crosshair, crosshair.get_rect(center=mouse))

    pygame.display.update()
    clock.tick(60)
