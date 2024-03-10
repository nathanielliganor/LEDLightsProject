'''
Parent Class (LEDLights): To send signal

Subclasses:
1. StaticLights() - methods for requirements that do not require the lights to move
2. DynamicLights() - methods for requirements that require the lights to move

I left off on fixing main() for last three StaticLights methods. Started implementing Dynamic methods
'''

import requests
import time

class LEDLights():

    def __init__(self, url):
        self.url = url

    def send_signals(self, signal_values):
        print(f"Signal Values: {signal_values}")
        response = requests.post(self.url, json={"values": signal_values})
        if response.ok:
            print("Request was successful!")
            print(response.json())
        else:
            print("Request failed!")
            print("Status code:", response.status_code)
            print("Response text:", response.text)


class StaticLights(LEDLights):

    @staticmethod
    def AmericanFlag():
        signal_values = []
        color_mapping = {
            "1": (255, 0, 0, 0),   # Map value 1 to red color
            "2": (0, 0, 255, 0),   # Map value 2 to blue color
            "3": (0, 0, 0, 255)    # Map value 3 to white color
        }

        for row in range(10):
            for col in range(30):
                if row % 2 == 0:  # Even rows (0-based indexing)
                    if col < 13:  # Top-left rectangle (blue)
                        signal_values.append(color_mapping["2"])  # Signal for blue color
                    elif col < 25:  # Red stripes
                        signal_values.append(color_mapping["1"])  # Signal for red color
                    else:  # White stripes
                        signal_values.append(color_mapping["3"])  # Signal for white color
                else:  # Odd rows
                    if col < 13:  # Top-left rectangle (blue)
                        signal_values.append(color_mapping["1"])  # Signal for red color
                    elif col < 25:  # Red stripes
                        signal_values.append(color_mapping["2"])  # Signal for blue color
                    else:  # White stripes
                        signal_values.append(color_mapping["3"])  # Signal for white color

        return signal_values

    @staticmethod
    def ColorSequence(colors):
        signal_values = ""
        color_sequence = colors
        for color in color_sequence:
            for i in range(300):
                signal_values += color + ", "
        signal_values = signal_values[:-2]
        return signal_values

    @staticmethod
    def UmichLights():
        signal_values = ""
        for i in range(300):
            if i % 2 == 0:
                signal_values += "255, 255, 0, 0, "
            else:
                signal_values += "0, 0, 255, 0, "
        signal_values = signal_values[:-2]
        return signal_values

    @staticmethod
    def getBlankSequence():
        values_default = ''

        for led_i in list(range(0, 300)):
            leading_comma = ',' if led_i != 0 else ''
            values_default = values_default + leading_comma + '0,0,0,0'

        return values_default

class DynamicLights(LEDLights):

    def alternate_lights():
        signal_values = ""
        color1 = "255, 255, 0, 0"
        color2 = "0, 0, 255, 0"
        for i in range(300):
            signal_values += color1 + ", " + color2 + ", "
        signal_values = signal_values[:-2]
        return signal_values

def main():
    url = "https://si568.umsi.run/change?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoic2hhaGF5dUB1bWljaC5lZHUifQ.lOZzE4nwWFj-sNa-etncEQXAJV9rbCV7ElBnGx2skKk&device=CATS"

    # Create an instance of LEDLights with URL
    lights = LEDLights(url)

    # Define the colors required for color_sequence.
    requirement_1_colors = [
        "0, 0, 255, 0",  # Blue
        "255, 0, 0, 0",  # Red
        "0, 0, 0, 255",  # White
        "0, 0, 255, 0",  # Green
    ]

    # American Flag
    signal_values = StaticLights.AmericanFlag()
    lights.send_signals(signal_values)

    # Color Sequence
    color_sequence_values = StaticLights.ColorSequence()

if __name__ == "__main__":
    main()