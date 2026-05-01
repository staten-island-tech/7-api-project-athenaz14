""" import requests

def getPoke(poke):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }
pokemon = getPoke("Bulbasaur")
print(pokemon)
requests.get("https://pokeapi.co/api/v2/pokemon/bulbasaur")
data = response.json()

 """
pokemon = {
    "name": "Bulbasaur",
    "type": "grass",
    "weight": 69
}
print(pokemon["type"])
for key, value in pokemon.items():
    print(key, "→", value)

""" types = [t["type"]["name"] for t in data["types"]]
 """

    