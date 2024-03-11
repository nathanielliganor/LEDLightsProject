import requests


# Request url.
CATS_URL = "https://si568.umsi.run/change?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoic2hhaGF5dUB1bWljaC5lZHUifQ.lOZzE4nwWFj-sNa-etncEQXAJV9rbCV7ElBnGx2skKk&device=CATS"


# We can use a common function to
# send values.
def send_signals(signal_values):
    try:
        response = requests.post(CATS_URL, json={"values": signal_values})
    except:
        raise Exception('Error sending signals',
                        response.status_code, response.text)
