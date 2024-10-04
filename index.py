from pywebio import *
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server

    
class main_aplication():
    def __init__(self, logo) -> None:
        self.logo = logo
        
    def index(self):
        put_row([

            put_image(open("images/images.png", "rb").read()).style("position:relative; right: -200px"),
            #put_button("Iniciar sesión", onclick=None).style("margin-left: auto;")        
            ])
        
        put_html("<hr>")
        put_text("Sistema gestor farmaceutico").style("font-family: italic; text-align:center; font-size:30px")
        put_html("<hr>")
        put_row([
            put_button("Facturar", onclick=None).style("text-align: center; border-radius: 10%;"), None,
            put_button("productos", onclick=None).style("text-align: center;"), None,
            put_button("Promociones", onclick=None).style("text-align: center;")
        ]) 


aplication = main_aplication("images/images.png")

if __name__ == "__main__":
    start_server(aplication.index(), port=8000, debug=True)