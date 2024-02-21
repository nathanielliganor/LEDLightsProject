import requests


def change_color(r, g, b, w, brightness):

    url = "https://si568.umsi.run/change?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWt1dHN1cGlAdW1pY2guZWR1In0.M2ep3tjhGXOB0SlzZgcV3eSIsuHH4eh9VosLtqv4LiA&device=CATS"

    # Floor division is used just to ensure int values.
    values = {
        'values': f"{r * brightness // 255}, {g * brightness // 255}, {b * brightness // 255}, {w * brightness // 255}"
    }

    response = requests.post(url, json=values)

    if response.json():
        return response.json()
    else:
        return "Error"


def shutoff():
    url = "https://si568.umsi.run/off?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWt1dHN1cGlAdW1pY2guZWR1In0.M2ep3tjhGXOB0SlzZgcV3eSIsuHH4eh9VosLtqv4LiA&device=CATS"
    requests.post(url)
    return "Shutoff"


change_color(150, 150, 150, 100, 255)