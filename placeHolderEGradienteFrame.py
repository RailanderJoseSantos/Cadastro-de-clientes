from tkinter import *
from estiloWidgets.entryPlaceHolder import *
from estiloWidgets.gradienteFrame import *

root = Tk()
gradiente = GradientFrame(root,'gray','blue')
gradiente.pack()
holder = EntPlaceHold(root,'Digite o seu nome')
holder.place(x=10, y=10)
root.mainloop()
