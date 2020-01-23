def generate_view(data):
    result = {}
    for key, value in data.items():
        if isinstance(value, dict):
            result.update({key: generate_view(value)})
        elif isinstance(value, tuple):
            if value[0] and value[1]:
                result.update(
                    {
                        key: {
                            "status": "modified",
                            "removed value": value[0],
                            "added value": value[1]
                        }
                    }
                )
            if not value[0]:
                result.update(
                    {
                        key: {
                            "status": "added",
                            "value": value[1]
                        }
                    }
                )
            if not value[1]:
                result.update(
                    {
                        key: {
                            "status": "removed",
                            "value": value[0]
                        }
                    }
                )
        else:
            result.update(
                {
                    key: {
                        "status": "unchanged",
                        "value": value
                    }
                }
            )
    return result


def render(internal_diff):
    return generate_view(internal_diff)
