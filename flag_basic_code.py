import requests
import time

# Function to send signals to the transmitter
def send_signals(signal_values):
    requests.post("https://si568.umsi.run/change?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoic2hhaGF5dUB1bWljaC5lZHUifQ.lOZzE4nwWFj-sNa-etncEQXAJV9rbCV7ElBnGx2skKk&device=CATS", json={'values': signal_values})

# Function to generate signals for displaying the American flag
def generate_flag_signals():
    signal_values = []
    color_mapping = {
        "red_high": (255, 0, 0, 255),   # High brightness red
        "red_low": (255, 0, 0, 128),    # Low brightness red
        "blue_high": (0, 0, 255, 255),  # High brightness blue
        "blue_low": (0, 0, 255, 128),   # Low brightness blue
        "white_high": (255, 255, 255, 255), # High brightness white
        "white_low": (255, 255, 255, 128)  # Low brightness white
    }
    
    for row in range(10):
        brightness = "high" if row % 2 == 0 else "low" # Alternate brightness
        for col in range(30):
            if row % 2 == 0:  # Even rows (0-based indexing)
                if col < 13:  # Top-left rectangle (blue)
                    signal_values.append(color_mapping[f"blue_{brightness}"])  # Signal for blue color
                elif col < 25:  # Red stripes
                    signal_values.append(color_mapping[f"red_{brightness}"])  # Signal for red color
                else:  # White stripes
                    signal_values.append(color_mapping[f"white_{brightness}"])  # Signal for white color
            else:  # Odd rows
                if col < 13:  # Top-left rectangle (blue)
                    signal_values.append(color_mapping[f"red_{brightness}"])  # Signal for red color
                elif col < 25:  # Red stripes
                    signal_values.append(color_mapping[f"blue_{brightness}"])  # Signal for blue color
                else:  # White stripes
                    signal_values.append(color_mapping[f"white_{brightness}"])  # Signal for white color
    
    return signal_values

def animate_flag(signal_values):
    '''Shifts the flag's stripes to create a moving sequence effect'''
    # Number of columns in the flag
    num_columns = 30
    # Split the flag into rows for processing
    rows = [signal_values[i:i+num_columns] for i in range(0, len(signal_values), num_columns)]

    # Apply horizontal shift to each row
    for i in range(len(rows)):
        # Shift the entire row for stripes below the union
        if i >= 5:
            rows[i] = rows[i][-1:] + rows[i][:-1] # Shift right by one position
        else:
            # For the union area, only shift the part of the row after the union
            union = rows[i][:13] # Keep the union static
            stripes = rows[i][13:] # Only shift this part
            shifted_stripes = stripes[-1:] + stripes[:-1] # Shift right
            rows[i] = union + shifted_stripes # Reassemble the row
    
    # Flatten the list back into the original format
    return [color for row in rows for color in row]

# Main function to generate signals and send them
def main():
    original_signal_values = generate_flag_signals()
    signal_values = original_signal_values.copy()
    for i in range(10): # Number of animation cycles
        signal_values = animate_flag(signal_values)
        send_signals(signal_values)
        time.sleep(1) # Delay between updates to create the animation effect

if __name__ == "__main__":
    main()
