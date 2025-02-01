from platform import system as sys
from os import system


def clear_terminal():

    plataform = sys()
    if plataform in ["Linux", "Darwin"]:
        system("clear")
    elif plataform == "Windows":
        system("cls")
    else:
        print("Sistema Operacional não identificado")
