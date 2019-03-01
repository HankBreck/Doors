import random
from script import run

def initiation():
    if (init == "Y"):
        run()
    elif (init == "N"):
        quit()
    else:
        print("Please enter either \'Y\' or \'N\'")
while True:
    init = input("Do you wish to start a new game? [Y/N]\n")
    initiation()
