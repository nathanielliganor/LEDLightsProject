# Requirements 1-3
import requests
import time

# requests.post("https://si568.umsi.run/test?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoibW1pdGNoanJAdW1pY2guZWR1In0.MiyU3Vu_3jBVAVqfgJZL39ATXGcUB4yeTOE-CKklg-U&device=CATS")

# response = requests.post(
#     "https://si568.umsi.run/change?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoibW1pdGNoanJAdW1pY2guZWR1In0.MiyU3Vu_3jBVAVqfgJZL39ATXGcUB4yeTOE-CKklg-U&device=CATS",
#     json={"values": "255, 0, 255, 1"}
# )

# if response.ok:
#     print("Request was successful!")
#     print(response.json())
# else:
#     print("Request failed!")
#     print("Status code:", response.status_code)
#     print("Response text:", response.text)

# requests.post(
#     "https://si568.umsi.run/off?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoibW1pdGNoanJAdW1pY2guZWR1In0.MiyU3Vu_3jBVAVqfgJZL39ATXGcUB4yeTOE-CKklg-U&device=CATS"
# )


# https://forum.arduino.cc/t/fastled-chase-sequence-with-multiple-colors-3-ws2812-led-strip/629592
# https://firialabs.com/blogs/lab-notes/neopixel-api-part-4-chase-lights-explained
# https://www.sitepoint.com/colors-json-example/

# 1) Make all the lights blue/ then red/ then white/ then green.

cats_url = "https://si568.umsi.run/change?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoic2hhaGF5dUB1bWljaC5lZHUifQ.lOZzE4nwWFj-sNa-etncEQXAJV9rbCV7ElBnGx2skKk&device=CATS"

def send_signals(signal_values):
    print(f"Signal Values: {signal_values}")
    response = requests.post(cats_url, json={"values": signal_values})
    if response.ok:
        print("Request was successful!")
        print(response.json())
    else:
        print("Request failed!")
        print("Status code:", response.status_code)
        print("Response text:", response.text)


def color_sequence(colors):
    signal_values = ""
    color_sequence = colors
    for color in color_sequence:
        # print(f"Color: {color}")
        for i in range(300):
            signal_values += color + ", "
    signal_values = signal_values[:-2]
    # print(f"Signal Values: {signal_values}")
    return signal_values

# 2) Make every other light maize (yellow) and blue. (E.g., the first light is maize,
# second is blue, third is maize, and so on.)

def get_umich_lights():
    signal_values = ""
    for i in range(300):
        if i % 2 == 0:
            signal_values += "255, 255, 0, 0, "
        else:
            signal_values += "0, 0, 255, 0, "
    signal_values = signal_values[:-2]
    return signal_values

# 3) Make the lights alternate back and forth from maize to blue in two different ways. (Choose one of these, or make a more complex example)
# a) Every other light changes. (E.g., first light is maize, the second is blue, then the first light changes to blue, and the second light changes to maize, and so on.)
# b) All lights change together. (E.g., all lights maize, then all lights blue, maize, and so on.)
# c) Can you fade the lights?

def alternate_lights():
    signal_values = ""
    color1 = "255, 255, 0, 0"
    color2 = "0, 0, 255, 0"
    for i in range(300):
        signal_values += color1 + ", " + color2 + ", "
    signal_values = signal_values[:-2]
    return signal_values

def main():
    requirement_1_colors = [
        "0, 0, 255, 0",
        "255, 0, 0, 0",
        "0, 0, 0, 255",
        "0, 0, 255, 0",
    ]  # Blue, Red, White, Green
    signal_values = color_sequence(requirement_1_colors)
    print(f"Final Signal Values: {signal_values}")
    send_signals(signal_values)
    # send_signals(get_umich_lights())
    # send_signals(alternate_lights())

if __name__ == "__main__":
    main()
