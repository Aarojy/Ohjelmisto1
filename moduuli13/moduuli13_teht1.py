from flask import Flask

app = Flask(__name__)

@app.route('/alkuluku/<type>')
def alkuluku(type):
    print(type)
    type = int(type)
    is_prime = True

    for i in range(2, type // 2):
        if type % i == 0:
            is_prime = False
            break

    if is_prime == True and type != 4:
        return {"Number":type, "isPrime":True}
    return {"Number": type, "isPrime": False}


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5001, use_reloader=True)
