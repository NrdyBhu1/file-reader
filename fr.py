import sys
import colorama


colorama.init()

if not len(sys.argv) > 1:
    print(colorama.Style.BRIGHT + colorama.Fore.GREEN + "Usage: fr <file>" + colorama.Style.RESET_ALL)
    sys.exit()

filename = sys.argv[1]

try:
    with open(filename, "r") as f:
        data = f.read()

    print("----------------------------")
    print(filename)
    print("----------------------------")
    print(data)
    print("----------------------------")
except Exception as e:
    print(colorama.Fore.RED)
    print("That File does not exist!!")
    print(e)
    print(colorama.Style.RESET_ALL)
