import requests

# Function to send signals to the transmitter
def send_signals(signal_values):
    requests.post("https://si568.umsi.run/change?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoic2hhaGF5dUB1bWljaC5lZHUifQ.lOZzE4nwWFj-sNa-etncEQXAJV9rbCV7ElBnGx2skKk&device=CATS", json={'values': signal_values})

# Function to generate signals for displaying the American flag
def generate_flag_signals():
    signal_values = []
    color_mapping = {
        "1": (255, 0, 0, 0),   # Map value 1 to red color
        "2": (0, 0, 255, 0),   # Map value 2 to blue color
        "3": (0, 0, 0, 255)    # Map value 3 to white color
    }
    
    for row in range(10):
        for col in range(30):
            if row < 5 and col < 13:  # Top-left rectangle (blue)
                signal_values.append(color_mapping["1"])  # Signal for blue color
            elif col < 25:  # Red stripes
                signal_values.append(color_mapping["2"])  # Signal for red color
            else:  # White stripes
                signal_values.append(color_mapping["3"])  # Signal for white color
                
    return signal_values

# Main function to generate signals and send them
def main():
    signal_values = generate_flag_signals()
    send_signals(signal_values)

if __name__ == "__main__":
    main()
