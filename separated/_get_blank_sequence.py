""" Generate a 300-light blank sequence
consisting of unlit "0" values.
"""
def getBlankSequence():
    values_default = ''

    for led_i in list(range(0, 300)):
        leading_comma = ',' if led_i != 0 else ''
        values_default = values_default + leading_comma + '0,0,0,0'

    return values_default
