import os 
# import pyautogui as py
import subprocess as sp
import sys
def main(*args):
    print(args[0])
if __name__ == "__main__":
    main(sys.argv)
    print("functional");
    # sp.call(["sh test.sh"])
    os.system("sh command.sh")
    