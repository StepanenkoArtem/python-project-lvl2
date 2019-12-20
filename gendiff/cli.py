def output(text, view):
    if view == 'json':
        print("{open_bracket}\n{text}\n{close_bracket}".format(
            open_bracket="{",
            text=text,
            close_bracket="}")
        )
