import flet as ft
import subprocess


def main(page: ft.Page):

    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER



    button1 = ft.ElevatedButton('FirstApp',on_click=subprocess.run(["python", 'C:\\Users\\vectra\\Desktop\\Vectra\\sheet_vizApps_SDK\\appsStore\\FirstApp\\main.py'])  ,style=ft.ButtonStyle(bgcolor=ft.colors.YELLOW, padding=20,
                                                                                              color=ft.colors.BLACK))
  
    button2 = ft.ElevatedButton('SecondApp', style=ft.ButtonStyle(bgcolor=ft.colors.LIGHT_GREEN_700, padding=20,
                                                                  color=ft.colors.BLACK))
    button3 = ft.ElevatedButton('CounterFlet', style=ft.ButtonStyle(bgcolor=ft.colors.LIGHT_BLUE, padding=20,
                                                                    color=ft.colors.BLACK))





    ButtonROW = ft.Row([button1, button2, button3], alignment=ft.MainAxisAlignment.CENTER)
    page.add(ButtonROW)


