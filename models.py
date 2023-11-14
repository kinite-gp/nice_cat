from os import getcwd,get_terminal_size

path = getcwd()
columns, lines = get_terminal_size()
calc__ = lambda width, space: width-space
rcalc = calc__(columns, 8)*"─"

def get_format(arg):
    file = arg.split(".")
    filetype = file[-1]
    return filetype.lower()

def get_line_number(index):
    r = 7 - (len(str(index)) + 1)
    r = r*" "
    return f"{r}{index}"

def plot(action, body=None, line_number=None):
    if action == "start":
        print("───────┬"+rcalc)
    elif action == "midd":
        print("───────┼"+rcalc)
    elif action == "end":
        print("───────┴"+rcalc)
    elif action == "header":
        print(f"       │ {body}")
    else:
        print(f"{line_number} │ {body}")

def ncat_help():
    print("ncat 'FILENAME or STRING'")

