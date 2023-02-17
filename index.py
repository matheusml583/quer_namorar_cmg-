# IMPORTA A BIBLIOTECA TKINTER
from tkinter import *
from tkinter import ttk
from tkhtmlview import HTMLLabel

# IMPORTA A BIBLIOTECA RANDOM
import random

# INSTANCIA UM OBJ DA CLASSE "Tk()"
root = Tk()

# APLICXAÇÃO EM TELA CHEIA
root.attributes('-fullscreen', True)

# BOTÃO FECHAR PROGRAMA
close_button = ttk.Button(root, text="X", command=root.destroy)

# Define o tamanho e a posição do botão de fechar
close_button.place(relx=1, rely=0, anchor=NE, width=30, height=30)

# CRIA UM BUTTON E ATRIBUI ELE A UMA VARIÁVEL
btn_no = Button(root, text="NÂO!")
btn_yes = Button(root, text="SIM!")

comemoracao_div = HTMLLabel(root)
comemoracao_div.set_html('<div style="background-color: white; color: black; font-size: 24px; text-align: center; padding: 10px; height: 100vmin; width:100vmax;">CORRETA RESPOSTA!</div>')

# DEFINE UMA FUNÇÃO PARA MOVER O BOTÃO QUANDO O MOUSE PASSA POR CIMA
def move_button(event, button):
    x, y = event.x, event.y
    bx, by = button.winfo_x(), button.winfo_y()
    dx, dy = bx - x, by - y
    distance = (dx**2 + dy**2) ** 0.5
    dx, dy = dx / distance, dy / distance
    new_x, new_y = bx + dx *10, by + dy *10
    width, height = root.winfo_width(), root.winfo_height()
    new_x, new_y = random.randint(0, width), random.randint(0, height)
    button.place(x=new_x, y =new_y)

# DEFINE UMA FUNÇÃO PARA EXIBIR A DIV DE COMEMORAÇÃO
def show_comemoracao():
    comemoracao_div.place(relx=0.5, rely=0.5, anchor=CENTER)
    # destrói a div após 3 segundos
    root.after(10000, lambda: comemoracao_div.place_forget())

# ADICIONA UM BIN AO BOTÃO PARA CHAMAR A FUNÇÃO `move_button` QUANDO O MOUSE PASSAE POR CIMA
btn_no.bind("<Motion>", lambda event: move_button(event, btn_no))

# ADICIONA UM BIND AO BOTÃO "SIM!" PARA CHAMAR A FUNÇÃO `show_comemoracao` QUANDO O BOTÃO É CLICADO
btn_yes.config(command=show_comemoracao)

# POSICIONE OS BOTOES INICIALMENTE NO CENTRO DA TELA
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
btn_no.place(x=(screen_width - btn_no.winfo_reqwidth()) // 2 +50, y=(screen_height - btn_no.winfo_reqheight()) // 2)
btn_yes.place(x=(screen_width - btn_yes.winfo_reqwidth()) // 2 -50, y=(screen_height - btn_yes.winfo_reqheight()) // 2)

# ADICIONA UM LABEL
text_label = Label(root, text="QUER NAMORAR CMG?")
text_label.place(relx=0.5, rely=0.4, anchor=CENTER)

# CHAMA O MÉTODO `mainloop()` PARA INICIAR O LOOP PRINCIPAL DA APLICAÇÃO
root.title("Markzada")
root.mainloop()