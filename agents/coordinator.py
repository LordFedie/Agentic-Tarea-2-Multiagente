from agents.calculator import CalculatorAgent
from agents.organizer import OrganizerAgent
from agents.expert import ExpertAgent
from agents.prompts.coordinator_prompt import (COORDINATOR_PROMPT)
from utils.ollama_client import ask_llm

def normalize(text):

    return ''.join(
        c for c in unicodedata.normalize(
            'NFD',
                text
        )
        if unicodedata.category(c) != 'Mn'
    ).lower()

class CoordinatorAgent:

    def __init__(self):

        self.calculator = CalculatorAgent()
        self.organizer = OrganizerAgent()
        self.expert = ExpertAgent()

    def run(self, user_message: str):

        print("\n[COORDINADOR]")
        print(f"Consulta recibida: {user_message}")

        decision = ask_llm(
            COORDINATOR_PROMPT,
            user_message
        )

        print("[COORDINADOR] Respuesta cruda:")
        print(repr(decision))

        print(f"[COORDINADOR] Decisión: {decision}")

        decision = decision.lower()

        if "calculator" in decision:

            return self.calculator.run(
                user_message
            )

        if "organizer" in decision:

            return self.organizer.run(
                user_message
            )

        return self.expert.run(
            user_message
        )
