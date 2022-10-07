import colorama
from colorama import Fore, Back, Style
from file import method
def InputPrint(Color,BackA,Text,Styl,IsLight):
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
        if BackA.lower() == "none":
            backVar = Back.RESET
        if BackA.lower() == "red":
            backVar = Back.LIGHTRED_EX
        if BackA.lower() == "blue":
            backVar = Back.LIGHTBLUE_EX
        if BackA.lower() == "green":
            backVar = Back.LIGHTGREEN_EX
        if BackA.lower() == "yellow":
            backVar = Back.LIGHTYELLOW_EX
        if BackA.lower() == "white":
            backVar = Back.LIGHTWHITE_EX
        if BackA.lower() == "cyan":
            backVar = Back.LIGHTCYAN_EX
        if BackA.lower() == "black":
            backVar = Back.LIGHTBLACK_EX
        if BackA.lower() == "magenta":
            backVar = Back.LIGHTMAGENTA_EX
    else:
        if BackA.lower() == "none":
            backVar = Back.RESET
        if BackA.lower() == "red":
            backVar = Back.RED
        if BackA.lower() == "blue":
            backVar = Back.BLUE
        if BackA.lower() == "green":
            backVar = Back.GREEN
        if BackA.lower() == "yellow":
            backVar = Back.YELLOW
        if BackA.lower() == "white":
            backVar = Back.WHITE
        if BackA.lower() == "cyan":
            backVar = Back.CYAN
        if BackA.lower() == "black":
            backVar = Back.BLACK
        if BackA.lower() == "magenta":
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
        x = input(backVar + StyVar + foreVar + f"{Text}  \n")
    else:
        x = input(backVar + foreVar + f"{Text}  \n")