import requests
import json
import random


url = "https://wttr.in/@@@?format=j2"
city = "London"
response = requests.get(url.replace("@@@", city))

if response.status_code == 200:
    # convert the text to json data
    data = json.loads(response.text)
    current = data["current_condition"][0]
    
    description = current["weatherDesc"][0]["value"]
    temperature = current["temp_C"]
    wind = current["windspeedKmph"]



print("In", city, "it is", description, "with a temperature of", temperature, "and wind speed of", wind)




api_key = "PTbUrCpvqyYgk51vvHReTISgDxSqufjF5HcRXrMquOBtlWctBMcVED81"
url = "https://api.pexels.com/v1/search"
security = {
    "Authorization": api_key
}
data = {
    "query": description + " " + city + " landscape weather city",
    "per_page": 10
}

response = requests.get(url, headers=security, params=data)

print(response)
random_number = random.randint(0, 9)
image_url = json.loads(response.text)["photos"][random_number]["src"]["original"]
print(image_url)


response = requests.get(image_url)
file = open("image.jpeg", "wb")
file.write(response.content)
file.close()


import pygame
pygame.init()

screen = pygame.display.set_mode((1500, 800))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()
font_large = pygame.font.Font("GrapeNuts-Regular.ttf", 80)
image = pygame.image.load("image.jpeg")
image = pygame.transform.smoothscale_by(image, 0.25)

image_rect = image.get_rect(center=screen_rect.center)

text_city = font_large.render("Location: " + city, True, "white")
text_city_rect = text_city.get_rect(center=(screen_rect.width * 0.5, screen_rect.height * 0.2))
text_temperature = font_large.render(temperature + "ºC", True, "white")
text_temperature_rect = text_temperature.get_rect(center=(screen_rect.width * 0.5, screen_rect.height * 0.33))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("black")

    screen.blit(image, image_rect)
    screen.blit(text_city, text_city_rect)
    screen.blit(text_temperature, text_temperature_rect)

    pygame.display.update()
    clock.tick(30)
