
import requests

print("=" * 50)
print("         WEATHER APPLICATION")
print("=" * 50)

while True:
    city = input("\nEnter City Name: ").strip()

    if city == "":
        print("Please enter a city name.")
        continue

    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print("Unable to connect to the weather service.")
            continue

        data = response.json()

        # Check if weather information is available
        if "current_condition" not in data:
            print("City not found! Please enter a valid city.")
            continue

        current = data["current_condition"][0]

        # Get the city name returned by the service
        returned_city = city.title()
        if "nearest_area" in data:
            returned_city = data["nearest_area"][0]["areaName"][0]["value"]

        print("\n" + "=" * 50)
        print("              WEATHER REPORT")
        print("=" * 50)
        print("City         :", returned_city)
        print("Temperature  :", current["temp_C"], "°C")
        print("Feels Like   :", current["FeelsLikeC"], "°C")
        print("Humidity     :", current["humidity"], "%")
        print("Pressure     :", current["pressure"], "mb")
        print("Weather      :", current["weatherDesc"][0]["value"])
        print("Wind Speed   :", current["windspeedKmph"], "km/h")
        print("Visibility   :", current["visibility"], "km")
        print("=" * 50)

    except requests.exceptions.ConnectionError:
        print("\nNo Internet Connection!")

    except requests.exceptions.Timeout:
        print("\nRequest Timed Out!")

    except Exception as e:
        print("\nError:", e)

    again = input("\nDo you want to search another city? (yes/no): ").strip().lower()

    if again != "yes":
        print("\nThank you for using the Weather Application!")
        break
