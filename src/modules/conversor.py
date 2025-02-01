import requests

class Conversor:

    def __init__(self, moeda_origem, moeda_destino, valor):
        self.moeda_origem = moeda_origem  # Moeda de origem
        self.moeda_destino = moeda_destino  # Moeda de destino
        self.valor = valor  # Valor a ser convertido

    def obter_taxa_conversao(self):
        """
        Obtém a taxa de conversão da moeda de origem para a moeda de destino a partir de uma API.

        Retorna:
            float: A taxa de conversão entre as duas moedas.

        Levanta:
            Exception: Se a requisição à API falhar ou se a moeda não for encontrada.
        """
        try:
            # API de câmbio para obter a taxa de conversão
            url = f"https://api.exchangerate-api.com/v4/latest/{self.moeda_origem}"
            response = requests.get(url)
            data = response.json()
            if self.moeda_destino not in data['rates']:
                raise Exception("Conversão não identificada.")

            return data['rates'][self.moeda_destino]
        except Exception as e:
            raise Exception(f"Erro ao obter a taxa de conversão: {str(e)}")

    def conversao(self, sigla1: str, sigla2: str):
        """
        Realiza a conversão de moedas utilizando a taxa obtida da API.

        Parâmetros:
        - sigla1 (str): Sigla da moeda de origem.
        - sigla2 (str): Sigla da moeda de destino.

        Retorna:
        - None
        """
        if self.moeda_origem == self.moeda_destino:
            raise Exception(f"Não é possível converter de {sigla1} para {sigla2}.")

        try:
            taxa = self.obter_taxa_conversao()
            print(f"A Conversão de {self.valor:.2f} {sigla1} para {sigla2} é: {round(self.valor * taxa, 2):.2f} {sigla2} \nCuja taxa é: {taxa:.2f} {sigla2}/{sigla1} \n")
        except Exception as e:
            print(str(e))
