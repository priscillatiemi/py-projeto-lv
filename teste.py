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
    image = ft.Image(
        width=200,
        height=200
    )
    def close_dlg(e):
        dm.open = False

    def open_dlg(e):
        dm.open = True

    def open_dlg_bm(e):
        page.dialog = dm
        dm.open = True
        page.update()
    dlg_bm = ft.AlertDialog(
        title="Bom mesmo!!!"
        )

    dlg = ft.AlertDialog(
        title="Escolha novamente!"
    )

    dm = ft.AlertDialog(
        "Você me ama? <3"
    )
    dlg_bt_sim = ft.TextButton(text="Sim", on_click=open_dlg_bm)
    dlg_bt_nao = ft.TextButton(text="Não", on_click=close_dlg)
    
    dlg.content = dm

    button = ft.TextButton(text="Abrir Diálogo", on_click=open_dlg)
    page.add(text, image, button, dlg, dlg_bm, dlg_bt_sim, dlg_bt_nao)
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
