import requests

def get_weather(api_key, city):
    url = f"https://api.weatherapi.com/v1/marine.json?key={api_key}&q={city}&days=3"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        location = data["location"]["name"]
        temperature = data["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
        condition = data["forecast"]["forecastday"][0]["day"]["condition"]["text"]
        vent = data["forecast"]["forecastday"][0]["day"]["maxwind_kph"]
        dirVent = data["forecast"]["forecastday"][0]["hour"][8]["wind_dir"]
        print(f"Météo à {location}: {temperature}°C, {condition}, Vitesse du vent: {vent/1.852} noeuds, et le vent vient de la direction {dirVent}")
        return {"location": location, "temperature": temperature, "condition": condition, "vent": vent}
    else:
        print("erreur  lors de la réccupération des données", response.status_code)
    

if __name__ == "__main__":
    api_key = "77eb92f97e104bf6b9773753242709"
    city = "Paris"
    get_weather(api_key, city)
    