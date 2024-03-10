import time
import requests


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


# Description:
# This function takes a blank sequence of unlit lights
# and creates a leader-chaser sequence where the chaser
# can try to close the gap with the leader.
#
# Arguments:
# sequence is a plain csv string of four integers separated by commas.
# callback: function that posts the request.
# leader_rbga, chaser_rbga: 4-value comma separated RGBA tuples
# gap_size: initial number of leds separting the leader from the chaser.
# gap_change: [de]acceleration of the chaser per loop in milliseconds.
#
# Returns:
# null
def doChase(sequence, postCallback, leader_rgba = '255,255,255,100',
            chaser_rgba = '255,255,255,100', gap_size = 3,
            gap_change = 1, speed = 0.00001, persist = False):

    # Standardardize rgba formats consistency.
    leader_rgba = leader_rgba.replace(' ', '')
    chaser_rgba = chaser_rgba.replace(' ', '')

    # The chaser light's gap and [de]accerlation can
    # be adjusted on a per-light, per-loop basis.
    # Note: an arg of '1' indicates an 1-light gap,
    # or 4 values (r,b,g,a), e.g. 4^3 = (4 vals)^(three lights).
    gap_size = 4**gap_size
    # Note: an arg of '1' indicates a 1 light gap
    # by one light per loop.
    gap_change = 8 * gap_change # NOTE: changing this to 4 * gap_change is really cool.

    # Leader light sits at wherever the chaser
    # is plus the current gap_size.
    i_leader_start = gap_size
    i_leader_end = gap_size + 7 # One-light gap (4 integers + 3 commas)
    i_chaser_start = 0
    i_chaser_end = 7 # Target first light (4 integers + 3 commas)

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
        if persist == True:
            # Note: replace each instance of "values" (see else)
            # with "sequence" to persist lights.
            sequence = values_before + values_replace + values_after
            # Leader always takes the new set of values
            # from the chaser and further modifies it. This is
            # how lights are turned off after it's "turn"
            # in the chase sequence.
            values_before = sequence[:i_leader_start]
            values_replace = leader_rgba
            values_after = sequence[i_leader_end:]
            sequence = values_before + values_replace + values_after
        else:
            values = values_before + values_replace + values_after
            # Leader always takes the new set of values
            # from the chaser and further modifies it. This is
            # how lights are turned off after it's "turn"
            # in the chase sequence.
            values_before = values[:i_leader_start]
            values_replace = leader_rgba
            values_after = values[i_leader_end:]
            values = values_before + values_replace + values_after

        # Using a callback to make swaps easy.
        if persist == True:
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


# Some settings.
sequence = getBlankSequence()
callback = send_signals
leader_rbga = '255,255,255,100'  #optional
sequence_rbga = '255,100,255,100'  #optional
gap_size = 3  #optional
gap_change = 1  #optional
speed = 0.00001  #optional
persist = False #optional (and perhaps we don't do this?)


# Execute the sequence.
doChase(sequence, callback, leader_rbga, sequence_rbga, gap_size, gap_change, speed, persist)