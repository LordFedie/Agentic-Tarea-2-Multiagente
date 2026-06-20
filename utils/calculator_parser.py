def parse_calculator_response(response):

    action = {
        "TOOL": None,
        "ARGS": [],
        "EXPRESSION": None
    }

    for line in response.splitlines():

        if line.startswith("TOOL:"):
            action["TOOL"] = line.replace(
                "TOOL:",
                ""
            ).strip()

        if line.startswith("ARGS:"):

            raw_args = line.replace(
                "ARGS:",
                ""
            ).strip()

            action["ARGS"] = [
                float(x.strip())
                for x in raw_args.split(",")
                if x.strip()
            ]

        if line.startswith("EXPRESSION:"):
            action["EXPRESSION"] = line.replace(
                "EXPRESSION:",
                ""
            ).strip()

    return action
