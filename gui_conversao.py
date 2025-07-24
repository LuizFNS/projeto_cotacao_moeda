import flet as ft
from api import AwesomeApi

awesome_api = AwesomeApi()
moedas = awesome_api.moedas_disponiveis()

def main(page: ft.Page):
    page.title = "App de Cotação"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 30
    page.scroll = "auto"

    titulo = ft.Text("💱 Cotação de Moedas", size=24, weight="bold")

    campo_converter_de_moeda = ft.Dropdown(
        label="Converter de:",
        options=[
            ft.dropdown.Option(key=k, text=f"{k} → {v}") for k, v in moedas.items()
        ],
        value="BRL",
        width=250,
    )

    campo_converter_para_moeda = ft.Dropdown(
        label="Para:",
        options=[
            ft.dropdown.Option(key=k, text=f"{k} → {v}") for k, v in moedas.items()
        ],
        value="USD",
        width=250,
    )

    valor = ft.TextField(
        label="Valor de conversão",
        value="1",
        width=100,
        keyboard_type=ft.KeyboardType.NUMBER
    )

    resultado = ft.Text(
        value="0",
        width=250,
        size=16,
        weight="bold",
        color="#FFFFFF"
    )

    def buscar_click(e):
        de = campo_converter_de_moeda.value
        para = campo_converter_para_moeda.value
        try:
            valor_num = float(valor.value)
            resultado.value = "🔄 Consultando..."
            page.update()

            cotacao = awesome_api.cotacao_atual(de, para, valor_num)

            if isinstance(cotacao, str) and "Erro" in cotacao:
                resultado.value = "❌ Erro ao consultar"
                resultado.color = "#F44336"
            else:
                resultado.value = f"💲 {cotacao}"
                resultado.color = "#FFFFFF"

        except ValueError:
            resultado.value = "❗ Valor inválido"
            resultado.color = "#F44336"

        page.update()

    botao = ft.ElevatedButton("Buscar", on_click=buscar_click)

    page.add(
        ft.Column([
            titulo,
            ft.Row(
                controls=[
                    campo_converter_de_moeda,
                    campo_converter_para_moeda
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[valor, resultado],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[botao],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=25)
    )

if __name__ == "__main__":
    ft.app(target=main)
