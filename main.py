import flet as ft
from gui_conversao import main_ui
from api import FreeCurrencyApi

fca = FreeCurrencyApi()

if __name__ == "__main__":
    ft.app(target=main_ui)
#    print(fca.cotacao_atual())
