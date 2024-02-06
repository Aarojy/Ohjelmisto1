import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
 )
def find_airport_coords(ICAO):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{ICAO}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchone()
    kursori.fetchall()
    return result

ICAO1 = input("Syötä maan 1 ÍCAO-koodi: ")
ICAO2 = input("Syötä maan 2 ÍCAO-koodi: ")
Coords_1 = find_airport_coords(ICAO1)
Coords_2 = find_airport_coords(ICAO2)

distance = distance.distance(Coords_1, Coords_2)
print(f"Syöttämiesi lentokenttien etäisyys on {float(str(distance).split()[0]):.2f} kilometriä")
