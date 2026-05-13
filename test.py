import requests
url = "https://api.chess.com/pub/player/124chess"
def getMatch():
    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    return []
data = getMatch()    
""" user_input = input("Learn more about chess player: 124chess(options are avatar, player_id, @id, url, name, title)")
 """
for info in data:
    print(info)


""" 
for info in data:
    if user_input == data["avatar"]:
        print(data["avatar"])
    elif user_input == data["player_id"]:
         print(data["player_id"])
    elif user_input == data["@id"]:
         print(data["@id"])


 """