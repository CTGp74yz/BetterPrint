import colorama
from colorama import Fore, Back
from file import method

def SingleWord(Color,BackA,Text):
    split = Text.split(" ")
    Loop = -1
    string = ""
    for i in range(len(split)):
        Loop += 1
        if Color[Loop].lower() == "none":
            foreVar = Fore.RESET
        if Color[Loop].lower() == "red":
            foreVar = Fore.RED
        if Color[Loop].lower() == "blue":
            foreVar = Fore.BLUE
        if Color[Loop].lower() == "green":
            foreVar = Fore.GREEN
        if Color[Loop].lower() == "yellow":
            foreVar = Fore.YELLOW
        if Color[Loop].lower() == "white":
            foreVar = Fore.WHITE
        if Color[Loop].lower() == "cyan":
            foreVar = Fore.CYAN
        if Color[Loop].lower() == "black":
            foreVar = Fore.BLACK
        if Color[Loop].lower() == "magenta":
            foreVar = Fore.MAGENTA

        if BackA[Loop].lower() == "none":
            backVar = Back.RESET
        if BackA[Loop].lower() == "red":
            backVar = Back.RED
        if BackA[Loop].lower() == "blue":
            backVar = Back.BLUE
        if BackA[Loop].lower() == "green":
            backVar = Back.GREEN
        if BackA[Loop].lower() == "yellow":
            backVar = Back.YELLOW
        if BackA[Loop].lower() == "white":
            backVar = Back.WHITE
        if BackA[Loop].lower() == "cyan":
            backVar = Back.CYAN
        if BackA[Loop].lower() == "black":
            backVar = Back.BLACK
        if BackA[Loop].lower() == "magenta":
            backVar = Back.MAGENTA


        string += backVar + foreVar + f"{split[Loop]} "
    print(string)