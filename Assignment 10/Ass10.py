#Task 1
import requests

def chuck_norris_joke():
    request = "https://api.chucknorris.io/jokes/random"
    response = requests.get(request).json()
    print(response)

#Task 2
import requests

def get_weather(city, api_key):
    request = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(request).json()

    if response.get("cod") != 200:
        print("City not found!")
        return

    description = response["weather"][0]["description"]
    temp_kelvin = response["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15

    print(f"Weather in {city}: {description}, {temp_celsius:.2f} °C")

#Task 3
from flask import Flask

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def prime_number(number):
    result = {"Number": number, "isPrime": is_prime(number)}
    return (result)

if __name__ == '__main__':
    app.run()

#Task 4
from flask import Flask

app = Flask(__name__)

airport_db = {
    "LFLL": {
        "name": "Lyon Saint-Exupery Airport",
        "city": "Lyon",
        "country": "FR"},
    "KJFK": {
        "name": "John F. Kennedy International Airport",
        "city": "New York",
        "country": "US"}
}

@app.route('/airport/<icao>', methods=['GET'])
def airport_info(icao):
    airport = airport_db.get(icao.upper())
    if airport:
        result = {"icao": icao.upper(), "name": airport["name"], "city": airport["city"], "country": airport["country"]}
        return (result)
    else:
        return ({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run()