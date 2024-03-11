from _send_signals import send_signals

""" Requirement 2: make every other
light maize and blue.
"""


def get_umich_lights():
    signal_values = ""

    for i in range(300):
        if i % 2 == 0:
            signal_values += "255, 255, 0, 0, "
        else:
            signal_values += "0, 0, 255, 0, "

    signal_values = signal_values[:-2]
    send_signals(signal_values)

# get_umich_lights()
