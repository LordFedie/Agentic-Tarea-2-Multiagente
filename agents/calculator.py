from agents.prompts.calculator_prompt import (CALCULATOR_PROMPT)
from utils.ollama_client import ask_llm
from utils.calculator_parser import (parse_calculator_response)
from tools.math_tools import (sumar,restar,multiplicar,dividir,potencia,raiz)


class CalculatorAgent:

    def __init__(self):

        self.tools = {
            "sumar": sumar,
            "restar": restar,
            "multiplicar": multiplicar,
            "dividir": dividir,
            "potencia": potencia,
            "raiz": raiz
        }

    def run(self, task: str):

        print("\n[CALCULADOR]")
        print(f"Tarea: {task}")

        llm_response = ask_llm(
            CALCULATOR_PROMPT,
            task
        )

        print(
            f"[CALCULADOR] Decisión: "
            f"{llm_response}"
        )

        tool_name, args = parse_calculator_response(
            llm_response
        )

        if tool_name not in self.tools:

            return (
                "No pude determinar "
                "la herramienta adecuada."
            )

        result = self.tools[
            tool_name
        ](*args)

        return (
            f"Herramienta usada: "
            f"{tool_name}\n"
            f"Resultado: {result}"
        )