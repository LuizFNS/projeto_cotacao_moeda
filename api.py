import os
import requests
import xml.etree.ElementTree as ET

class AwesomeApi:
    def __init__(self, base_url="https://economia.awesomeapi.com.br/", api_token="2247d6f0da628db9d391510927ad71714f01565490b82e56c9a3f646143c86cb"):
        self.BASE_URL = base_url
        self.API_TOKEN = api_token or os.getenv("AWESOME_API_TOKEN")

    def cotacao_atual(self, de='BRL', para='USD', valor=1):
        try:
            consulta = f"{para}-{de}"
            url = f"{self.BASE_URL}json/last/{consulta}"
            resp = requests.get(url, params={"token": self.API_TOKEN})
            resp.raise_for_status()
            data = resp.json()
            chave = para + de
            cotacao = float(data[chave]["bid"]) * float(valor)
            return f"{para}: {round(cotacao, 3)}"
        except Exception as e:
            return f"Erro na consulta: {e}"

    def fechamento_diario(self, moeda="USD-BRL", start="20180901", end="20180930"):
        url = f"{self.BASE_URL}json/daily/{moeda}/"
        resp = requests.get(url, params={"start_date": start, "end_date": end})
        return resp.json()

    def moedas_disponiveis(self):
        url = f"{self.BASE_URL}/xml/available/uniq"
        resp = requests.get(url, params={"token": self.API_TOKEN})
        resp.encoding = "utf-8"
        root = ET.fromstring(resp.text)
        moedas_dict = {}
        for moedas in root:
            codigo = moedas.tag
            nome = moedas.text
            moedas_dict[codigo] = nome
        return moedas_dict

if __name__ == "__main__":
    api = AwesomeApi(api_token="sua_token_aqui")
    print(api.cotacao_atual())
