import requests
import random

url = "https://captaincoaster.com/api/images"
api_key = "5320eb8c-2cfd-44e7-af8a-bcecd38be0b9"

authorisation = {"Authorization": api_key}
response = requests.get(url, headers=authorisation)
if not response.ok:
    print("Download failed", response)
    print(response.text)
    exit()


data = response.json()
coasters = data["hydra:member"]
print("Downloaded", len(coasters), "coasters")

print("Coaster index 0:")
coaster = random.choice(coasters)
for key, value in coaster.items():
    print("  ", repr(key), ":::", repr(value))


print("Downloading image metadata...")
url = "https://captaincoaster.com" + coaster["coaster"]
response = requests.get(url, headers=authorisation)

if not response.ok:
    print("Error downloading image", response)
    print(response.text)
    exit()

print()
data = response.json()
print(data)



print("Downloading image...")
image_url = "https://pictures.captaincoaster.com/1440x1440/" + coaster["path"]
response = requests.get(image_url, headers=authorisation)

if not response.ok:
    print("Error downloading image", response)
    print(response.text)
    exit()

print("Downloaded image successfully")
file = open("image.jpg", "wb")
file.write(response.content)
file.close()
