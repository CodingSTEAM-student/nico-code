import csv
import random

def read_file_data():
    file = open("data.csv", "r", encoding="utf-8")
    data = csv.DictReader(file)
    pokemon = list(data)
    file.close()
    return pokemon


all_pokemon = read_file_data()
name = input("Enter name to search for: ")
for pokemon in all_pokemon:
    if pokemon["name"] == name:
        break

print(pokemon)
image_url = pokemon["image_url"]

import requests
response = requests.get(image_url)

file = open("image.png", "wb")
file.write(response.content)
file.close()