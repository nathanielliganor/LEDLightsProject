import requests
from _send_signals import send_signals


# Function to generate signals for displaying the American flag
def generate_flag_signals():
    signal_values = ""
    color_mapping = {
        "1": "255, 0, 0, 0, ",  # Red color
        "2": "0, 0, 255, 0, ",  # Blue color
        "3": "255, 255, 255, 0, "  # White color
    }

    for row in range(10):
        for col in range(30):
            if row % 2 == 0:  # Even rows (0-based indexing)
                if row < 5:  # First 5 rows
                    if col < 12:  # First 40% of columns
                        if col % 2 == 0:
                            signal_values += color_mapping["2"]  # Signal for blue color
                        else:
                            signal_values += color_mapping["3"]
                    else:
                        signal_values += color_mapping["1"]  # Signal for white color
                else:  # After the first 5 rows
                    signal_values += color_mapping["1"]  # Signal for red color
            else:
                if row < 5:
                    if col > 17:
                        if col % 2 == 0:
                            signal_values += color_mapping["3"]
                        else:
                            signal_values += color_mapping["2"]
                    else:
                        signal_values += color_mapping["3"]
                else:
                    signal_values += color_mapping["3"]

    signal_values = signal_values[:-2]  # Removing the extra comma and space at the end
    return signal_values


# Main function to generate signals and send them
def main():
    signal_values = generate_flag_signals()
    send_signals(signal_values)


if __name__ == "__main__":
    main()
