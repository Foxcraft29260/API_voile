import requests

def get_weather(api_key, city):
    url = f"https://api.weatherapi.com/v1/marine.json?key={api_key}&q={city}&days=3"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        location = data["location"]["name"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"Météo à {location}: {temperature}°C, {condition}")
    else:
        print("erreur  lors de la réccupération des données", response.status_code)
    

if __name__ == "__main__":
    api_key = "77eb92f97e104bf6b9773753242709"
    city = "Paris"
    get_weather(api_key, city)