import os
import platform, sys

def sastantua(n):
    path = ""
    if platform.system() == "Linux":
        path = "./bin/sastantua_linux"
    elif platform.system() == "Darwin":
        path = "./bin/sastantua_mac"
    elif platform.system() == "Windows":
        director = str(os.getcwd()).replace("\\","/")
        path = director + "/bin/sastantua_windows.exe"

    path += " "
    path += str(n)
    list_dir = os.popen(path)
    l = list_dir.readlines()
    for i in l:
        print(i, end='')

try:
    n = int(sys.argv[1])
except ValueError:
    n = -1
except IndexError:
    n = -1

sastantua(n)
