import requests
import time

while True:
    cat_url = "https://cataas.com/cat/gif"
    dog_url = "https://random.dog/woof"
    response = requests.get(cat_url)
    # check for any errors when requesting
    if not response.status_code == 200:
        print("Error downloading:", response, response.text)
    else:
        # if no errors, use the downloaded data
        file = open("hello.jpg","wb")
        file.write(response.content)
        file.close()
    time.sleep(5)