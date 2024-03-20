import flet as ft
import modal as dm

def main(page: ft.Page):
    page.title = "Vc me ama?"
    page.window_width = 600
    page.window_heigth = 600
    page.window_resizable = False
    page.padding = 100
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = 'light'
    page.bgcolor = '#FF90BC'
    page.update()

    text = ft.Text(
        "Clique no coração <3",
        size=20,
        color=ft.colors.BLACK,
        weight=ft.FontWeight.BOLD,
        font_family="Montserrat"
    )
    
    def close_dlg(e):
        dm.open = False
        page.update()

    def open_dlg(e):
        dlg.visible = True

    #def open_dlg_main(e):
    #    dlg_bm.visible = True
#
    #dlg_bm = ft.Dialog(
    #    title="Bom mesmo!!!",
    #    modal=True
    #)

    def open_dlg_modal(e):
        page.dialog = dm
        dm.open = True
        page.update()
    dlg = ft.AlertDialog(
        title=ft.Text("Escolha novamente!")
    )
    def open_dlg_main(e):
        page.dialog = dlg
        dlg.open = True
        page.update()
    dm = ft.AlertDialog(
        modal=True,
        title=ft.Text("Diga sim ^^"),
        content=ft.Text("Você me ama? <3"),
        actions=[
            ft.TextButton("Sim", on_click=open_dlg_bm),
            ft.TextButton("Não", on_click=open_dlg),   
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )
 
    button = ft.IconButton(
        icon=ft.icons.FAVORITE, icon_color="red", on_click=open_dlg_modal,
    )
    page.add(text, button)
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
    