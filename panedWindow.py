from tkinter import *
from tkinter import Tk

root = Tk()
root.title("Pained Window")
root.geometry("500x400")

painel1 = PanedWindow(bd=4, relief='raised', bg='red')
painel1.pack(fill=BOTH, expand=1)

left_label = Label(painel1, text='Painel Esquerdo')
painel1.add(left_label)

painel2 = PanedWindow(painel1, orient=VERTICAL, bd=4, relief='raised', bg='red')
painel1.add(painel2)

top = Label(painel2, text="Top")
painel2.add(top)

bottom = Label(painel2, text="Bottom")
painel2.add(bottom)
root.mainloop()