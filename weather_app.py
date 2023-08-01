import requests

API_KEY = "b6907d289e10d714a6e88b30761fae22"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"

def get_weather_data(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

def get_weather_by_date(data, date):
    for item in data['list']:
        if item['dt_txt'] == date:
            return item['main']['temp']
    return None

def get_wind_speed_by_date(data, date):
    for item in data['list']:
        if item['dt_txt'] == date:
            return item['wind']['speed']
    return None

def get_pressure_by_date(data, date):
    for item in data['list']:
        if item['dt_txt'] == date:
            return item['main']['pressure']
    return None

if __name__ == "__main__":
    city = "London,us"
    data = get_weather_data(city)
    options = {
        1: "Get weather",
        2: "Get Wind Speed",
        3: "Get Pressure",
        0: "Exit"
    }

    while True:
        print("\nOptions:")
        for key, value in options.items():
            print(f"{key}. {value}")

        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Terminating the program.")
            break

        date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")

        if choice == 1:
            weather = get_weather_by_date(data, date)
            if weather is not None:
                print(f"Temperature on {date}: {weather} °C")
            else:
                print("Data not found for the specified date.")
        elif choice == 2:
            wind_speed = get_wind_speed_by_date(data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Data not found.")
        elif choice == 3:
            pressure = get_pressure_by_date(data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Data not found.")
        else:
            print("Invalid choice choose a valid option.")
