from agents.prompts.critic_prompt import (
    CRITIC_PROMPT
)

from utils.ollama_client import ask_llm


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

        print("\n[CRITIC]")
        print(review)

        return review