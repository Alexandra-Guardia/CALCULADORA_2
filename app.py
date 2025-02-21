from flask import Flask,render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
#creamos una ruta que solo es accesible por post (si la escribimos directamente en el navegador nos dara error)
@app.route('/calcular', methods=['POST'])
def calculo():
    data = {
        "operacion": request.form["operacion"],
        "num1": int(request.form.get("num1", 0)),  # Convertir a entero
        "num2": int(request.form.get("num2", 0))   # Convertir a entero
    }
    resp = 0
    if data["operacion"] == "suma":
        resp = data["num1"] + data["num2"]
    elif data["operacion"] == "resta":
        resp = data["num1"] - data["num2"]
    elif data["operacion"] == "multiplicacion":
        resp = data["num1"] * data["num2"]
    elif data["operacion"] == "division":
        if data["num2"] != 0:
            resp = data["num1"] / data["num2"]
        else:
            resp = "No se puede dividir por 0"
    return render_template('calculo.html', resp=resp, op=data["operacion"])
