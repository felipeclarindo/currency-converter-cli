from time import sleep
from .modules.conversor import Conversor
from .utils.utils import clear_terminal


class App:
    def __init__(self) -> None:
        """
        Inicializa a classe App, criando uma instância do objeto Conversor e definindo as moedas disponíveis para conversão.

        Returns:
            None
        """
        self.conversor = Conversor(moeda_origem=None, moeda_destino=None, valor=None)  # Instância do objeto
        self.moedas = {
            "Euro": "EUR",  # Código da moeda
            "Dólar": "USD",
            "Libra": "GBP",
            "Real": "BRL"
        }  # Moedas para conversão

    def byFelipe(self) -> None:
        """
        Exibe a assinatura do autor no console.

        Returns:
            None
        """
        self.clear()
        print("""\
--------------------------
|                        |
|  Conversor de Moedas   |
|   by \033[1;31mFelipe Clarindo   \033[0m|
|                        |
--------------------------\
""")

    def clear(self, want_input: bool) -> None:
        """
        Limpa a tela do console.

        Esta função identifica o sistema operacional em que está sendo executada e utiliza o comando
        apropriado para limpar a tela do console. Suporta sistemas operacionais Linux, macOS (Darwin) e Windows.

        Args:
            want_input (bool): Define se a função deve limpar a tela diretamente ou aguardar o usuário pressionar ENTER.

        Returns:
            None
        """
        if want_input:
            input("Aperte \033[1;31mENTER\033[0m para continuar...")
            clear_terminal()
        else:
            clear_terminal()

    def layout_menu(self) -> None:
        """
        Exibe o layout do menu no console.

        Returns:
            None
        """
        print('-' * 40)
        print("--------- CONVERSOR DE MOEDA -----------")
        print('-' * 40)

    def run(self) -> None:
        """
        Executa a lógica principal do conversor de moedas. Solicita a seleção das moedas e o valor para conversão,
        realiza a conversão e exibe o resultado.

        Returns:
            None
        """
        while True:
            self.clear(False)
            self.layout_menu()

            try:
                print("""\
Digite de acordo com o índice!
[1] EURO
[2] DOLAR
[3] LIBRA
[4] REAL \n""")

                # Mapeia as entradas do usuário para os códigos das moedas
                escolha_origem = int(input("Converter de: "))
                escolha_destino = int(input("Para: "))
                
                # Mapeia as escolhas numéricas para os códigos das moedas
                lista_moedas = list(self.moedas.values())
                self.conversor.moeda_origem = lista_moedas[escolha_origem - 1]  # Código da moeda de origem
                self.conversor.moeda_destino = lista_moedas[escolha_destino - 1]  # Código da moeda de destino

                self.conversor.valor = float(input("Digite o valor a ser convertido: "))

                self.clear(False)
                print("\033[32mConvertendo....\033[0m")
                sleep(1)

                self.clear(False)
                self.conversor.conversao(self.conversor.moeda_origem, self.conversor.moeda_destino)

                self.clear(True)
                cont = str(input('Deseja continuar? \nDigite \033[1;32mSim\033[0m ou \033[1;31mNão\033[0m! \n')).strip().lower()
                if cont in ["n", "não", "nn", "nao"]:
                    self.byFelipe()
                    print("Finalizado!")
                    break
                self.clear(False)
                print("\033[32mReiniciando....\033[0m")
                sleep(1)

            except ValueError:
                print(f"ValueError: O valor inserido é inválido!")
                self.clear(True)
            except Exception as e:
                print(f"Erro: {e}")
                self.clear(True)
