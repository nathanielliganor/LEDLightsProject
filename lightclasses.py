import requests
import time
from datetime import datetime

class LEDLights():

    def __init__(self, url):
        self.url = url

    # We can use a common function to
    # send values.
    def send_signals(self, signal_values):
        try:
            response = requests.post(self.url, json={"values": signal_values})
        except:
            raise Exception('Error sending signals',
                            response.status_code, response.text)

    """ Rescale a range of numbers into another, new
    range, while occupying the entire new range.
    @see: https://stackoverflow.com/questions/19057341/translate-numbers-from-a-range-to-another-range
    """
    def rescale(val, in_min, in_max, out_min, out_max):
        return out_min + (val - in_min) * ((out_max - out_min) / (in_max - in_min))

    """ Generate a 300-light blank sequence
    consisting of unlit "0" values.
    """
    def getBlankSequence(self):
        values_default = ''

        for led_i in list(range(0, 300)):
            leading_comma = ',' if led_i != 0 else ''
            values_default = values_default + leading_comma + '0,0,0,0'

        return values_default

    """ Get the current time in a given area.
    """
    def set_time(area, location, region=""):
        url = f"http://worldtimeapi.org/api/timezone/{area}/{location}/{region}"
        try:
            response = requests.get(url)
            data = response.json()
            return data["datetime"]
        except response.exceptions.RequestException as e:
            print("Error:", e)
            return None

class StaticLights(LEDLights):

    """ Requirement 1: alternate entire strip
        from green, red, white, and blue.
    """
    def color_sequence(self, sleep = 0.5):
        colors = ['0, 0, 255, 0',
                '255, 0, 0, 0',
                '0, 0, 0, 255',
                '0, 225, 0, 0']

        for i in range(10):

            for color in colors:
                signal_values = ""

                for j in range(300):
                    signal_values += (', ' if j != 0 else '') + color

                self.send_signals(signal_values)
                time.sleep(sleep)

    """ Requirement 2: make every other
    light maize and blue.
    """
    def get_umich_lights(self):
        signal_values = ""

        for i in range(300):
            if i % 2 == 0:
                signal_values += "255, 255, 0, 0, "
            else:
                signal_values += "0, 0, 255, 0, "

        signal_values = signal_values[:-2]
        self.send_signals(signal_values)

    """Requirement 3: alternating maize and
    blue lights.
    """
    def alternate_lights(self):
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
            self.send_signals(signal_values)

    # Function to generate signals for displaying the American flag
    def generate_flag_signals(self):
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
        self.send_signals(signal_values)

    def hour_tracker(self, sequence, current_time, sleep):
        """The function takes the current time and the sleep time
        and sends signals to the CATS device to display the time.

        Parameters:
        -----------
        current_time (datetime): The current time.
        sleep (float): The time to sleep between each signal.

        Returns:
        --------
        None
        """
        colors = ["0, 0, 255, 0", "255, 0, 0, 0"]
        self.send_signals(sequence)
        for i in range(0, current_time.minute):
            for color in colors:
                signal_values = ""
                for j in range(0, current_time.hour):
                    signal_values += (", " if j != 0 else "") + color
                self.send_signals(signal_values)
                time.sleep(sleep)

class DynamicLights(LEDLights):

    """ Change colors, locations, alphas, and speed
    based on decibel samples using Audacity.
    """
    @staticmethod
    def danceToBeats(sequence, postCallback, numloops=1):
        import csv
        beats = []
        with open('dance_to_beats.csv', newline='') as csvfile:
            file = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in file:
                beats.append(-1 * int(float(row[0])))

        # Rescale numbers to range(0, 300)
        # https://stackoverflow.com/questions/19057341/translate-numbers-from-a-range-to-another-range
        beats_scaled = []
        for beat in beats:
            beats_scaled.append(int((beat - min(beats)) * (300 / (max(beats) - min(beats)))))

        # Todo: seems to loop endlessly, check reused "loops" variable in range().
        # number of playbacks
        loops = range(0, numloops)
        for loop in loops:

            j = 0
            for beat in beats_scaled:
                # Color is proportional to the beat.
                rgb = int(beat)
                # White is proportional to duration.
                w = -1 * j

                values_before = sequence[:beat * 4]
                values_replace = str(rgb) + ',' + str(rgb) + ',' + str(rgb) + ',' + str(w)
                values_after = sequence[(beat) * 4 + 30:]
                values = values_before + values_replace + values_after

                postCallback(values)

                # Duration is proportional to the beat.
                interval = float(beat / 300) / len(beats)
                time.sleep(interval)

                j = j + 1

    """This function takes a blank sequence of unlit lights
    and creates a leader-chaser sequence where the chaser
    can try to close the gap with the leader.
    """
    @staticmethod
    def chase(sequence, postCallback, leader_rgba='255,255,255,100',
            chaser_rgba='255,255,255,100', gap_size=3,
            gap_change=1, speed=0.00001, persist=False):
        print(sequence)
        print(postCallback)
        print(leader_rgba)
        print(chaser_rgba)
        # Standardardize rgba formats consistency.
        leader_rgba = leader_rgba.replace(' ', '')
        chaser_rgba = chaser_rgba.replace(' ', '')

        # The chaser light's gap and [de]accerlation can
        # be adjusted on a per-light, per-loop basis.
        # Note: an arg of '1' indicates an 1-light gap,
        # or 4 values (r,b,g,a), e.g. 4^3 = (4 vals)^(three lights).
        gap_size = 4 ** gap_size
        # Note: an arg of '1' indicates a 1 light gap
        # by one light per loop.
        gap_change = 8 * gap_change

        # Leader light is placed ahead of
        # chaser by the gap_size.
        i_leader_start = gap_size
        i_leader_end = gap_size + 7
        i_chaser_start = 0
        i_chaser_end = 7

        for i in list(range(0, 300)):
            # Chaser always takes the original sequence
            # and creates a new set of values.
            values_before = sequence[:i_chaser_start]
            values_replace = chaser_rgba
            values_after = sequence[i_chaser_end:]

            # Persist a "trail" of lights.
            #
            # Extra fluff. We can delete if it becomes distracting.
            # If persist is true, then lights do not turn off
            # behind the leader and chaser.
            #
            # TO REMOVE THIS: keep the body of the "else" function, and
            # 1. Kill the remaining conditional and fix indent.
            # 2. Kill the if/then/else postCallback() line.
            # 3. Kill the function argument.
            if persist:
                # Replace "values" with "sequence" to persist lights.
                sequence = values_before + values_replace + values_after
                values_before = sequence[:i_leader_start]
                values_replace = leader_rgba
                values_after = sequence[i_leader_end:]
                sequence = values_before + values_replace + values_after
            else:
                values = values_before + values_replace + values_after
                values_before = values[:i_leader_start]
                values_replace = leader_rgba
                values_after = values[i_leader_end:]
                values = values_before + values_replace + values_after

            # Using a callback to make swaps easy.
            if persist:
                postCallback(sequence)
            else:
                postCallback(values)

            # Leader runs along the strip at a constant
            # rate until it reaches the end, where it loops
            # back around to the beginning of the strip.
            if len(list(range(0, 300)) * 4) >= i_leader_end + 8:
                i_leader_start = i_leader_start + 8
                i_leader_end = i_leader_end + 8
            else:
                i_leader_start = gap_size
                i_leader_end = gap_size + 7

            # Chaser will run along the strip, opening or closing the gap
            # with the leader, and looping back around when it reaches
            # the end of the strip.
            if len(list(range(0, 300)) * 8) >= i_chaser_end + 8 + gap_change:
                i_chaser_start = i_chaser_start + 8 + gap_change
                i_chaser_end = i_chaser_end + 8 + gap_change
            else:
                i_chaser_start = 0
                i_chaser_end = 7

            # Speed is limited by processing
            # and internet bandwidth.
            time.sleep(speed)