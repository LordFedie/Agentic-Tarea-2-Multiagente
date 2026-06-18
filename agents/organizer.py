from agents.prompts.organizer_prompt import (ORGANIZER_PROMPT)
from utils.ollama_client import ask_llm
from utils.organizer_parser import (parse_organizer_response)
from tools.calendar_tools import (add_event,update_event,delete_event,get_events_by_date)


class OrganizerAgent:

    def run(self, task: str):

        print("\n[ORGANIZER]")
        print(f"Tarea: {task}")

        llm_response = ask_llm(
            ORGANIZER_PROMPT,
            task
        )

        print(
            f"[ORGANIZER] Decisión:\n"
            f"{llm_response}"
        )

        action = parse_organizer_response(
            llm_response
        )

        tool = action.get("TOOL")

        if tool == "add_event":

            result = update_event(
                title=action["TITLE"],
                new_time=action["TIME"],
                date=action.get("DATE")
            )

            return (
                f"Evento agregado:\n"
                f"{result}"
            )

        if tool == "update_event":

            result = update_event(
                action["TITLE"],
                action["DATE"],
                action["TIME"]
            )

            return (
                f"Evento actualizado:\n"
                f"{result}"
            )

        if tool == "delete_event":

            result = delete_event(
                action["TITLE"],
                action["DATE"]
            )

            return (
                f"Evento eliminado:\n"
                f"{result}"
            )

        if tool == "get_events_by_date":

            result = get_events_by_date(
                action["DATE"]
            )

            return (
                f"Eventos encontrados:\n"
                f"{result}"
            )

        return (
            "No pude determinar "
            "la acción a realizar."
        )