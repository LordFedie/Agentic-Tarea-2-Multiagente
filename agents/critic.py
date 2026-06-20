import re

from agents.prompts.critic_prompt import (
    CRITIC_PROMPT
)

from utils.ollama_client import ask_llm


NUMBER_PATTERN = re.compile(
    r"(?<![\w.])-?\d+(?:\.\d+)?"
)


class CriticAgent:

    def run(
        self,
        user_message,
        agent_response
    ):

        review_prompt = f"""
Pregunta:
{user_message}

Respuesta:
{agent_response}
"""

        review = ask_llm(
            CRITIC_PROMPT,
            review_prompt
        )

        review = self._normalize_numeric_format_dispute(
            review,
            agent_response
        )

        print("\n[CRITIC]")
        print(review)

        return review

    def _normalize_numeric_format_dispute(
        self,
        review: str,
        agent_response: str
    ) -> str:

        if "invalid" not in review.lower():
            return review

        response_numbers = self._extract_numbers(
            agent_response
        )

        review_numbers = self._extract_numbers(
            review
        )

        if not response_numbers or len(review_numbers) < 2:
            return review

        expected_value = review_numbers[-1]

        for response_value in response_numbers:
            if response_value == expected_value:
                return (
                    "VALID\n"
                    "La diferencia detectada era solo de formato numerico."
                )

        return review

    def _extract_numbers(self, text: str):
        numbers = []

        for match in NUMBER_PATTERN.findall(text):
            try:
                numbers.append(float(match))
            except ValueError:
                continue

        return numbers
