

_STATUS = "status"
_VALUE = "value"
_REMOVED_VALUE = "removed value"
_ADDED_VALUE = "added value"


# avaliable statuses
MOD = "modified"
ADD = "added"
REM = "removed"
UNC = "unchanged"


def generate_view(data):
    result = {}
    for key, value in sorted(data.items()):
        if isinstance(value, dict):
            result.update({key: generate_view(value)})
        elif isinstance(value, tuple):
            if value[0] and value[1]:
                result.update({key: {_STATUS: MOD,
                                     _REMOVED_VALUE: value[0],
                                     _ADDED_VALUE: value[1]
                                     }}
                              )
            if not value[0]:
                result.update({key: {_STATUS: ADD, _VALUE: value[1]}})
            if not value[1]:
                result.update({key: {_STATUS: REM, _VALUE: value[0]}})
        else:
            result.update(
                {key: {_STATUS: UNC, _VALUE: value}}
            )
    return result


def render(internal_diff):
    return generate_view(internal_diff)
