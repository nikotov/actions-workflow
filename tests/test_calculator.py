from app.calculator import suma, resta, multiplicacion
from app.web_service import app

# Unitary tests
def test_suma() -> None:
    assert suma(2, 3) == 5

def test_resta() -> None:
    assert resta(5, 3) == 2

def test_multiplicacion() -> None:
    assert multiplicacion(2, 3) == 6


def test_suma_endpoint() -> None:
    client = app.test_client()
    response = client.post("/suma", json={"a": 2, "b": 3})

    assert response.status_code == 200
    assert response.get_json() == {"result": 5}


def test_resta_endpoint() -> None:
    client = app.test_client()
    response = client.post("/resta", json={"a": 5, "b": 3})

    assert response.status_code == 200
    assert response.get_json() == {"result": 2}


def test_multiplicacion_endpoint() -> None:
    client = app.test_client()
    response = client.post("/multiplicacion", json={"a": 2, "b": 3})

    assert response.status_code == 200
    assert response.get_json() == {"result": 6}


def test_endpoint_rejects_invalid_payload() -> None:
    client = app.test_client()
    response = client.post("/suma", json={"a": "2", "b": 3})

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "Payload must include integer fields 'a' and 'b'."
    }