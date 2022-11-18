#!/usr/bin/python3 
from CoolBlueC2 import CBC2Main, output
import sys
import os
import time

sys.path.append("CoolBlueC2")


def loaddata():
    if not os.path.exists("./data/"):
        os.mkdir("./data/")

    if not os.path.exists("./data/listeners/"):
        os.mkdir("./data/listeners/")


if __name__ == "__main__":
    loaddata()
    main = CBC2Main.MainMenu()
    for _ in output.banner:
        sys.stdout.write(_)
        sys.stdout.flush()
        time.sleep(0.0008)
    main.cmdloop()
