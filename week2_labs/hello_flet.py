import flet as ft

def main(page: ft.Page):
    page.title = "Hello Flet Desktop"
    page.window_width = 400
    page.window_height = 300
    page.add(ft.Text("Hello, Flet Desktop is working!"))

# Force desktop app
ft.app(target=main, view=ft.WEB_BROWSER)  # change to ft.WINDOW for native window

