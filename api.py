import requests
import xml.etree.cElementTree as ET


class FreeCurrencyApi:
    def __init__(
        self,
        BASE_URL="https://api.freecurrencyapi.com/v1/",
        API_TOKEN="fca_live_KA0N6plXyk6BIPPJYp1J6w2aOORZQyJTDYfncuUW",
    ):
        self.BASE_URL = BASE_URL
        self.API_TOKEN = API_TOKEN

    def cotacao_atual(self, moeda_cotacao="EUR", moeda_base="USD"):
        endpoint_latest = "latest"
        self.moeda_base = moeda_base
        self.moeda_cotacao = moeda_cotacao
        params = {
            "currencies": moeda_cotacao,
            "base_currency": moeda_base,
        }
        headers = {
            "apikey": self.API_TOKEN,
        }
        # https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_KA0N6plXyk6BIPPJYp1J6w2aOORZQyJTDYfncuUW&currencies=EUR
        url = f"{self.BASE_URL}{endpoint_latest}"
        resp = requests.get(url, params=params, headers=headers)
        return resp.json()


class BancoCentral:
    def __init__(
        self,
        BASE_URL="https://www3.bcb.gov.br/",
        endpoint_moedas="bc_moeda/rest/moeda/data",
    ) -> None:
        self.BASE_URL = BASE_URL
        self.endpoint_moedas = endpoint_moedas

    def moedas_disponiveis_bc(self):
        self.url = self.BASE_URL + self.endpoint_moedas
        self.resp = requests.get(self.url)
        self.root = ET.fromstring(self.resp.text)
        self.moedas = []

        for moeda in self.root.findall("moeda"):
            dados = {}
            for item in moeda:
                dados[item.tag] = item.text.strip() if item.text else None
            self.moedas.append(dados)
        return self.moedas


BASE_URL = "https://economia.awesomeapi.com.br/"
API_TOKEN = "2247d6f0da628db9d391510927ad71714f01565490b82e56c9a3f646143c86cb"


def conversao():
    consulta = "USD-BRL"
    url_consulta = BASE_URL + "json/last/" + consulta
    response = requests.get(url_consulta, params={"token": API_TOKEN})
    data = response.json()
    return data


def fechamento_diario():
    endpoint = "json/daily/"
    # consulta_moedas = ["USD-BRL", "BRL-USD"]
    moeda = "USD-BRL"
    numero_dias = {"start_date": "20180901", "end_date": "20180930"}
    url = f"{BASE_URL}{endpoint}{moeda}/"
    print(url)
    resp = requests.get(url, params=numero_dias)
    data = resp.json()
    return data


def moedas_disponiveis():
    url = "https://economia.awesomeapi.com.br/xml/available/uniq"
    resp = requests.get(url, params={"token": API_TOKEN})
    resp.encoding = "utf-8"
    root = ET.fromstring(resp.text)
    moedas_dict = {}
    for moedas in root:
        codigo = moedas.tag
        nome = moedas.text
        moedas_dict[codigo] = nome
    return moedas_dict


if __name__ == "__main__":
    fca = FreeCurrencyApi()
    bcc = BancoCentral()
    print(bcc.moedas_disponiveis_bc())
    # print(fca.cotacao_atual())
    # print(fechamento_diario())
    # moedas = moedas_disponiveis()
    # for k, v in moedas.items():
    #    print(k, v)
    # print(conversao())
    pass
