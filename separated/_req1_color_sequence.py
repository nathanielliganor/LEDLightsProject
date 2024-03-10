import time
from _send_signals import send_signals

""" Requirement 1: alternate entire strip
    from green, red, white, and blue. 
"""
def color_sequence(sleep = 0.5):
    colors = ['0, 0, 255, 0',
              '255, 0, 0, 0',
              '0, 0, 0, 255',
              '0, 225, 0, 0']

    for i in range(10):

        for color in colors:
            signal_values = ""

            for j in range(300):
                signal_values += (', ' if j != 0 else '') + color

            send_signals(signal_values)
            time.sleep(sleep)

# color_sequence()