from os import system
from platform import system as sys
from time import sleep

moedas = {
    "Euro": "€",
    "Dolar":"USD",
    "Libra":"£",
    "Real":"BRL",
}

def converterMoeda(sigla1, sigla2, moeda1, moeda2, valor):
    taxa_conversao = {
        (1, 2): 1.08,  # Euro para Dólar
        (1, 3): 0.86,  # Euro para Libra
        (1, 4): 5.34,  # Euro para Real
        (2, 1): 0.92,  # Dólar para Euro
        (2, 3): 0.79,  # Dólar para Libra
        (2, 4): 4.94,  # Dólar para Real
        (3, 1): 1.17,  # Libra para Euro
        (3, 2): 1.26,  # Libra para Dólar
        (3, 4): 6.24,  # Libra para Real
        (4, 1): 0.19,  # Real para Euro
        (4, 2): 0.20,  # Real para Dólar
        (4, 3): 0.16   # Real para Libra
    }

    if moeda1 == moeda2:
        print(f"Essa moeda convertida resultada no mesmo valor: {valor}")
    elif (moeda1, moeda2) in taxa_conversao:
        taxa = taxa_conversao[(moeda1, moeda2)]
        print(f"A Conversão da {sigla1} para {sigla2} é: {taxa}")
    else:
        print("Conversão não identificada.")




def clear() -> None:        
    plataform = sys()
    if plataform in ["Linux","Darwin"]:
        system("clear")
    elif plataform == "Windows":
        system("cls")
    else:    
        print("Sistema Operacional não identificado")

def showMenu()-> None: 
    clear()

    print('-'*40)
    print("--------- CONVERTOR DE MOEDA -----------")
    print('-'*40)


def iniciarConversao()-> None:
    while True:
        try:
                

            print("""
Digite de acordo com o indice!
[1] EURO
[2] DOLAR
[3] LIBRA
[4] REAL""")

            moeda1 = int(input("Converter de: "))-1
            moeda2 = int(input("Para: "))-1 

            if moeda1 > 3 or moeda1 < 0 or moeda2 > 3 or moeda2 < 0:
                raise ValueError("Indice invalido, Escolha um número de 1 a 4")

            showMenu()

            valor = float(input("Digite o valor a ser convertido: "))

            print("\033[32mConvertendo....\033[0m")
            sleep(1)

            showMenu()

            lista = list(moedas)

            converterMoeda(moedas[lista[moeda1]], moedas[lista[moeda2]], moeda1, moeda2, valor)

            input("Aperte \033[1;31mENTER\033[0m para continuar...")
            
            showMenu()
            
            cont = str(input('Deseja continuar? Digite \033[1;32m"S"\033[0m para \033[1;32mSim\033[0m e \033[1;31m"N"\033[0m para \033[1;31mNão\033[0m \n')).strip().lower()
            if "n" in cont:
                print("Finalizado!")
                break
                
        except ValueError:
            print("O Valor inserido é ínvalido!")

def byFelipe()->None:
    print("""
--------------------------
|                        |
|  Conversor de Moedas   |
|   by \033[1;31mFelipe Clarindo   \033[0m|
|                        |
--------------------------
""")
    