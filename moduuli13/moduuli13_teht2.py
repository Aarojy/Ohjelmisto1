from flask import Flask
import mysql.connector

connection = mysql.connector.connect(
            host="127.0.0.1",
            database="flight_game",
            port=3306,
            username="root",
            password="root",
            autocommit=True
            )

app = Flask(__name__)

@app.route('/ICAO/<ICAO>')
def ICAO(ICAO):
    sql = ('SELECT airport.name, airport.municipality '
           f'FROM airport WHERE airport.ident = "{ICAO}"')

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    return {'ICAO': ICAO, 'NAME': result[0][0], "MUNICIPALITY": result[0][1]}

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5001, use_reloader=True)
