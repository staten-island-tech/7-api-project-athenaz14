import requests

def getMatch(chess):
    response = requests.get(f"https://api.chess.com/pub/player/erik/matches{chess.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return { 
        "name" : data["name"],
        "played_as_white" : data["played_as_white"],
        "played_as_black" : data["played_as_black"]
    }
player = getMatch("1st TOC. Bishop Div/R3:TeamUSA vs Netherlands")
print(player)

