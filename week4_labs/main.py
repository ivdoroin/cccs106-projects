import flet as ft
from database import init_db
from app_logic import display_contacts, add_contact

def main(page: ft.Page):
    page.title = "Contact Book"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_width = 400
    page.window_height = 650

    db_conn = init_db()

    name_input = ft.TextField(label="Name", width=350)
    phone_input = ft.TextField(label="Phone", width=350)
    email_input = ft.TextField(label="Email", width=350)
    inputs = (name_input, phone_input, email_input)

    contacts_list_view = ft.ListView(expand=1, spacing=10, auto_scroll=True)

    add_button = ft.ElevatedButton(
        text="Add Contact",
        on_click=lambda e: add_contact(page, inputs, contacts_list_view, db_conn)
    )

    search_input = ft.TextField(
        label="Search",
        width=350,
        on_change=lambda e: display_contacts(page, contacts_list_view, db_conn, search_input.value)
    )

    dark_mode_switch = ft.Switch(
        label="Dark Mode",
        value=False,
        on_change=lambda e: toggle_theme(page, dark_mode_switch.value)
    )

    page.add(
        ft.Column(
            [
                ft.Text("Enter Contact Details:", size=20, weight=ft.FontWeight.BOLD),
                name_input, phone_input, email_input, add_button,
                ft.Divider(),
                ft.Row([ft.Text("Contacts:", size=20, weight=ft.FontWeight.BOLD), dark_mode_switch]),
                search_input,
                contacts_list_view,
            ],
            scroll=ft.ScrollMode.AUTO
        )
    )

    display_contacts(page, contacts_list_view, db_conn)

def toggle_theme(page, dark_mode):
    """Switch between light and dark mode."""
    page.theme_mode = ft.ThemeMode.DARK if dark_mode else ft.ThemeMode.LIGHT
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
