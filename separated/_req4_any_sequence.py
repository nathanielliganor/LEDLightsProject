import time
from _get_blank_sequence import getBlankSequence
from _send_signals import send_signals

""" Rescale a range of numbers into another, new
range, while occupying the entire new range.
@see: https://stackoverflow.com/questions/19057341/translate-numbers-from-a-range-to-another-range
"""
def rescale(val, in_min, in_max, out_min, out_max):
    return out_min + (val - in_min) * ((out_max - out_min) / (in_max - in_min))


""" Change colors, locations, alphas, and speed
based on decibel samples using Audacity.
"""
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
