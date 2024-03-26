import requests

user_input = input("Syötä paikkakunta: ")

try:
    pyynto = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid=7cc813f152116cb974a24d671691cf51')
    tulos = pyynto.json()

    print(f'Paikassa {user_input.title()} säätila on: "{tulos["weather"][0]["main"]}" ja lämpötila on: {tulos["main"]["temp"]-272.15:.1f} celsius astetta')

except KeyError as e:
    print("Valitsemaasi paikkakuntaa ei löydy!:(")

except Exception as e:
    print("Jokin meni vikaan!:(")