import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
 )
def find_airport_by_ICAO(iso_country):
    sql = f"SELECT type FROM airport WHERE iso_country = '{iso_country}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    dict_of_types = {}
    for row in result:
        if row[0] not in dict_of_types:
            dict_of_types.update({row[0]:1})
        else:
            dict_of_types[row[0]] += 1

    return dict_of_types

iso_country_input = input("Syötä maakoodi: ")
found_airport = find_airport_by_ICAO(iso_country_input)
if found_airport:
    print(f"Syöttämälläsi maakoodilla {iso_country_input} löytyi:")
    for airport in found_airport:
        print(f"Lentokenttätyyppiä: {airport}, {found_airport.get(airport)}-kappaletta")
else:
    print("Syöttämäsi maakoodi ei vastaa mitään maata tai maassa ei ole yhtään lentokenttää.")