import requests
import time

def fetch_random_users(results_per_page, total_pages):
    print("Results per page:", results_per_page)
    print("Total pages:", total_pages)
    print("-" * 100)

    base_url = "https://randomuser.me/api/"
    for page in range(1, total_pages + 1):
        params = {"page": page, "results": results_per_page}
        response = requests.get(base_url, params = params)

        if response.status_code == 200:
            data = response.json()
            yield data["results"]
        else:
            print(f"Failed to fetch page {page}: {response.status_code}")

total_pages = 5
results_per_page = 3

for users in fetch_random_users(results_per_page, total_pages):
    for user in users:
        title = user["name"]["title"]
        first_name = user["name"]["first"]
        last_name = user["name"]["last"]
        city = user["location"]["city"]
        country = user["location"]["country"]

        print(f"Title: {title}, Name: {first_name} {last_name}, City: {city}, Country: {country}")
        print("-" * 100)
        time.sleep(2)