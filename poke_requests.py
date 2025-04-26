import requests
from PIL import Image
from io import BytesIO


API_URL = "https://pokeapi.co/api/v2"
POKE_IMAGE_URL = "https://veekun.com/dex/media/pokemon/global-link"
num= 124

def poke_name(name):
    URL = f"{API_URL}/pokemon/{name}"
    response = requests.get(URL)
    print(response)

def pokemon_api_display(number):
    URL = URL = f"{API_URL}/pokemon/{number}"
    response = requests.get(URL)

    if response.status_code == 200:
        pokemon_data = response.json()
        print(pokemon_data)
    else:
        print(f"Connection Failed... {response.status_code}")

def pokemon_image(number):
    URL = f"{POKE_IMAGE_URL}/{number}.png"
    return URL

# pokemon_api_display(num)
# pokemon_image(num)