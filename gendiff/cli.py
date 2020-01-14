INDENT = 4
TAMPLATE = '{token:>{indent}} {key}: {value}'



def make_result(diff, indent=INDENT):
    result = ['{']

    def add_line(item, value, token="", line_indent=indent):
        return "\n" + TAMPLATE.format(
            token=token,
            indent=line_indent-1,
            key=item,
            value=value,
        )

    for key in sorted(diff):
        if isinstance(diff[key], dict):
            result.append(
                add_line(key, make_result(diff[key], indent=indent + indent))
            )
        elif isinstance(diff[key], tuple):
            if diff[key][0]:
                result.append(add_line(key, diff[key][0], token="-"))
            if diff[key][1]:
                result.append(add_line(key, diff[key][1], token="+"))
        else:
            result.append(add_line(key, diff[key]))
    result.append("\n{0:>{indent}}".format("", indent=indent*2-INDENT*2))
    result.append("}")
    return "".join(result)


def render(diff):
    print(make_result(diff))
    return make_result(diff)
