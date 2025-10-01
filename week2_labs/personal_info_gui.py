
import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Personal Information Manager"
    page.window.width = 600
    page.window.height = 700
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    title = ft.Text(
        "Personal Information Manager",
        size=28,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.INDIGO_700
    )

    # Input fields
    first_name = ft.TextField(label="First Name", width=280)
    last_name = ft.TextField(label="Last Name", width=280)
    age = ft.TextField(label="Age", width=100, keyboard_type=ft.KeyboardType.NUMBER)
    student_id = ft.TextField(label="Student ID", width=200)

    program_dropdown = ft.Dropdown(
        label="Academic Program",
        width=300,
        options=[
            ft.dropdown.Option("BSCS"),
            ft.dropdown.Option("BSIT"),
            ft.dropdown.Option("BSCpE"),
            ft.dropdown.Option("BSIS"),
        ]
    )

    year_level = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="1st", label="1st Year"),
            ft.Radio(value="2nd", label="2nd Year"),
            ft.Radio(value="3rd", label="3rd Year"),
            ft.Radio(value="4th", label="4th Year"),
        ])
    )

    favorite_color = ft.Dropdown(
        label="Favorite Color",
        width=200,
        options=[
            ft.dropdown.Option("Red"), ft.dropdown.Option("Blue"),
            ft.dropdown.Option("Green"), ft.dropdown.Option("Yellow"),
            ft.dropdown.Option("Purple"), ft.dropdown.Option("Orange"),
            ft.dropdown.Option("Pink"), ft.dropdown.Option("Black"),
            ft.dropdown.Option("White"), ft.dropdown.Option("Gray"),
        ]
    )

    hobbies = ft.TextField(label="Hobbies/Interests", width=400, multiline=True)

    # Output container with dark background
    output_container = ft.Container(
        content=ft.Text(
            "Fill out the form and click 'Generate Profile'.",
            color=ft.Colors.WHITE
        ),
        bgcolor=ft.Colors.INDIGO_900,
        padding=15,
        border_radius=10,
        width=550
    )

    # Functions
    def generate_profile(e):
        if not all([first_name.value, last_name.value, age.value]):
            output_container.content = ft.Text(
                "Please fill in all required fields (Name and Age)!",
                color=ft.Colors.WHITE
            )
            page.update()
            return

        current_year = datetime.now().year
        birth_year = current_year - int(age.value)
        graduation_year = current_year + (4 - int(year_level.value[0]) if year_level.value else 4)

        profile_content = ft.Column([
            ft.Text(f"Full Name: {first_name.value} {last_name.value}", size=16, color=ft.Colors.WHITE),
            ft.Text(f"Student ID: {student_id.value or 'Not provided'}", size=16, color=ft.Colors.WHITE),
            ft.Text(f"Age: {age.value} years old", size=16, color=ft.Colors.WHITE),
            ft.Text(f"Birth Year: {birth_year}", size=16, color=ft.Colors.WHITE),
            ft.Text(f"Program: {program_dropdown.value or 'Not selected'}", size=16, color=ft.Colors.WHITE),
            ft.Text(f"Year Level: {year_level.value or 'Not selected'}", size=16, color=ft.Colors.WHITE),
            ft.Text(f"Favorite Color: {favorite_color.value or 'Not selected'}", size=16, color=ft.Colors.WHITE),
            ft.Text(f"Hobbies: {hobbies.value or 'Not provided'}", size=16, color=ft.Colors.WHITE),
            ft.Text(f"Expected Graduation: {graduation_year}", size=16, color=ft.Colors.WHITE),
            ft.Text(f"Profile generated on: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}", size=12, color=ft.Colors.WHITE),
        ])
        output_container.content = profile_content
        page.update()

    def clear_form(e):
        first_name.value = ""
        last_name.value = ""
        age.value = ""
        student_id.value = ""
        program_dropdown.value = None
        year_level.value = None
        favorite_color.value = None
        hobbies.value = ""
        output_container.content = ft.Text(
            "Form cleared. Fill out the information again.",
            color=ft.Colors.WHITE
        )
        page.update()

    generate_btn = ft.ElevatedButton("Generate Profile", on_click=generate_profile, width=150)
    clear_btn = ft.ElevatedButton("Clear Form", on_click=clear_form, width=150)

    page.add(
        ft.Column([
            title,
            ft.Divider(),
            ft.Row([first_name, last_name], spacing=20),
            ft.Row([age, student_id], spacing=20),
            program_dropdown,
            ft.Text("Year Level:"),
            year_level,
            favorite_color,
            hobbies,
            ft.Row([generate_btn, clear_btn], spacing=20),
            ft.Divider(),
            ft.Text("Generated Profile:"),
            output_container,
        ], spacing=10)
    )

if __name__ == "__main__":
    ft.app(target=main)
