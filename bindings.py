from tkinter import *
from tkinter import ttk
#APENAS PARA APRENDIZADO
root = Tk()
l = ttk.Label(root, text="Inicial")
l.grid()
l.bind('<Enter>', lambda e: l.configure(text="Mouse entrou"))
l.bind('<Leave>', lambda e: l.configure(text="Mouse saiu"))
l.bind('<1>', lambda e: l.configure(text="Botão esquerdo clicado"))
l.bind('<Double-1>', lambda e: l.configure(text="Duplo clique"))
l.bind("<B3-Motion>", lambda e: l.configure(text="Posição do mouse: %d,%d"%
                                                 (e.x, e.y)))

root.mainloop()