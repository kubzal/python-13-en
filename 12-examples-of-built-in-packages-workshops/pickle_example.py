import pickle

data = {
    "name": "John",
    "age": 30,
    "hobbies": ["programming", "basketball", "chess"]
}

print("Orginal data:", data)

with open("my_data.pkl", "wb") as f:
    pickle.dump(data, f)

with open("my_data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

print("\nLoaded data:", loaded_data)

