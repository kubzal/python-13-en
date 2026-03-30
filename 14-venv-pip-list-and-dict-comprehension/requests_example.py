import requests

results = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.2298&longitude=21.0118&daily=temperature_2m_max&forecast_days=1")

results_dict = results.json()
temperature = float(results_dict["daily"]["temperature_2m_max"][0])

print(f"maximum temperature: {temperature}°C")