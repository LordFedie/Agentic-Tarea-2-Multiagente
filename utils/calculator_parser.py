def parse_calculator_response(response):

    lines = response.splitlines()

    tool = None
    args = []

    for line in lines:

        if line.startswith("TOOL:"):
            tool = line.replace(
                "TOOL:",
                ""
            ).strip()

        if line.startswith("ARGS:"):

            raw_args = line.replace(
                "ARGS:",
                ""
            ).strip()

            args = [
                float(x.strip())
                for x in raw_args.split(",")
            ]

    return tool, args