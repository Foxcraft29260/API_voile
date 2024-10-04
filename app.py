import requests

from variables import *

def get_weather(api_key, city, days: int = 1): 
    # max days > 5
    url = f"https://api.weatherapi.com/v1/marine.json?key={api_key}&q={city}&days={days}"
    response = requests.get(url)
    data = response.json()
    final_data: list = []
    
    if response.status_code == 200:
        # Boucle pour regarder les différents jours
        for day in range(days):
            final_data.append({"date": data["forecast"]["forecastday"][day]["date"], "values": []})
            # Boucle pour regarder les 24h de la journée
            for time in data["forecast"]["forecastday"][day]["hour"]:
                # vérification de la plage horaire
                if int(time["time"][11:13]) >= 8 and int(time["time"][11:13]) <= 20:
                    #Vérification de la vitesse du vent et sa direction 
                    if time["wind_kph"]//1.852 >= GOOD_SPEED and time["wind_dir"] in GOOD_DIR:
                        final_data[day]["values"].append({ "time": time["time"][11:],
                                           "wind_mls": time["wind_kph"]//1.852, 
                                           "wind_dir": time["wind_dir"]
                                           })
        
        # location = data["location"]["name"]
        # temperature = data["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
        # condition = data["forecast"]["forecastday"][0]["day"]["condition"]["text"]
        # vent = data["forecast"]["forecastday"][0]["day"]["maxwind_kph"]
        # dirVent = data["forecast"]["forecastday"][0]["hour"][8]["wind_dir"]
        # print(f"Météo à {location}: {temperature}°C, {condition}, Vitesse du vent: {vent/1.852} noeuds, et le vent vient de la direction {dirVent}")
        return final_data
    else:
        # print("erreur  lors de la réccupération des données", response.status_code)
        return "erreur  lors de la récupération des données"
    

if __name__ == "__main__":
    api_key = "77eb92f97e104bf6b9773753242709"
    city = "Landerneau"
    print(get_weather(api_key, city, 5))
    