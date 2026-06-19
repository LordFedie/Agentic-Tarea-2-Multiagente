from ollama import chat
from config import OLLAMA_MODEL


def ask_llm(system_prompt: str, user_message: str):

    print(f"[OLLAMA] Modelo: {OLLAMA_MODEL}")
    print(f"[OLLAMA] Consulta: {user_message}")

    response = chat(
        model=OLLAMA_MODEL,
        messages=[   # ← aquí sí hay coma arriba
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        options={    # ← opcional pero recomendado
            "num_gpu": 0
        }
    )

    print("[OLLAMA] Respuesta recibida")

    return response.message.content