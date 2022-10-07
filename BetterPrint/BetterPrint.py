import colorama
from file import method
from colorama import Fore, Back, Style
from time import sleep

def BetterPrint(Color, Back, Text, Pause,Styl,IsLight):
    Styled = False
    if Styl.lower() == "normal":
        StyVar = Style.NORMAL
        Styled = True
    if Styl.lower() == "bright":
        StyVar = Style.BRIGHT
        Styled = True
    if Styl.lower() == "dim":
        StyVar = Style.DIM
        Styled = True
    if Styled != True:
        StyVar = "0"
    if IsLight:
        if Back.lower() == "none":
            backVar = Back.RESET
        if Back.lower() == "red":
            backVar = Back.LIGHTRED_EX
        if Back.lower() == "blue":
            backVar = Back.LIGHTBLUE_EX
        if Back.lower() == "green":
            backVar = Back.LIGHTGREEN_EX
        if Back.lower() == "yellow":
            backVar = Back.LIGHTYELLOW_EX
        if Back.lower() == "white":
            backVar = Back.LIGHTWHITE_EX
        if Back.lower() == "cyan":
            backVar = Back.LIGHTCYAN_EX
        if Back.lower() == "black":
            backVar = Back.LIGHTBLACK_EX
        if Back.lower() == "magenta":
            backVar = Back.LIGHTMAGENTA_EX
    else:
        if Back.lower() == "none":
            backVar = Back.RESET
        if Back.lower() == "red":
            backVar = Back.RED
        if Back.lower() == "blue":
            backVar = Back.BLUE
        if Back.lower() == "green":
            backVar = Back.GREEN
        if Back.lower() == "yellow":
            backVar = Back.YELLOW
        if Back.lower() == "white":
            backVar = Back.WHITE
        if Back.lower() == "cyan":
            backVar = Back.CYAN
        if Back.lower() == "black":
            backVar = Back.BLACK
        if Back.lower() == "magenta":
            backVar = Back.MAGENTA
    if IsLight:
        if Color.lower() == "none":
            foreVar = Fore.RESET
        if Color.lower() == "red":
            foreVar = Fore.LIGHTRED_EX
        if Color.lower() == "blue":
            foreVar = Fore.LIGHTBLUE_EX
        if Color.lower() == "green":
            foreVar = Fore.LIGHTGREEN_EX
        if Color.lower() == "yellow":
            foreVar = Fore.LIGHTYELLOW_EX
        if Color.lower() == "white":
            foreVar = Fore.LIGHTWHITE_EX
        if Color.lower() == "cyan":
            foreVar = Fore.LIGHTCYAN_EX
        if Color.lower() == "black":
            foreVar = Fore.LIGHTBLACK_EX
        if Color.lower() == "magenta":
            foreVar = Fore.LIGHTMAGENTA_EX
    else:
        if Color.lower() == "none":
            foreVar = Fore.RESET
        if Color.lower() == "red":
            foreVar = Fore.RED
        if Color.lower() == "blue":
            foreVar = Fore.BLUE
        if Color.lower() == "green":
            foreVar = Fore.GREEN
        if Color.lower() == "yellow":
            foreVar = Fore.YELLOW
        if Color.lower() == "white":
            foreVar = Fore.WHITE
        if Color.lower() == "cyan":
            foreVar = Fore.CYAN
        if Color.lower() == "black":
            foreVar = Fore.BLACK
        if Color.lower() == "magenta":
            foreVar = Fore.MAGENTA
    if StyVar != "0":
        print(StyVar +  foreVar + f"{Text}")
    else:
        print(foreVar + f"{Text}")
    sleep(Pause)



