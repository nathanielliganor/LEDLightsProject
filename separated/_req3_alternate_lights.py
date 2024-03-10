import time
from _send_signals import send_signals

"""Requirement 3: alternating maize and
blue lights.
"""
def alternate_lights():
    # signal_values = ""
    color1 = "255, 255, 0, 0"
    color2 = "0, 0, 255, 0"

    for i in range(10):
        signal_values = ""
        # Every other loop swap maize and blue.
        if i % 2 == 0:
            for j in range(300):
                signal_values += color1 + ", " + color2 + ", "
        else:
            for j in range(300):
                signal_values += color2 + ", " + color1 + ", "

        time.sleep(0.1)
        signal_values = signal_values[:-2]
        send_signals(signal_values)

# alternate_lights()
