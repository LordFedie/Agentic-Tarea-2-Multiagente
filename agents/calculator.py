from utils.ollama_client import ask_llm


SYSTEM_PROMPT = """
Eres el Agente Calculador.

Tu trabajo es:
- Resolver operaciones matemáticas.
- Explicar brevemente el resultado.
- Nunca responder preguntas de calendario.
- Nunca responder preguntas conceptuales.
"""


class CalculatorAgent:

    def run(self, task: str):

        print("\n======================")
        print("[CALCULADOR]")
        print("======================")
        print(f"Tarea recibida: {task}")

        response = ask_llm(
            SYSTEM_PROMPT,
            task
        )

        print("[CALCULADOR] Tarea completada")

        return response