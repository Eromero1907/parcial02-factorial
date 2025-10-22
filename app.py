from flask import Flask, Response
import json

app = Flask(__name__)

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n debe ser >= 0")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def etiqueta_par_impar(valor: int) -> str:
    return "par" if valor % 2 == 0 else "impar"

@app.route("/calc/<int:n>", methods=["GET"])
def calc(n):
    if n < 0:
        return Response(
            json.dumps({"error": "n debe ser mayor o igual a 0"}, ensure_ascii=False, indent=2),
            status=400,
            mimetype="application/json"
        )

    fact = factorial(n)
    etiqueta = etiqueta_par_impar(n)

    data = {
        "numero": n,
        "factorial": fact,
        "etiqueta": etiqueta
    }

    json_data = json.dumps(data, ensure_ascii=False, sort_keys=False, indent=2)
    return Response(json_data, mimetype="application/json")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
