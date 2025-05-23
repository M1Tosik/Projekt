import random
import time
import requests

# Adres endpointu backendu Flask (hostowanego na Azure)
SERVER_URL = "https://pogoda-c0fcgsbbcpegbtcv.polandcentral-01.azurewebsites.net/data"

def ocen_jakosc_powietrza(pm10):
    if pm10 <= 13:
        return "Bardzo dobra"
    elif pm10 <= 35:
        return "Dobra"
    elif pm10 <= 75:
        return "Średnia"
    elif pm10 <= 150:
        return "Zła"
    else:
        return "Bardzo zła"

# Inicjalne wartości
temperature = round(random.uniform(-30.0, 35.0), 1)
humidity = round(random.uniform(10.0, 99.0), 1)
dustPM25 = round(random.uniform(0.0, 200.0), 1)
dustPM10 = round(random.uniform(0.0, 300.0), 1)

print("⏱️ Uruchomiono symulację danych środowiskowych...")

while True:
    # Symulacja zmian
    temperature += round(random.uniform(-0.2, 0.2), 1)
    humidity += round(random.uniform(-2.0, 2.0), 1)
    dustPM25 += round(random.uniform(-3.0, 3.0), 1)
    dustPM10 += round(random.uniform(-4.0, 4.0), 1)

    # Zakresy
    temperature = max(-30.0, min(temperature, 35.0))
    humidity = max(10.0, min(humidity, 99.0))
    dustPM25 = max(0.0, min(dustPM25, 300.0))
    dustPM10 = max(0.0, min(dustPM10, 400.0))

    jakosc = ocen_jakosc_powietrza(dustPM10)

    dane = {
        "temperature": temperature,
        "humidity": humidity,
        "pm25": dustPM25,
        "pm10": dustPM10,
        "quality": jakosc
    }

    try:
        response = requests.post(SERVER_URL, json=dane)
        if response.status_code == 200:
            print(f"[✓] Wysłano dane: {dane}")
        else:
            print(f"[✗] Błąd POST: {response.status_code}")
    except Exception as e:
        print(f"[!] Błąd połączenia: {e}")

    time.sleep(2)
