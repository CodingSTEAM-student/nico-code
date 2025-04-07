import random
import requests

# choice of apis
rollercoaster_url = "https://captaincoaster.com/api/images/"
rollercoaster_api = "5320eb8c-2cfd-44e7-af8a-bcecd38be0b9"

# request example
authorisation = {"Authorization": rollercoaster_api}
parameters = {"page": random.randint(1, 570)}
response = requests.get(rollercoaster_url, headers=authorisation, params=parameters)
# check for any errors when requesting
if not response.status_code == 200:
    print("Error downloading:", response, response.text)
    exit()

# if no errors, use the downloaded data
data = response.json()
print(data)
results = data["hydra:member"]
print(len(results))
result = random.choice(results)
id = result["@id"]
complete_url = rollercoaster_url[:26] + "/" + id
print(id)
response = requests.get(complete_url, headers=authorisation)
data = response.json()
print(data.keys())
image_url = "https://pictures.captaincoaster.com/1440x1440/" + data["path"]
response = requests.get(image_url, headers=authorisation)

# save to an image file on disk
file = open("image.jpg", "wb")
file.write(response.content)
file.close()

import pygame
pygame.init()

screen_width = 1440 * 0.75
screen_height = 1080 * 0.75
screen = pygame.display.set_mode((screen_width, screen_height))

image = pygame.image.load("image.jpg")

scale = 0.01
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    scaled = pygame.transform.smoothscale_by(image, scale)
    rect = scaled.get_rect(center=(1440//2, 1080//2))
    screen.blit(scaled, rect)
    pygame.display.update()

    scale += 0.01