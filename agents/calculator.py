from agents.prompts.calculator_prompt import (CALCULATOR_PROMPT)
from utils.ollama_client import ask_llm
from utils.calculator_parser import (parse_calculator_response)
from tools.math_tools import (sumar,restar,multiplicar,dividir,potencia,raiz,evaluar_expresion)


class CalculatorAgent:

    def __init__(self):

        self.tools = {
            "sumar": sumar,
            "restar": restar,
            "multiplicar": multiplicar,
            "dividir": dividir,
            "potencia": potencia,
            "raiz": raiz,
            "evaluar_expresion": evaluar_expresion
        }

    def run(self, task: str):

        print("\n[CALCULADOR]")
        print(f"Tarea: {task}")

        llm_response = ask_llm(
            CALCULATOR_PROMPT,
            task
        )

        print(
            f"[CALCULADOR] Decision: "
            f"{llm_response}"
        )

        action = parse_calculator_response(
            llm_response
        )

        tool_name = action["TOOL"]

        if tool_name not in self.tools:

            return (
                "No pude determinar "
                "la herramienta adecuada."
            )

        if tool_name == "evaluar_expresion":
            expression = action["EXPRESSION"]

            if not expression:
                return "Falta la expresion a evaluar."

            result = self.tools[tool_name](
                expression
            )

            return (
                f"Herramienta usada: {tool_name}\n"
                f"Expresion: {expression}\n"
                f"Resultado: {result}"
            )

        result = self.tools[
            tool_name
        ](*action["ARGS"])

        return (
            f"Herramienta usada: "
            f"{tool_name}\n"
            f"Resultado: {result}"
        )
