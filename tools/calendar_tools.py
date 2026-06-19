import json
from pathlib import Path


CALENDAR_FILE = Path("data/calendar.json")


def load_calendar():

    print("[CALENDAR TOOL] Cargando calendario")

    if not CALENDAR_FILE.exists():
        print("[CALENDAR TOOL] No existe calendario, creando estructura vacía")
        return {"events": []}

    with open(CALENDAR_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_calendar(data):
    with open(CALENDAR_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def add_event(title, date, time):
    data = load_calendar()

    event = {
        "title": title,
        "date": date,
        "time": time
    }

    data["events"].append(event)

    save_calendar(data)

    print(f"[CALENDAR TOOL] Evento agregado: {event}")

    return event


def get_events_by_date(date):
    data = load_calendar()

    return [
        event
        for event in data["events"]
        if event["date"] == date
    ]


def update_event(title, new_time, date=None):

    data = load_calendar()

    for event in data["events"]:

        title_match = (
            title.lower()
            in event["title"].lower()
        )

        date_match = (
            True
            if date is None
            else event["date"] == date
        )

        if title_match and date_match:

            event["time"] = new_time

            save_calendar(data)

            print(
                f"[CALENDAR TOOL] Evento actualizado: "
                f"{event}"
            )

            return event

    return None


def delete_event(title, date=None):

    data = load_calendar()

    for i, event in enumerate(data["events"]):

        title_match = (
            title.lower()
            in event["title"].lower()
        )

        date_match = (
            True
            if date is None
            else event["date"] == date
        )

        if title_match and date_match:

            removed = data["events"].pop(i)

            save_calendar(data)

            print(
                f"[CALENDAR TOOL] Evento eliminado: "
                f"{removed}"
            )

            return removed

    return None

def delete_all_events():

    data = {"events": []}

    save_calendar(data)

    print(
        "[CALENDAR TOOL] Todos los eventos eliminados"
    )

    return True