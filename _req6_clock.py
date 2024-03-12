import time
import requests
from datetime import datetime
from _send_signals import send_signals
from _get_blank_sequence import getBlankSequence

cats_url = "https://si568.umsi.run/change?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoic2hhaGF5dUB1bWljaC5lZHUifQ.lOZzE4nwWFj-sNa-etncEQXAJV9rbCV7ElBnGx2skKk&device=CATS"

def set_time(area, location, region=""):
    url = f"http://worldtimeapi.org/api/timezone/{area}/{location}/{region}"
    response = requests.get(url)
    data = response.json()
    return data["datetime"]

def hour_tracker(sequence, current_time, sleep):
    """The function takes the current time and the sleep time
    and sends signals to the CATS device to display the time.

    Parameters:
    -----------
    current_time (datetime): The current time.
    sleep (float): The time to sleep between each signal.

    Returns:
    --------
    None
    """
    colors = ["0, 0, 255, 0", "255, 0, 0, 0"]
    send_signals(sequence)
    for i in range(0, current_time.minute):
        for color in colors:
            signal_values = ""
            for j in range(0, current_time.hour):
                signal_values += (", " if j != 0 else "") + color
            send_signals(signal_values)
            time.sleep(sleep)
def main():
    """The entry point of the program."""

    detroit_time = set_time("America", "Detroit")
    dt = datetime.fromisoformat(detroit_time)
    hour_tracker(getBlankSequence(),dt, sleep=0.1)

if __name__ == "__main__":
    main()
