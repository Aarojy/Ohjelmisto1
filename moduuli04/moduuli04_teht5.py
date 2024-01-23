right_username = "python"
right_password = "rules"

username = input("Syötä käyttäjätunnus: ")
password = input("Syötä salasana: ")

times_guessed = 0

while times_guessed < 4 and (username != right_username or password != right_password):
    times_guessed += 1
    print(f"Kirjautumistiedot väärin! Yrityksiä jäljellä {5-times_guessed} Yritä uudestaan.p")
    username = input("Syötä käyttäjätunnus: ")
    password = input("Syötä salasana: ")

if username == right_username and password == right_password:
    print("Tervetuloa!")
else:
    print("Pääsy evätty!")
