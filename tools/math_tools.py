import math


def sumar(a: float, b: float) -> float:
    return a + b


def restar(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


def potencia(base: float, exponente: float) -> float:
    return base ** exponente


def raiz(numero: float) -> float:
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return math.sqrt(numero)