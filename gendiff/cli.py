def output(text, view):
    if view == 'json':
        print("{open_bracket}{text}{close_bracket}".format(
            open_bracket="{\n",
            text=text,
            close_bracket="}")
        )
