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
""" pokemon = {
    "name": "Bulbasaur",
    "type": "grass",
    "weight": 69
}
print(pokemon["type"])
for key, value in pokemon.items():
    print(key, "→", value)
 """
""" types = [t["type"]["name"] for t in data["types"]]
"""
{
  "author": "Paul Sawers",
  "entities": [
    {
      "description": "American social media and technology company",
      "full_name": "Meta Platforms",
      "image": "https://upload.wikimedia.org/wikipedia/commons/7/7c/Meta_Platforms_Headquarters_Menlo_Park_California.jpg",
      "name": "Facebook",
      "type": "ORG"
    },
    {
      "description": "online platform for rental accommodations",
      "full_name": "Airbnb",
      "image": "https://upload.wikimedia.org/wikipedia/commons/2/25/888_Brannan%2C_San_Francisco%2C_2016.jpg",
      "name": "Airbnb",
      "type": "ORG"
    },
    {
      "description": "CRM company that builds customer support and sales software which aims for quick implementation and adaptation at scale.",
      "full_name": "Zendesk",
      "image": "https://upload.wikimedia.org/wikipedia/commons/e/e6/New_zendesk_building.jpg",
      "name": "Zendesk",
      "type": "ORG"
    },
    {
      "description": "Dutch telecom company",
      "full_name": "MessageBird",
      "name": "MessageBird",
      "type": "ORG"
    },
    {
      "description": "data visualization software company",
      "full_name": "FusionCharts",
      "name": "FusionCharts",
      "type": "ORG"
    },
    {
      "latitude": 8.45,
      "location_type": "CITY",
      "longitude": 5.1,
      "name": "Idera",
      "type": "LOC"
    },
    {
      "latitude": 29.76328,
      "location_type": "CITY",
      "longitude": -95.36327,
      "name": "Houston",
      "type": "LOC"
    },
    {
      "latitude": 34.83333,
      "location_type": "LANDMARK",
      "longitude": 32.38333,
      "name": "APIs",
      "type": "LOC"
    },
    {
      "latitude": 48.20849,
      "location_type": "CITY",
      "longitude": 16.37208,
      "name": "Vienna",
      "type": "LOC"
    },
    {
      "latitude": 46.32021,
      "location_type": "CITY",
      "longitude": -112.10722,
      "name": "Amazon",
      "type": "LOC"
    },
    {
      "latitude": 34.1276,
      "location_type": "CITY",
      "longitude": -95.41746,
      "name": "Apple",
      "type": "LOC"
    },
    {
      "latitude": 49.01692,
      "location_type": "REGION",
      "longitude": -82.3331,
      "name": "Slack",
      "type": "LOC"
    },
    {
      "latitude": 3.65037,
      "location_type": "LANDMARK",
      "longitude": 25.32787,
      "name": "API",
      "type": "LOC"
    },
    {
      "latitude": 45.35268,
      "location_type": "LANDMARK",
      "longitude": -116.39586,
      "name": "Rapid",
      "type": "LOC"
    },
    {
      "latitude": 52.471,
      "location_type": "POI",
      "longitude": -1.877,
      "name": "BBS",
      "type": "LOC"
    },
    {
      "latitude": -2.88263,
      "location_type": "CITY",
      "longitude": -77.95803,
      "name": "Embarcadero",
      "type": "LOC"
    }
  ],
  "image": "https://venturebeat.com/wp-content/uploads/2021/01/IderaHomepage.png?fit=1206%2C628&strip=all",
  "language": "en",
  "publish_date": "2021-01-18 16:19:10",
  "sentiment": 0.291,
  "text": "Idera, a Houston-based company that develops a range of database tools, alongside application development and test management tools, has acquired Apilayer, an Austrian startup that offers cloud-based application programming interfaces (APIs). Terms of the deal were not disclosed. Apilayer, which was founded out of Vienna in 2015, provides myriad APIs that serve access to real-time data, such as IP address geolocation, currency conversation, language detection, phone number validation, weather data and forecasts, flight tracking, and stock markets. The company claims a number of high-profile clients, including Amazon, Apple, Slack, Uber, Facebook, Airbnb, and Zendesk. APIs have emerged as indispensable tools for companies looking to build scalable, reliable applications, driven in large part by the rise of cloud computing and a shift to a microservices-based architecture from tightly woven, monolithic apps. As more companies transition to the cloud to boost their digital operations, demand for APIs will continue to grow, evidenced in part by a slew of activity in the space. API development platform Postman raised $150 million at a $2 billion valuation, API marketplace RapidAPI secured $25 million, and MessageBird raised $200 million at a $3 billion valuation before acquiring Pusher to add more real-time communication APIs to its platform. Founded in 2000 as BBS Technologies, Idera targets enterprises with myriad products and services designed to enhance their SQL databases, spanning design, monitoring, and protection. The company, which is co-owned by a trio of private equity firms, has built much of its product suite through acquisitions, having snapped up more than a dozen companies from across the database, DevOps, and testing sphere in the past seven years. Idera said Aliplayer will join its developer tools business alongside other acquisitions, such as Embarcadero and FusionCharts.",
  "title": "Idera acquires API developer Apilayer",
  "url": "https://venturebeat.com/2021/01/18/idera-acquires-api-developer-apilayer/"
}
""""""
import requests

def getWorld_News(news):
    response = requests.get ("https://venturebeat.com/2021/01/18/idera-acquires-api-developer-apilayer/{news.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None

    data = response.json()
    return {
        "latitude": data["name"],
        "location_type": data["height"],
        "longitude": data["weight"],
        "name": data["name"],
        "type": data ["type"]
    }
"entities" == getWorld_News("Embarcadero")
print(getWorld_News)

for key, value in "entities".items():
    print(f"{key.title()}: {value}")

data = getWorld_News()
name = input("Enter the name of where of where the news article came from:")
type = input("Enter the type of the news article:")
for name in data:
    if name["name"] in data:
        