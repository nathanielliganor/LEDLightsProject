from datetime import datetime
from os import stat_result
from lightclasses import LEDLights
from lightclasses import StaticLights
from lightclasses import DynamicLights

def main():
    # Request url.
    CATS_URL = "https://si568.umsi.run/change?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoic2hhaGF5dUB1bWljaC5lZHUifQ.lOZzE4nwWFj-sNa-etncEQXAJV9rbCV7ElBnGx2skKk&device=CATS"

    # Create an instance of LEDLights with CATS_URL for Static Methods
    lights = StaticLights(CATS_URL)

    # Static Methods
    lights.color_sequence()
    #lights.get_umich_lights()
    #lights.alternate_lights()
    #lights.generate_flag_signals()

    #detroit_time = LEDLights.set_time("America", "Detroit")
    #dt = datetime.fromisoformat(detroit_time)
    #lights.hour_tracker(LEDLights.getBlankSequence(),dt, sleep=0.1)

    # Create an instance of LEDLights with CATS_URL for Static Methods
    #lights = DynamicLights(CATS_URL)

    # Dyanmic Methods
    #lights.danceToBeats(
    #    lights.getBlankSequence(),
    #    lights.send_signals,
    #    10
    #)

    #lights.chase(lights.getBlankSequence(), lights.send_signals)

if __name__=="__main__":
    main()