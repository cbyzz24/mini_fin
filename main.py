import flet as ft


def main(page: ft.Page):
    page.window_height=600
    page.window_width=800
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    mortgage_amount = ft.TextField(label="Amount", text_size=14, content_padding=2, text_align="right", height=28, width=100,)

    bill_container = ft.Container(
        height=540,
        width=800,
        padding=10,
        bgcolor=ft.colors.BLUE_400,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text("Mortgage", size=14, height=20, width=100,),
                ft.Text("1st", size=14, height=20, width=30,),
                mortgage_amount,
            ]

        )
    )


    page.add(bill_container)
    


ft.app(main)
