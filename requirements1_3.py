# Requirements 1-3
import time
import requests

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

# def send_signals(signal_values):
#     try:
#         response = requests.post(cats_url, json={"values": signal_values})
#     except:
#         raise Exception('Error sending signals',
#                         response.status_code, response.text)

def send_signals(signal_values):
    # print(f"Signal Values: {signal_values}")
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
        for i in range(300):
            signal_values += color
    signal_values = signal_values[:-2]
    return signal_values


def color_sequence_2():
    colors = ['0, 0, 255, 0',
              '255, 0, 0, 0',
              '0, 0, 0, 255',
              '10, 225, 0, 0']
    for i in range(10):
        for color in colors:
            signal_values = ""
            for j in range(300):
                signal_values += (', ' if j != 0 else '') + color
            send_signals(signal_values)

            time.sleep(0.5)


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


def main():
    requirement_1_colors = [
        "0, 0, 255, 0",
        "255, 0, 0, 0",
        "0, 0, 0, 255",
        "0, 0, 255, 0",
    ]  # Blue, Red, White, Green

    signal_values = color_sequence(requirement_1_colors)

    # send_signals(signal_values)
    # send_signals(get_umich_lights())
    # send_signals(alternate_lights())
    send_signals(requirement1())

if __name__ == "__main__":
    main()
