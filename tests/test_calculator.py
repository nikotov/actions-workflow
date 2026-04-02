from app.calculator import suma, resta, multiplicacion

# Unitary tests
def test_suma() -> None:
    assert suma(2, 3) == 5

def test_resta() -> None:
    assert resta(5, 3) == 2

def test_multiplicacion() -> None:
    assert multiplicacion(2, 3) == 6