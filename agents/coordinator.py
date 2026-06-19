from agents.calculator import CalculatorAgent
from agents.organizer import OrganizerAgent
from agents.expert import ExpertAgent
from agents.critic import CriticAgent

from agents.prompts.coordinator_prompt import (
    COORDINATOR_PROMPT
)

from utils.ollama_client import ask_llm


class CoordinatorAgent:

    def __init__(self):

        self.calculator = CalculatorAgent()
        self.organizer = OrganizerAgent()
        self.expert = ExpertAgent()
        self.critic = CriticAgent()

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

        # Calculator
        if "calculator" in decision:

            response = self.calculator.run(
                user_message
            )

            review = self.critic.run(
                user_message,
                response
            )

            print(
                f"[CRITIC] Veredicto: {review}"
            )

            return response

        # Organizer
        if "organizer" in decision:

            response = self.organizer.run(
                user_message
            )

            review = self.critic.run(
                user_message,
                response
            )

            print(
                f"[CRITIC] Veredicto: {review}"
            )

            return response

        # Expert
        response = self.expert.run(
            user_message
        )

        review = self.critic.run(
            user_message,
            response
        )

        print(
            f"[CRITIC] Veredicto: {review}"
        )

        if "invalid" in review.lower():

            print("[COORDINADOR] Respuesta rechazada por el CRITIC")

            return (
                "Hubo un problema al procesar la solicitud. "
                "Intenta reformularla."
            )

        return response