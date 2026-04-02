from __future__ import annotations

from flask import Flask, jsonify, request

from app.calculator import multiplicacion, resta, suma

app = Flask(__name__)


def _get_operands() -> tuple[int, int] | tuple[None, None]:
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return None, None

    a = payload.get("a")
    b = payload.get("b")
    if not isinstance(a, int) or not isinstance(b, int):
        return None, None

    return a, b


@app.post("/suma")
def suma_endpoint():
    a, b = _get_operands()
    if a is None or b is None:
        return jsonify({"error": "Payload must include integer fields 'a' and 'b'."}), 400

    return jsonify({"result": suma(a, b)})


@app.post("/resta")
def resta_endpoint():
    a, b = _get_operands()
    if a is None or b is None:
        return jsonify({"error": "Payload must include integer fields 'a' and 'b'."}), 400

    return jsonify({"result": resta(a, b)})


@app.post("/multiplicacion")
def multiplicacion_endpoint():
    a, b = _get_operands()
    if a is None or b is None:
        return jsonify({"error": "Payload must include integer fields 'a' and 'b'."}), 400

    return jsonify({"result": multiplicacion(a, b)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
