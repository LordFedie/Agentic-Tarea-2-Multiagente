import ast
import math
import operator
import re


ALLOWED_BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
}

ALLOWED_UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


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
            "No se puede calcular la raiz cuadrada de un numero negativo"
        )

    return math.sqrt(numero)


def evaluar_expresion(expression: str) -> float:
    print(f"[MATH TOOL] evaluar_expresion({expression})")

    normalized_expression = (
        expression
        .replace("^", "**")
        .replace("×", "*")
        .replace("÷", "/")
        .replace("√", "sqrt")
    )

    normalized_expression = re.sub(
        r"(?<=\d)\s*x\s*(?=\d|\()",
        " * ",
        normalized_expression,
        flags=re.IGNORECASE
    )

    parsed_tree = ast.parse(
        normalized_expression,
        mode="eval"
    )

    return _evaluate_node(parsed_tree.body)


def _evaluate_node(node):

    if isinstance(node, ast.Constant):
        value = node.value

        if not isinstance(value, (int, float)):
            raise ValueError("La expresion contiene valores no permitidos")

        return float(value)

    if isinstance(node, ast.BinOp):
        operator_type = type(node.op)

        if operator_type not in ALLOWED_BINARY_OPERATORS:
            raise ValueError("Operador no permitido")

        left = _evaluate_node(node.left)
        right = _evaluate_node(node.right)

        if operator_type is ast.Div and right == 0:
            raise ValueError("No se puede dividir por cero")

        return ALLOWED_BINARY_OPERATORS[operator_type](left, right)

    if isinstance(node, ast.UnaryOp):
        operator_type = type(node.op)

        if operator_type not in ALLOWED_UNARY_OPERATORS:
            raise ValueError("Operador unario no permitido")

        operand = _evaluate_node(node.operand)

        return ALLOWED_UNARY_OPERATORS[operator_type](operand)

    if isinstance(node, ast.Call):

        if not isinstance(node.func, ast.Name):
            raise ValueError("Funcion no permitida")

        if node.func.id != "sqrt" or len(node.args) != 1:
            raise ValueError("Solo se permite la funcion sqrt")

        return raiz(_evaluate_node(node.args[0]))

    raise ValueError("Expresion no permitida")
