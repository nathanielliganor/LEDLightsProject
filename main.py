from datetime import datetime
from lightclasses import LEDLights
from lightclasses import StaticLights
from lightclasses import DynamicLights

def main():
    # Request url.
    CATS_URL = "http://si568.umsi.run/change?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoic2hhaGF5dUB1bWljaC5lZHUifQ.lOZzE4nwWFj-sNa-etncEQXAJV9rbCV7ElBnGx2skKk&device=CATS"

    # Create an instance of LEDLights with CATS_URL
    lights = LEDLights(CATS_URL)

    # Color Sequence
    signal_values = StaticLights.color_sequence()

    # UMich Lights
    # signal_values = StaticLights.get_umich_lights()

    # Alternate Lights
    # signal_values = StaticLights.alternate_lights()

    # Dance to Beats
    # signal_values = DynamicLights.danceToBeats(LEDLights.getBlankSequence(), lights.send_signals, 10)

    # Chase
    # signal_values = DynamicLights.chase(
    #     LEDLights.getBlankSequence(),
    #     lights.send_signals,
    #     '255,255,255,100',
    #     '255,255,255,100',
    #     3, 1, 0.00001, False)

    # Generate Flag Signals
    # signal_values = StaticLights.generate_flag_signals()

    # Hour Tracker
    # USA_time = LEDLights.set_time("America", "Detroit")
    # dt = datetime.fromisoformat(USA_time)

    # start_of_hour = dt.replace(minute=0, second=0, microsecond=0)
    # print("Converted datetime:", dt)

    # signal_values = StaticLights.hour_tracker(dt)
    lights.send_signals(signal_values)