def generate_view(data):
    result = {}
    for key, value in data.items():
        if isinstance(value, dict):
            result.update({key: generate_view(value)})
        elif isinstance(value, tuple):
            if value[0] == 'modified':
                result.update(
                    {
                        key: {
                            "status": "modified",
                            "removed value": value[1][0],
                            "added value": value[1][1]
                        }
                    }
                )
            if value[0] == 'added':
                result.update(
                    {
                        key: {
                            "status": "added",
                            "value": value[1]
                        }
                    }
                )
            if value[0] == 'removed':
                result.update(
                    {
                        key: {
                            "status": "removed",
                            "value": value[1]
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
