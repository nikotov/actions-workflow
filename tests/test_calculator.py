from app.calculator import suma, resta, multiplicacion

def test_sum() -> None:
    assert suma(2, 3) == 5

# Introducir un fallo premeditado!
def test_resta() -> None:
    assert resta(5, 3) == 2

def test_multiply() -> None:
    assert multiplicacion(2, 3) == 6