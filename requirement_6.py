import time
import requests
from datetime import datetime


cats_url = "https://si568.umsi.run/change?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoic2hhaGF5dUB1bWljaC5lZHUifQ.lOZzE4nwWFj-sNa-etncEQXAJV9rbCV7ElBnGx2skKk&device=CATS"

def send_signals(signal_values):
    # print(f"Signal Values: {signal_values}")
    response = requests.post(cats_url, json={"values": signal_values})
    # if response.ok:
    #     print("Request was successful!")
    #     print(response.json())
    # else:
    #     print("Request failed!")
    #     print("Status code:", response.status_code)
    #     print("Response text:", response.text)

def set_time(area, location, region=""):
    url = f"http://worldtimeapi.org/api/timezone/{area}/{location}/{region}"
    response = requests.get(url)
    data = response.json()
    return data["datetime"]

# def clock_lights():

def hour_tracker(current_time):
    colors = ["255, 165, 0, 0", "0, 0, 255, 0"]
    if current_time.minute != 0 and current_time.second != 0:
        signal_values = ""
        for color in colors:
            signal_values = ""
            for i in range(10):
                for j in range(0, current_time.hour):
                    signal_values += (", " if j != 0 else "") + color
                send_signals(signal_values)
                time.sleep(0.1)


        # signal_values = signal_values[:-2]
        # return signal_values

USA_time = set_time("America", "Detroit")
dt = datetime.fromisoformat(USA_time)

start_of_hour = dt.replace(minute=0, second=0, microsecond=0)
print("Converted datetime:", dt)
# print("Start of hour:", start_of_hour)

hour_tracker(dt)

