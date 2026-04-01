"""
=== Exercise: EUR to PLN Exchange Rate Checker ===

In this exercise, you will write a program that checks the EUR to PLN
exchange rate on a particular day using the NBP (National Bank of Poland) API.

The program will ask the user for a date in the "YYYY-MM-DD" format,
for example "2025-03-15". If no date is provided, the application should
consider the previous working day as the date to check.

The program will then make a request to the NBP API to fetch the exchange rate.

Tasks:
-------
1. Ask the user for a date in "YYYY-MM-DD" format to check the exchange rate.
2. If no date is provided, consider the previous working day as the default date.
3. Make a request to the NBP API to fetch the EUR/PLN exchange rate for the given date.
4. Display the result to the user:
   - If the rate is found, print the mid (average) exchange rate.
   - Compare it to a reference rate of 4.50 PLN and tell the user:
     * "EUR is expensive today!" if the rate is above 4.50
     * "EUR is cheap today!" if the rate is below 4.50
     * "EUR is exactly at the reference rate." if equal to 4.50
   - If no data is available (e.g. weekend/holiday), print "No exchange rate
     data available for this date (possibly a weekend or holiday)."
5. Save the query results to a JSON file. If the date is already present
   in the file, do not make a request to the API — return the result from the file.
"""
import os
import json
import requests
from datetime import datetime, timedelta

CACHE_FILE = "cache.json"
REFERENCE_RATE = 4.50
API_URL = "https://api.nbp.pl/api/exchangerates/rates/a/eur/{date}"

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as file:
            return json.load(file)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w") as file:
        json.dump(cache, file, indent=2)

def get_previous_workday():
    today = datetime.now()
    offset = 1
    if today.weekday() == 0: # Monday -> go back to Friday
        offset = 3
    elif today.weekday() == 6: # Sunday -> go back to Friday
        offset = 2
    previous_day = today - timedelta(days=offset)
    return previous_day.strftime("%Y-%m-%d")

def get_date_from_user():
    date_input = input("Enter a date (YYYY-MM-DD) or press Enter for the previous working day: ").strip()

    if not date_input:
        # than look at the previous working day
        default_date = get_previous_workday()
        print(f"No date provided. Using previous working day: {default_date}")
        return default_date

    try:
        datetime.strptime(date_input, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD")
        return None

    return date_input

def fetch_exchange_rate(exchange_date_):
    url = API_URL.format(date=exchange_date_)

    params = {"format": "json"}
    response = requests.get(url, params=params)
    data = response.json()
    rate = data["rates"][0]["mid"]

    return rate

def display_results(date_, rate_):
    print()
    print(f"EUR/PLN exchange rate on {date_}: {rate_} PLN")

    if rate_ > REFERENCE_RATE:
        print("EUR is expensive today!")
    elif rate_ < REFERENCE_RATE:
        print("EUR is cheap today!")
    else:
        print("EUR is exactly at the reference rate.")

def main():
    # get data from user
    exchange_date = get_date_from_user()

    # check if date exist in cache
    cache = load_cache()
    if exchange_date in cache:
        print(f"(Using cached result for {exchange_date})")
        exchange_rate = cache[exchange_date]
    else:
        # if not, fetch the api
        print(f"Fetching exchange rate for: {exchange_date}...")
        exchange_rate = fetch_exchange_rate(exchange_date)
        cache[exchange_date] = exchange_rate
        save_cache(cache)

    # present data to user
    display_results(exchange_date, exchange_rate)

if __name__ == "__main__":
    main()