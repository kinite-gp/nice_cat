import sys
from models import *
from book import *
from paint import *

# bypass argv empty!!!!
try:
    arg = sys.argv
except:
    arg = "ncat 'FILENAME or STRING'"

if arg[1] == "--help" or arg[1] == "-help" or arg[1] == "-h" or arg[1] == "--h":
    ncat_help()
    sys.exit(1)

try:
    file = open(arg[1], "r")
    file = file.read()

    plot("start")
    plot(action="header",body=f"{formats[get_format(arg[1])]} File: {arg[1]}")
    plot("midd")

    file = sprayer(file,get_format(arg[1]))

    for line in file:
        plot(action="",line_number=get_line_number(file.index(line)),body=line)

    plot("end")

except:
    plot("start")
    plot(action="header",body=arg[1])
    plot("end")
