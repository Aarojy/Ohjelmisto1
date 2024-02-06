import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
 )
def find_airport_by_ICAO(ICAO):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{ICAO}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchone()
    kursori.fetchall()
    return result

ICAO_input = input("Syötä lentokentän ICAO-koodi: ")
found_airport = find_airport_by_ICAO(ICAO_input)
if found_airport:
    print(f"Syöttämälläsi ICAO-koodilla: {ICAO_input} löytyi lentokenttä nimeltä: {found_airport[0]}, joka sijaitsee kunnassa nimeltä {found_airport[1]}.")
else:
    print(f"Syöttämälläsi ICAO-koodilla: {ICAO_input} ei löytynyt lentokoenttää.")