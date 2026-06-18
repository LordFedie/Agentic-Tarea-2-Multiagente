import math


def sumar(a: float, b: float) -> float:
    print(f"[MATH TOOL] sumar({a}, {b})")
    return a + b


def restar(a: float, b: float) -> float:
    print(f"[MATH TOOL] restar({a}, {b})")
    return a - b


def multiplicar(a: float, b: float) -> float:
    print(f"[MATH TOOL] multiplicar({a}, {b})")
    return a * b


def dividir(a: float, b: float) -> float:
    print(f"[MATH TOOL] dividir({a}, {b})")

    if b == 0:
        raise ValueError("No se puede dividir por cero")

    return a / b


def potencia(base: float, exponente: float) -> float:
    print(f"[MATH TOOL] potencia({base}, {exponente})")
    return base ** exponente


def raiz(numero: float) -> float:
    print(f"[MATH TOOL] raiz({numero})")

    if numero < 0:
        raise ValueError(
            "No se puede calcular la raíz cuadrada de un número negativo"
        )

    return math.sqrt(numero)