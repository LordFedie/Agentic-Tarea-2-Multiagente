from agents.prompts.organizer_prompt import (ORGANIZER_PROMPT)
from utils.ollama_client import ask_llm
from utils.organizer_parser import (parse_organizer_response)
from tools.calendar_tools import (add_event,update_event,delete_event,get_events_by_date,delete_all_events)


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

            title = action.get("TITLE")
            date = action.get("DATE")
            time = action.get("TIME")

            if not title or not date or not time:
                return "Faltan datos para crear el evento."

            result = add_event(
                title=title,
                date=date,
                time=time
            )

            return f"Evento agregado:\n{result}"

        if tool == "update_event":

            title = action.get("TITLE")
            time = action.get("TIME")

            if not title or not time:
                return "Faltan datos para actualizar el evento."

            result = update_event(
                title=title,
                new_time=time,
                date=action.get("DATE")
            )

            return f"Evento actualizado:\n{result}"

        if tool == "delete_event":

            title = action.get("TITLE")

            if not title:
                return "No pude identificar el evento a eliminar."

            result = delete_event(
                title=title,
                date=action.get("DATE")
            )

            return f"Evento eliminado:\n{result}"

        if tool == "get_events_by_date":

            result = get_events_by_date(
                action["DATE"]
            )

            return (
                f"Eventos encontrados:\n"
                f"{result}"
            )

        if action["TOOL"] == "delete_all_events":

            result = delete_all_events()

            return (
                "Todos los eventos fueron "
                "eliminados correctamente."
            )

        return (
            "No pude determinar "
            "la acción a realizar."
        )