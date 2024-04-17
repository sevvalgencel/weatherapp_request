import requests


def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data


def main():
    city = input("Şehri Giriniz : ")
    api_key = "bd5e378503939ddaee76f12ad7a97608"
    weather_data = get_weather(api_key, city)

    if weather_data["cod"] == 200:
        print(f"Hava Durumu Bilgisi - {city}:")
        print(f"Sıcaklık: {weather_data['main']['temp']}°C")
        print(f"Nem: {weather_data['main']['humidity']}%")
    else:
        print(f"{city} için hava durumu bilgisi alınamadı.")


if __name__ == "__main__":
    main()