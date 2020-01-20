INITIAL_INDENT = 0
DEFAULT_INDENT = 4
FILLER = " "
TAMPLATE = '{}{}: {}\n'.format


def generate_view(data, indent=INITIAL_INDENT):
    def sign(char=" "):
        return "{}{}{}".format((shift-2) * FILLER, char, FILLER)

    def child():
        return TAMPLATE(
            sign(), key, generate_view(value, shift))

    def removed():
        return TAMPLATE(
            sign("-"), key, value[0])

    def removed_child():
        return TAMPLATE(
            sign("-"), key, generate_view(value[0], shift))

    def added():
        return TAMPLATE(
            sign("+"), key, value[1])

    def added_child():
        return TAMPLATE(
            sign("+"), key, generate_view(value[1], shift))

    def unchanged():
        return TAMPLATE(
            sign(), key, value)

    lines = ["{\n"]
    for key, value in sorted(data.items()):
        if str(value) == 'True':
            value = 'true'
        if str(value) == 'False':
            value = 'false'
        if str(value) == 'None':
            value = 'null'
        shift = indent + DEFAULT_INDENT
        if isinstance(value, dict):
            lines.append(
                child()
            )
        elif isinstance(value, tuple):
            if value[0]:
                if isinstance(value[0], dict):
                    lines.append(
                        removed_child()
                    )
                else:
                    lines.append(
                        removed()
                    )
            if value[1]:
                if isinstance(value[1], dict):
                    lines.append(
                        added_child()
                    )
                else:
                    lines.append(
                        added()
                    )
        else:
            lines.append(
                unchanged())
    lines.append("{}{}".format(indent * FILLER, "}"))
    return "".join(lines)


def render(internal_diff):
    print(generate_view(internal_diff))
