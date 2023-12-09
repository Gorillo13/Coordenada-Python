from tkinter import *
from tkinter import ttk
from pygame import *
from pygame import mixer
from threading import Thread
import pyautogui as pa
import time
import statistics
import re

def Iniciar():
    Modo.set(1)
    Entrada.grid_remove()
    mixer.init()
    mixer.music.load(r'C:\Users\Tuane Santos\Desktop\Murilo\Coordenada\Bip.mp3')

def Contador():
    mixer.music.play()
    for i in range(5):
        time.sleep(1)
        i += 1

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
        case 2:
            b = Qtd_Coord.get()
            Pontos = []
            Lista = []
            while len(Pontos) < b:
                Thread1 = Thread(target=Contador)
                Thread1.start()
                while Thread1.is_alive():
                    Lista.append(pa.position())
                    time.sleep(0.25)
                Moda = max(Lista, key=Lista.count)
                Pontos.append(Moda)
                while Moda in Lista:
                    Lista.remove(Moda)
            saida = '\n'.join(map(str, Pontos))
            Resultado.set(saida)

def Modo_1():
    Modo.set(1)
    Entrada.grid_remove()

def Modo_2():
    Modo.set(2)
    Entrada.grid()

def Validar(valor):
    if valor == '':
        return True
    return re.match('^[0-9]*$', valor) is not None and int(valor) <= 5

root = Tk()
root.title('Sla')

mainframe = ttk.Frame(root, padding='30 12 30 10', borderwidth=2, relief='sunken')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
Validar_wrapper = (root.register(Validar), '%P')

# Variáveis

Modo = IntVar()
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

Entrada = ttk.Entry(mainframe, textvariable=Qtd_Coord, validate='key', validatecommand=Validar_wrapper)
Entrada.grid(column=2, row=3)

# Botões

ttk.Button(mainframe, text='Modo 1', command=Modo_1).grid(column=0, row=2)
ttk.Button(mainframe, text='Modo 2', command=Modo_2).grid(column=2, row=2)
ttk.Button(mainframe, text='Iniciar', command=lambda: Coordenada()).grid(column=0, row=4)
ttk.Button(mainframe, text='Parar', command=lambda: Parar.set(True)).grid(column=2, row=4)

root.after_idle(Iniciar)

root.mainloop()