def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division par zéro impossible.")
    return a / b
