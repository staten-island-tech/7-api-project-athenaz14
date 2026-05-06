import requests
def getholiday(holi):
    response = requests.get(f"https://holidayapi.com/v1/holidays?pretty&key=3fea9852-6653-49c3-94f0-ed12cddbac0f&country=US&year=2025")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    
    print(data["name"])

    return []
""" 
            "name": data["name"],
            "date": data["date"],
            "observed": data["observed"],
            "public": data["public"],
            "country": data["country"] """
