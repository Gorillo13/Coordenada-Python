from tkinter import *
from tkinter import ttk
import pyautogui as pa
import statistics
import re

def Coordenada():
    a = Modo.get()
    match a:
        case 1:
            if (not Parar.get()):
                posicao = pa.position()
                Resultado.set(f'X: {posicao.x}\nY: {posicao.y}')
                root.after(100, lambda: Coordenada())
            else:
                Parar.set(False)

def Modo_1():
    Modo.set(1)

def Modo_2():
    Modo.set(2)

def Validar(valor):
    if valor == '':
        return True
    return re.match('^[0-9]*$', valor) is not None and int(valor) <= 10

root = Tk()
root.title('Sla')

mainframe = ttk.Frame(root, padding='30 12 30 10', borderwidth=2, relief='sunken')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
Validar_wrapper = (root.register(Validar), '%P')

# Variáveis

Modo = IntVar()
Modo.set(1)
Titulo = StringVar()
Titulo.set('Coordenada')
Texto = StringVar()
Texto.set('Texto')
Resultado = StringVar()
Parar = BooleanVar()
Parar.set(False)
Qtd_Coord = IntVar()

# Caixas de Texto

ttk.Label(mainframe, textvariable=Titulo).grid(column=1, row=0, sticky=(N, W, E, S))
ttk.Label(mainframe, textvariable=Texto).grid(column=0, row=1, sticky=(N, W, E, S))
ttk.Label(mainframe, textvariable=Resultado).grid(column=1, row=3)

# Caixas de Entrada

ttk.Entry(mainframe, textvariable=Qtd_Coord, validate='key', validatecommand=Validar_wrapper).grid(column=2, row=3)

# Botões

ttk.Button(mainframe, text='Modo 1', command=Modo_1).grid(column=0, row=2)
ttk.Button(mainframe, text='Modo 2', command=Modo_2).grid(column=2, row=2)
ttk.Button(mainframe, text='Iniciar', command=lambda: Coordenada()).grid(column=0, row=4)
ttk.Button(mainframe, text='Parar', command=lambda: Parar.set(True)).grid(column=2, row=4)

root.mainloop()