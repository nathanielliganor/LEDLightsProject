from _send_signals import send_signals
from _get_blank_sequence import getBlankSequence

from _req1_color_sequence import color_sequence
from _req2_maize_blue import get_umich_lights
from _req3_alternate_lights import alternate_lights
from _req4_any_sequence import danceToBeats
from _req5_chase import chase
# from _req6_clock import hour_tracker
# from _req7_extra_flag import generate_flag_signals


def main():
    # Execute each requirement by commenting out
    # the requirement you'd like to run.
    color_sequence()
    # get_umich_lights()
    # alternate_lights()
    # danceToBeats(getBlankSequence(), send_signals, 10)
    # chase(getBlankSequence(), send_signals,
    #       '255,255,255,100',
    #       '255,100,255,100',
    #       3, 1, 0.0001, False),
    # hour_tracker() # Uncomment out from/import above to active
    # generate_flag_signals()


if __name__ == "__main__":
    main()
