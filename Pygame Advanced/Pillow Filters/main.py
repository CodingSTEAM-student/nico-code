from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
screen_r = screen.get_rect()
clock = pygame.time.Clock()

# image pre-processing
image = pygame.image.load("cardback.png").convert()
image = pygame.transform.smoothscale_by(image, 0.5)
im_size = image.get_size()
image_bytes = pygame.image.tobytes(image, "RGBA")

threshold = 0

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # real-time image processing
    image_pil = Image.frombytes("RGBA", im_size, image_bytes).convert("RGB")
    image_pil = ImageOps.solarize(image_pil, threshold)
    image_pil = image_pil.filter(ImageFilter.GaussianBlur(threshold / 15))
    image_final = pygame.image.frombytes(image_pil.tobytes(), im_size, "RGB")
    
    image_r = image_final.get_rect(center=screen_r.center)

    # rendering
    screen.blit(image_final, image_r)
    pygame.display.update()
    clock.tick(30)

    if threshold < 255:
        threshold += 4
    else:
        threshold = 0

