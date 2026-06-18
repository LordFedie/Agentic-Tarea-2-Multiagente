def parse_organizer_response(response):

    result = {}

    for line in response.splitlines():

        if ":" not in line:
            continue

        key, value = line.split(":", 1)

        result[key.strip().upper()] = value.strip()

    return result