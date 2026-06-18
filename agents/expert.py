from tools.search_tools import web_search
from utils.ollama_client import ask_llm


SYSTEM_PROMPT = """
Eres un experto académico.

Tu trabajo es explicar conceptos de forma clara,
breve y correcta utilizando la información recibida.
"""


class ExpertAgent:

    def run(self, query: str):

        print("\n[EXPERTO]")
        print(f"Consulta: {query}")

        search_query = (
            query
            .replace("¿Qué es", "")
            .replace("qué es", "")
            .replace("?", "")
            .strip()
        )

        search_results = web_search(search_query)

        context = ""

        for result in search_results[:3]:

            context += (
                f"Titulo: {result['title']}\n"
                f"Contenido: {result['body']}\n\n"
            )

        response = ask_llm(
            SYSTEM_PROMPT,
            f"Pregunta: {query}\n\nInformación:\n{context}"
        )

        return response