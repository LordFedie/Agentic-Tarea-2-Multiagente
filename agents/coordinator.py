from agents.calculator import CalculatorAgent
from agents.organizer import OrganizerAgent
from agents.expert import ExpertAgent
from agents.critic import CriticAgent

from agents.prompts.coordinator_prompt import (
    COORDINATOR_PROMPT
)

from utils.ollama_client import ask_llm
from utils.query_decomposer import split_compound_request


class CoordinatorAgent:

    def __init__(self):

        self.calculator = CalculatorAgent()
        self.organizer = OrganizerAgent()
        self.expert = ExpertAgent()
        self.critic = CriticAgent()

    def run(self, user_message: str):

        print("\n[COORDINADOR]")
        print(f"Consulta recibida: {user_message}")

        tasks = split_compound_request(
            user_message
        )

        print(f"[COORDINADOR] Subtareas detectadas: {len(tasks)}")

        final_responses = []

        for index, task in enumerate(tasks, start=1):

            print(f"\n[COORDINADOR] Subtarea {index}: {task}")

            decision = ask_llm(
                COORDINATOR_PROMPT,
                task
            )

            print("[COORDINADOR] Respuesta cruda:")
            print(repr(decision))

            normalized_decision = decision.lower()

            print(f"[COORDINADOR] Decision: {decision}")

            response, review = self._execute_with_retry(
                normalized_decision,
                task
            )

            if "invalid" in review.lower():

                print(
                    "[COORDINADOR] La subtarea fue rechazada "
                    "tras dos intentos"
                )

                return (
                    "Hubo un problema al procesar la solicitud. "
                    f"Subtarea rechazada: {task}"
                )

            final_responses.append(
                f"Subtarea {index}: {response}"
            )

        if len(final_responses) == 1:
            return final_responses[0].replace(
                "Subtarea 1: ",
                "",
                1
            )

        return "\n\n".join(final_responses)

    def _execute_with_retry(
        self,
        decision: str,
        task: str
    ):

        response = self._run_specialist(
            decision,
            task
        )

        review = self.critic.run(
            task,
            response
        )

        print(
            f"[CRITIC] Veredicto: {review}"
        )

        if "invalid" not in review.lower():
            return response, review

        print(
            "[COORDINADOR] Reintentando subtarea con "
            "retroalimentacion del CRITIC"
        )

        retry_task = self._build_retry_task(
            task,
            review
        )

        retry_response = self._run_specialist(
            decision,
            retry_task
        )

        retry_review = self.critic.run(
            task,
            retry_response
        )

        print(
            f"[CRITIC] Veredicto reintento: {retry_review}"
        )

        return retry_response, retry_review

    def _build_retry_task(
        self,
        task: str,
        review: str
    ) -> str:

        return (
            f"{task}\n\n"
            "Retroalimentacion del critic:\n"
            f"{review}\n\n"
            "Corrige la respuesta anterior. "
            "Debes cumplir exactamente la solicitud original "
            "y evitar el error indicado por el critic."
        )

    def _run_specialist(
        self,
        decision: str,
        user_message: str
    ):

        if "calculator" in decision:
            return self.calculator.run(user_message)

        if "organizer" in decision:
            return self.organizer.run(user_message)

        return self.expert.run(user_message)
