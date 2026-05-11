import requests
url = "https://api.chess.com/pub/player/124chess"
def getMatch(chess):
    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {

        "avatar" : data["avatar"],
        "player_id" : data["player_id"],
        "@id" : data["@id"],
        "url" : data["https://www.chess.com/member/124chess"],
        "name" : data["name"],
        "title" : data["title"],

    }
user_input = input("Learn more about chess player: 124chess(options are avatar, player_id, @id, url, name, title)")
if user_input == "avatar":
    print(data["avatar"])


