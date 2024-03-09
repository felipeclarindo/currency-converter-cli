from time import sleep
from conversor.definicoes_conversor import Conversor
from os import system
from platform import system as sys

# Autor
def byFelipe()->None:
    print("""
--------------------------
|                        |
|  Conversor de Moedas   |
|   by \033[1;31mFelipe Clarindo   \033[0m|
|                        |
--------------------------
""")

"""
Limpa a tela do console.

Esta função identifica o sistema operacional em que está sendo executada e utiliza o comando
apropriado para limpar a tela do console. Suporta sistemas operacionais Linux, macOS (Darwin) e Windows.

Returns:
    None

Raises:
    None
"""
def clear(booleano: bool) -> None:

    if booleano:
        # Indentificando o sistema operacional
        plataform = sys()
        if plataform in ["Linux","Darwin"]:
            system("clear")

        elif plataform == "Windows":
            system("cls")

        else:
            print("Sistema Operacional não identificado")

    else:

        input("Aperte \033[1;31mENTER\033[0m para continuar...")

        # Indentificando o sistema operacional
        plataform = sys()
        if plataform in ["Linux", "Darwin"]:
            system("clear")

        elif plataform == "Windows":
            system("cls")

        else:
            print("Sistema Operacional não identificado")

class Main:

    def __init__(self):

        self.conversor = Conversor(moeda1= None, moeda2 = None, valor = None) # Instância do objeto
        self.moedas = {"Euro": "€","Dolar":"USD","Libra":"£","Real":"BRL"} # Moedas para conversão

    def layout_menu(self) -> None:

        print('-' * 40)
        print("--------- CONVERSOR DE MOEDA -----------")
        print('-' * 40)

    def conversor_de_moedas(self):

        # Lógica do Conversor de moedas
        while True:

            # Limpa a tela do console.
            clear(True)

            # Chama o layout de apresentação do menu
            self.layout_menu()

            """
            Bloco de tratamento de exceções para a conversão de moedas.

            Este bloco de código tenta realizar a conversão de moedas, onde o usuário é solicitado a selecionar as moedas de origem e destino,
            bem como inserir o valor a ser convertido. Antes de proceder com a conversão, verifica-se se os valores inseridos são válidos.

            Exemplo de uso:
                Ao executar este bloco de código, o usuário é guiado através de diferentes etapas para inserir as informações necessárias para a conversão.
                Se uma exceção do tipo ValueError ocorrer durante a conversão, uma mensagem indicando que o valor inserido é inválido será exibida.

                Exemplo:
                >>> Digite de acordo com o índice!
                >>> [1] EURO
                >>> [2] DOLAR
                >>> [3] LIBRA
                >>> [4] REAL

                Converter de: 1
                Para: 2
                Digite o valor a ser convertido: 100
                Convertendo....
                (pausa por 1 segundo)

            Raises:
                ValueError: Se um valor inválido for inserido durante a seleção das moedas ou na entrada do valor a ser convertido.

            Returns:
                None
            """
            try:

                """
                Exibe as opções de moeda para o usuário.

                Este trecho de código imprime na tela as opções de moeda disponíveis para o usuário selecionar. Cada opção é identificada por
                um número entre colchetes e seu respectivo nome.

                Exemplo de uso:
                    Ao executar este trecho de código, as opções de moeda serão exibidas na tela para que o usuário possa fazer sua seleção.

                    Exemplo:
                    >>> Digite de acordo com o índice!
                    >>> [1] EURO
                    >>> [2] DOLAR
                    >>> [3] LIBRA
                    >>> [4] REAL
                """
                print(f"""
                Digite de acordo com o indice!
                [1] EURO
                [2] DOLAR
                [3] LIBRA
                [4] REAL \n""")

                """
                Solicita as moedas de conversão ao usuário.

                Este trecho de código solicita ao usuário que insira os códigos das moedas de origem e destino para a conversão.
                Os valores inseridos são convertidos para o tipo de dados inteiro antes de serem armazenados nas variáveis 'moeda1'
                e 'moeda2' do objeto 'conversor'.

                Exemplo de uso:
                    Ao executar este trecho de código, o usuário será solicitado a inserir os códigos das moedas de origem e destino para a conversão.

                    Exemplo:
                    >>> Converter de: 1
                    >>> Para: 2
                """
                self.conversor.moeda1 = int(input("Converter de: "))
                self.conversor.moeda2 = int(input("Para: "))

                # Realiza o tratamento de exceção para os índices de moeda antes de continuar
                self.conversor.tratamento_excessao()

                """
                Solicita um valor a ser convertido.

                Este script solicita ao usuário que insira um valor a ser convertido. O valor inserido é convertido
                para o tipo de dados float antes de ser armazenado em uma variável chamada 'valor'.

                Exemplo de uso:
                    Ao executar este script, o usuário será solicitado a inserir um valor numérico para conversão.

                    Exemplo:
                    >>> Digite o valor a ser convertido: 100
                """
                self.conversor.valor = float(input("Digite o valor a ser convertido: "))

                # Limpa a tela do console.
                clear(True)

                """
                Exibe uma mensagem de conversão e pausa a execução por um segundo.

                Este trecho de código imprime uma mensagem formatada em verde indicando uma operação de conversão
                em andamento e pausa a execução por um segundo, para dar tempo ao usuário de perceber a mensagem.

                Exemplo de uso:
                    Este trecho de código é frequentemente utilizado em programas que realizam operações de conversão
                     ou processamento que exigem um breve intervalo de tempo para completar.

                    Exemplo:
                    >>> Convertendo....
                    (pausa por 1 segundo)
                """
                print("\033[32mConvertendo....\033[0m")
                sleep(1)

                # Limpa a tela do console.
                clear(True)

                """
                Cria uma lista a partir dos elementos contidos em self.moedas.

                Esta linha de código cria uma nova lista contendo os mesmos elementos que estão contidos no objeto self.moedas,
                que pode ser uma estrutura iterável, como uma lista, tupla, conjunto, etc.

                Parameters:
                    self (objeto): A instância atual da classe que contém o método.
                    self.moedas (iterável): Uma coleção de elementos que serão usados para criar a nova lista.

                Returns:
                    Uma nova lista contendo os elementos de self.moedas.

                Exemplo de uso:
                    Supondo que self.moedas = ['Euro', 'Dólar', 'Libra', 'Real'], ao executar a linha de código, a lista resultante seria:
                    >>> lista
                    ['Euro', 'Dólar', 'Libra', 'Real']

                    Esse trecho de código pressupõe que self.moedas é um atributo ou propriedade definido anteriormente no contexto do objeto.
                """
                lista = list(self.moedas)

                """
                Realiza uma conversão de moeda utilizando os índices de moeda especificados.

                Esta linha de código chama a função de conversão do objeto 'conversor' com as moedas de origem e destino obtidas a partir
                 dos índices especificados pelo conversor.

                Parameters:
                    self (objeto): A instância atual da classe que contém o método.
                    self.conversor (objeto): O objeto que contém o método de conversão.
                    self.moedas (iterável): Uma coleção de moedas disponíveis.
                    self.conversor.moeda1 (int): O índice da moeda de origem.
                    self.conversor.moeda2 (int): O índice da moeda de destino.
                    lista (list): A lista de moedas disponíveis, previamente criada.

                Returns:
                    O resultado da conversão de moeda.

                Exemplo de uso:
                    Supondo que self.moedas = ['Euro', 'Dólar', 'Libra', 'Real'], self.conversor.moeda1 = 1 e self.conversor.moeda2 = 2,
                    e 'lista' é uma lista criada anteriormente contendo os elementos de self.moedas, a linha de código seria equivalente a:

                    >>> self.conversor.conversao('Euro', 'Dólar')
                    Isso realiza a conversão de Euro para Dólar, assumindo que a função conversao está implementada corretamente.

                    Esse trecho de código pressupõe que self.moedas e self.conversor são atributos ou propriedades definidos anteriormente no contexto do objeto.
                """
                self.conversor.conversao(self.moedas[lista[(self.conversor.moeda1-1)]],self.moedas[lista[(self.conversor.moeda2-1)]])


                # Limpa a tela do console.
                clear(False)

                """
                Solicita confirmação para continuar e executa ações com base na resposta.

                Este trecho de código solicita ao usuário que insira uma resposta para continuar ('S' para Sim e 'N' para Não).
                Se o usuário digitar 'N', a função byFelipe() é chamada e uma mensagem "Finalizado!" é exibida. Em seguida, o loop é interrompido.

                Parameters:
                    None

                Returns:
                    None

                Exemplo de uso:
                    Ao executar este trecho de código, o usuário será solicitado a inserir 'S' para continuar ou 'N' para interromper o processo.
                    Se 'N' for inserido, a função byFelipe() será chamada e a execução será interrompida.

                    Exemplo:
                    >>> Deseja continuar? Digite "S" para Sim e "N" para Não
                    [usuário digita 'N']
                    Finalizado!
                """
                cont = str(input(
                    'Deseja continuar? Digite \033[1;32m"S"\033[0m para \033[1;32mSim\033[0m e \033[1;31m"N"\033[0m para \033[1;31mNão\033[0m! \n')).strip().lower()
                if "n" in cont:
                    byFelipe()
                    print("Finalizado!")
                    break

            except ValueError:
                print("O Valor inserido é ínvalido!")

if __name__ == '__main__':
    execultar = Main()
    execultar.conversor_de_moedas()