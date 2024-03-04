import time
import requests

# Function to send signals to the transmitter
def send_signals(signal_values):
    requests.post("https://si568.umsi.run/change?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoic2hhaGF5dUB1bWljaC5lZHUifQ.lOZzE4nwWFj-sNa-etncEQXAJV9rbCV7ElBnGx2skKk&device=CATS", json={'values': signal_values})

# Define LED grid layout (10 rows x 30 columns)
led_grid = [
    [1, 2, 3, ..., 30],  # Row 1
    [31, 32, 33, ..., 60],  # Row 2
    ...
    [271, 272, 273, ..., 300]  # Row 10
]

# Function to light up LED at specified row and column
def light_up_led(row, col):
    send_signals({led_grid[row][col]: 1})

# Function to turn off all LEDs
def turn_off_leds():
    signal_values = {led_pin: 0 for row in led_grid for led_pin in row}
    send_signals(signal_values)

try:
    while True:
        # Get current time
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min
        second = current_time.tm_sec
        
        # Display current time on LED grid
        turn_off_leds()
        light_up_led(hour // 3, hour % 3)  # Display hour
        light_up_led(minute // 3 + 4, minute % 3)  # Display minute
        light_up_led(second // 3 + 8, second % 3)  # Display second
        
        # Delay for 1 second
        time.sleep(1)

except KeyboardInterrupt:
    turn_off_leds()
