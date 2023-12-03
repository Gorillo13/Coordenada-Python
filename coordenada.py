from tkinter import *
from tkinter import ttk
import pyautogui as pa
import time
import statistics

def coordenada(a):
    try:
        match a:
            case 1:
                posicao = pa.position()
                resultado.set(f'X: {posicao.x}\nY: {posicao.y}')
                root.after(100, lambda: coordenada(modo))
    except ValueError:
        resultado.set('erro')

def modo1():
    global modo
    modo = 1

def modo2():
    global modo
    modo = 2

root = Tk()
root.title('Sla')

mainframe = ttk.Frame(root, padding='30 12 30 10', borderwidth=2, relief='sunken')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Variáveis

modo = 1
titulo = StringVar()
titulo.set('Coordenada')
texto = StringVar()
texto.set('Texto')
resultado = StringVar()
cancelar = BooleanVar()
cancelar.set(False)

# Caixas de Texto

ttk.Label(mainframe, textvariable=titulo).grid(column=1, row=0, sticky=(N, W, E, S))
ttk.Label(mainframe, textvariable=texto).grid(column=0, row=1, sticky=(N, W, E, S))
ttk.Label(mainframe, textvariable=resultado).grid(column=1, row=3)

# Botões

ttk.Button(mainframe, text='Modo 1', command=modo1).grid(column=0, row=2)
ttk.Button(mainframe, text='Modo 2', command=modo2).grid(column=2, row=2)
ttk.Button(mainframe, text='Iniciar', command=lambda: coordenada(modo)).grid(column=0, row=4)
ttk.Button(mainframe, text='Cancelar', command=lambda: cancelar.set(True)).grid(column=2, row=4)

root.mainloop()