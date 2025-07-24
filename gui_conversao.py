import flet as ft
from api import FreeCurrencyApi, moedas_disponiveis

fca = FreeCurrencyApi()
moedas = moedas_disponiveis()


def main(page: ft.Page):
    page.title = "App de Cotação"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    titulo = ft.Text("Cotação de Moedas", size=24, weight="bold")
    # campo_moeda = ft.TextField(label="Moeda (ex: USD-BRL)", width=200)
    campo_converter_de_moeda = ft.Dropdown(
        label="Selecione uma moeda",
        options=[
            ft.dropdown.Option(key=f"{k}", text=f"{k} → {v}") for k, v in moedas.items()
        ],
        value="BRL",
        width=200,
    )
    campo_converter_para_moeda = ft.Dropdown(
        label="Selecione uma moeda",
        options=[
            ft.dropdown.Option(key=f"{k}", text=f"{k} → {v}") for k, v in moedas.items()
        ],
        value="USD",
        width=200,
    )
    resultado = ft.Text("")

    def buscar_click(e):
        converter_de_moeda = campo_converter_de_moeda.value
        converter_para_moeda = campo_converter_para_moeda.value
        resultado.value = (
            f"Buscando cotação de: {converter_de_moeda} para {converter_para_moeda} "
        )
        page.update()
        cotacao = fca.cotacao_atual(converter_de_moeda, converter_para_moeda)
        print(converter_para_moeda)
        for k, v in cotacao.get("data").items():
            cotacao_valor = v
        resultado.value = f"{k}: {round(cotacao_valor,3)}"
        page.update()

    botao = ft.ElevatedButton("Buscar", on_click=buscar_click)

    page.add(
        titulo, campo_converter_de_moeda, campo_converter_para_moeda, botao, resultado
    )


ft.app(target=main)  # Executa como app de desktop
# ft.app(target=main, view=ft.WEB_BROWSER)  # Ou para rodar no navegador
