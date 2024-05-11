import flet as ft
from pdf import draw_pdf, get_image_of_pdf
import os

def main(page: ft.Page):
    def close_dlg(e):
        dlg_modal.open = False
        page.update()
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Column([
            ft.Row([ft.Text("Ваш сформированный ценник!")], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ft.Image("./out.png", width=200, height=200)], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ft.Text("Вы можете найти его в директории проекта в формате pdf или png!")], alignment=ft.MainAxisAlignment.CENTER),

            
        ]),
        actions=[
            
            ft.Row([ft.TextButton("OK", on_click=close_dlg)], alignment=ft.MainAxisAlignment.CENTER),

            
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )
    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    def btn_click(e):
        if not txt_name.value or not txt_price.value:
            txt_name.error_text = "Пожалуйста, заполните все поля"
            txt_price.error_text = "Пожалуйста, заполните все поля"
            page.update()
        else:
            draw_pdf(txt_name.value, txt_price.value)
            # get current file path
            dir = os.path.abspath(os.curdir)
            print(dir)
            get_image_of_pdf(dir + 'out.pdf')
            open_dlg_modal(e)            
    page.title = "Пример формирования ценников"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    txt_name = ft.TextField(hint_text="Название товара", width=300, max_length=10)
        
    def is_price_numeric(e):
        if not e.control.value.isdigit():
          e.control.value = ""
          page.update()
    txt_price = ft.TextField(hint_text="Цена товара", width=300, max_length=3, keyboard_type=ft.KeyboardType.NUMBER, on_change=is_price_numeric)
    # txt_price.on_change = 

    btn = ft.ElevatedButton("Сформировать PDF!", on_click=btn_click)
    page.add(
        ft.Column([
            ft.Row([txt_name], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([txt_price], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([btn], alignment=ft.MainAxisAlignment.CENTER)
        ])
    )
ft.app(main)