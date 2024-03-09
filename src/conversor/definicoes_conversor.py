class Conversor:

    def __init__(self, moeda1, moeda2, valor):

        self.moeda1 = moeda1 # Moeda de origem
        self.moeda2 = moeda2 # Moeda de destino
        self.valor = valor # Valor á ser convertido

        # Dicionário de taxas de conversão entre diferentes moedas
        self.__taxa_conversao = {
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

    def tratamento_excessao(self):
        """
        Realiza tratamento de exceção para os índices de moeda.

        Este método verifica se os índices de moeda estão dentro dos limites permitidos (de 1 a 4).
        Se um índice estiver fora desse intervalo, uma exceção do tipo ValueError é levantada com uma mensagem indicando o problema.

        Raises:
            ValueError: Se algum dos índices de moeda for menor que 1 ou maior que 4.

        Returns:
            None
        """
        if (self.moeda1 - 1) > 3 or (self.moeda1 - 1) < 0 or (self.moeda2 - 1) > 3 or (self.moeda2 - 1) < 0:

            raise ValueError("Indice invalido, Escolha um número de 1 a 4")

    """
    Realiza a conversão de moedas com base nas taxas de conversão fornecidas.

    Parâmetros:
    - sigla1 (str): Sigla da moeda de origem.
    - sigla2 (str): Sigla da moeda de destino.

    Retorna:
    - None

    Esta função verifica se a conversão entre as moedas de origem e destino é possível
    com base nas taxas de conversão fornecidas. Se a conversão for possível, ela calcula
    o valor convertido com base na taxa de conversão e exibe na tela. Caso contrário, exibe
    uma mensagem informando que a conversão não é possível.

    Exemplos de uso:
    >>> conversor = Conversor(moeda1=1, moeda2=2, valor=100)
    >>> conversor.conversao("USD", "EUR")
    A Conversão de USD para EUR é: 108.0 
    Cuja taxa é: 1.08

    >>> conversor.conversao("EUR", "USD")
    A Conversão de EUR para USD é: 92.0 
    Cuja taxa é: 0.92

    >>> conversor.conversao("EUR", "GBP")
    Conversão não identificada.
    """
    def conversao(self, sigla1: str, sigla2: str):

        if self.moeda1 == self.moeda2:
            print(f"Essa moeda convertida resulta no mesmo valor: {self.valor}")
        elif (self.moeda1, self.moeda2) in self.__taxa_conversao:
            taxa = self.__taxa_conversao[(self.moeda1, self.moeda2)]
            print(f"A Conversão de {sigla1} para {sigla2} é: {round(self.valor * taxa,2)} \nCujo taxa é: {taxa}\n")
        else:
            print("Conversão não identificada.")