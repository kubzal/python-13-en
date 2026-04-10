import sys
import random
import time
from datetime import datetime, timedelta


class Sensor:
    """Class represents temperature sensor"""
    def __init__(self, location):
        self.location = location

    def read_temperature(self):
        """Simulates temperature read"""
        return round(random.uniform(-10, 40), 2)

    def temperature_stream(self):
        while True:
            yield self.read_temperature()

    def temperare_stream_with_location(self):
        while True:
            yield f"[{datetime.now()}] Temperature in the {self.location}: {self.read_temperature()}°C"


# Example of usage
kitchen_sensor = Sensor("Kitchen")
# temp_gen = kitchen_sensor.temperature_stream()

temp_gen = kitchen_sensor.temperare_stream_with_location()

# for _ in range(5):

args = sys.argv
# print(args)
if len(args) > 2:
    secs = int(args[1])
    interval = int(args[2])
elif len(args) == 2:
    secs = int(args[1])
    interval = 1
else:
    secs = input("How long would you like to display the temperature (in seconds)?: ")
    interval = input("What time interval (in seconds) between the temperature reads you like?: ")

end_time = datetime.now() + timedelta(seconds=int(secs))

while datetime.now() < end_time:
    time.sleep(int(interval))
    # print(f"Temperature: {next(temp_gen)} °C")
    print(next(temp_gen))