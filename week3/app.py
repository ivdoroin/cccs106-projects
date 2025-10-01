import flet as ft

def main(page: ft.Page):
    page.title = "Hello Flet!"
    page.add(ft.Text("Hello, world!"))

ft.app(target=main)
