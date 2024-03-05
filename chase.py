#!/usr/bin/env python
# coding: utf-8

import requests

# Num leds
leds_i = list(range(0, 3))

# ### Colors
colors = {}
colors[0] = {'values': '255, 255, 255, 50, 0, 0, 0, 0, 0, 0, 0, 0'}
colors[1] = {'values': '0, 0, 0, 0, 255, 255, 255, 50, 0, 0, 0, 0'}
colors[2] = {'values': '255, 255, 255, 50, 0, 0, 0, 0, 255, 255, 255, 50'}

# Test loop
import time

for led_i in leds_i:
    values = colors[led_i]
    requests.post("https://si568.umsi.run/change?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoibmtldGNodW1AdW1pY2guZWR1In0.f2lmEnFW3PMgXJP6OoNZLBnyQsXSKES8mUdbNhKXUsA&device=CATS", json=values)
    time.sleep(1)
