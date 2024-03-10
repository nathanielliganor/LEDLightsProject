import time
import requests
import random
import csv


# Global vars.
cats_url = "https://si568.umsi.run/change?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoic2hhaGF5dUB1bWljaC5lZHUifQ.lOZzE4nwWFj-sNa-etncEQXAJV9rbCV7ElBnGx2skKk&device=CATS"


# We can use a common function to
# send values.
def send_signals(signal_values):
    try:
        response = requests.post(cats_url, json={"values": signal_values})
    except:
        raise Exception('Error sending signals',
                        response.status_code, response.text)


# Generate a 300-light blank sequence
# consisting of unlit "0" values.
def getBlankSequence():
    values_default = ''

    for led_i in list(range(0, 300)):
        leading_comma = ',' if led_i != 0 else ''
        values_default = values_default + leading_comma + '0,0,0,0'

    return values_default


# Rescale a range of numbers into another, new
# range, while occupying the entire new range.
def rescale(val, in_min, in_max, out_min, out_max):
    return out_min + (val - in_min) * ((out_max - out_min) / (in_max - in_min))


# Change colors, locations, alphas, and speed
# based on decibel samples using Audacity.
def danceToBeats(sequence, postCallback, loops = 1):
    import csv
    beats = []
    with open('dance_to_beats.csv', newline='') as csvfile:
        file = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in file:
            beats.append(-1 * int(float(row[0])))

    # Rescale numbers to range(0, 300)
    for beat in range(0, len(beats)):
        beats[beat] = int(rescale(beats[beat], min(beats), max(beats), 0, 299))

    # number of playbacks
    loops = range(0, loops)
    for loop in loops:

        j = 0
        for beat in beats:
            # Color is proportional to the beat.
            r = int(beat)
            g = int(beat)
            b = int(beat)

            # Alpha is proportional to duration.
            a = -1 * j

            values_before = sequence[:beat * 3] # HOW CAN WE REACH THE WHOLE STRIP? https://stackoverflow.com/questions/929103/convert-a-number-range-to-another-range-maintaining-ratio
            values_replace = str(r) +','+str(g)+','+str(b)+','+str(a)
            values_after = sequence[(beat * 3) + 30:] # HOW TO SCALE NUMBERS TO REACH WHOLE STRIP: https://stackoverflow.com/questions/929103/convert-a-number-range-to-another-range-maintaining-ratio
            values = values_before + values_replace + values_after

            postCallback(values)

            # Duration is proportional to the beat.
            interval = float(beat/300)/len(beats)
            time.sleep(interval)

            j = j + 1


sequence = getBlankSequence()

danceToBeats(sequence, send_signals, 10)