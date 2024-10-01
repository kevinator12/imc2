import flet as ft
from flet_core.elevated_button import ElevatedButton


def reproducir1(txt1,labresul):
    try:
        txt1=float(txt1.value.strip())
        labresul.value=f"reproducir: {reproducir}"
    except ValueError:
        labresul.value="error"

def reproducir2(txt1,labresul):
    try:
        txt1=float(txt1.value.strip())
        labresul.value=f"reproducir: {reproducir}"
    except ValueError:
        labresul.value="error"
        
def reproducir2(txt1,labresul):
    try:
        txt1=float(txt1.value.strip())
        labresul.value=f"reproducir: {reproducir}"
    except ValueError:
        labresul.value="error"
        
def reproducir2(txt1,labresul):
    try:
        txt1=float(txt1.value.strip())
        labresul.value=f"reproducir: {reproducir}"
    except ValueError:
        labresul.value="error"


def main(page: ft.Page):
    page.title="ABP (HISTORIA UNIVERSAL)"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.bgcolor="blue"
    
    txt1=ft.Text("¿QUE HISTORIA QUIERES OIR?")
    
    labresul=ft.Text("PON ATENCION:")
    
    
    def limpiar(e):
        txt1.value=""
        labresul.value="reproducir"
        page.update()
    
    
    btn1=ElevatedButton("(BOMBARDEO DE HIROSHIMA Y NIAGASAKI)")
    btn2=ElevatedButton("(CAIDA DEL IMPERI ROMANO)")
    btn3=ElevatedButton("(11 DE SEPTIEMBRE)")
    btn4=ElevatedButton("(SEGUNDA GUERRA MUNDIAL)")
    
    page.add(
        ft.Row([txt1],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([labresul],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([btn1,btn2,btn3,btn4],alignment=ft.MainAxisAlignment.CENTER)
    )



ft.app(target=main,view=ft.AppView.WEB_BROWSER)
