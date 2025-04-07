from PIL import Image, ImageFilter, ImageEnhance
import csv
import random

def read_file_data():
    file = open("data.csv", "r", encoding="utf-8")
    data = csv.DictReader(file)
    pokemon = list(data)
    file.close()
    return pokemon


all_pokemon = read_file_data()
# name = input("Enter name to search for: ")
# for pokemon in all_pokemon:
#     if pokemon["name"] == name:
#         break
pokemon = {"name": ""}
while "GX" not in pokemon["name"]:
    pokemon = random.choice(all_pokemon)

image_url = pokemon["image_url"]

import requests
response = requests.get(image_url)

file = open("image.png", "wb")
file.write(response.content)
file.close()

import pygame

screen = pygame.display.set_mode((1800, 1000))
clock = pygame.time.Clock()
image = pygame.image.load("image.png")
# convert image to byte representation
image_bytes = pygame.image.tobytes(image, "RGBA")

cardback = pygame.image.load("cardback.png")
scale = 1.0
cardback = pygame.transform.smoothscale_by(cardback, scale)

image_rect = image.get_rect()
cardback_rect = cardback.get_rect()
cardback_rect_2 = cardback.get_rect()

cardback_rect.centerx = screen.get_width() * 0.33
cardback_rect_2.centerx = screen.get_width() * 0.66
cardback_rect.centery = screen.get_height() / 2
cardback_rect_2.centery = screen.get_height() / 2


size = 5
speed = 1
aspect_ratio = image.get_height() / image.get_width()

show_card = False
amount = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_position = event.pos
            if cardback_rect.collidepoint(clicked_position):
                show_card = True
        

    screen.fill("black")
    screen.blit(cardback, cardback_rect)
    screen.blit(cardback, cardback_rect_2)

    if show_card:
        scaled_image = pygame.transform.scale(image, (size, aspect_ratio * size))
        # load the image bytes into Pillow
        pil_image = Image.frombytes("RGBA", image.size, image_bytes)
        # apply the image transformations
        # blur
        pil_image = pil_image.filter(ImageFilter.BoxBlur(amount))
        amount = amount - 1
        
        # re-convert the image bytes to allow pygame to use the image
        filtered_bytes = pil_image.tobytes()
        image = pygame.image.frombytes(filtered_bytes, image.size, "RGBA")

        screen.blit(image, cardback_rect)

    pygame.display.update()
    clock.tick(30)

    size = size + int(speed)
    speed = speed + 0.5
    if size > 500 or size < 5:
        speed = speed * -1

    if size < 10:
        size = 10
    elif size > 490:
        size = 490
