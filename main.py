from agents.calculator import CalculatorAgent


def main():

    print("\n===== INICIO DEL SISTEMA =====")

    calculator = CalculatorAgent()

    result = calculator.run(
        "¿Cuánto es la raíz cuadrada de 256?"
    )

    print("\n===== RESPUESTA FINAL =====")
    print(result)


if __name__ == "__main__":
    main()