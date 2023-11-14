import syntex


def sprayer(text,file_type):

    if file_type == "py":
        out = syntex.py(text)
    elif file_type == "txt":
        out = syntex.py(text)

    return out