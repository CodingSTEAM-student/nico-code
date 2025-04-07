import requests

# choice of apis
weather_url = "https://goweather.herokuapp.com/weather/"
pokemon_url = "https://api.pokemontcg.io/v2/cards/?q=name:ponyta"
pokemon_api_key = "7e0632a2-84cd-4a05-a18b-156063dddb31"
trivia_url = "https://opentdb.com/api.php?amount=1&category=9"


# request example
authorisation = {"X-Api-Key": pokemon_api_key}
response = requests.get(pokemon_url, headers=authorisation)
# check for any errors when requesting
if not response.status_code == 200:
    print("Error downloading:", response, response.text)
else:
    # if no errors, use the downloaded data
    data = response.json()
    results = data["data"]
    print(results[0].keys())

