from tkinter import *
from tkinter import messagebox
root = Tk()

def display():
    messagebox.showinfo("Info","Show info")
    messagebox.showwarning("Info","Show Warning")
    messagebox.showerror("Info","Show Error")
    okcancel = messagebox.askokcancel("Alerta","Ok ou Cancelar")
    print(okcancel)
    yesno = messagebox.askyesno("Dialogo","Responda sim ou não")
    print(yesno)
    retrycalcel = messagebox.askretrycancel("Dialogo","Informe sua resposta")
    print(retrycalcel)
    answer = messagebox.askquestion("Dialogo"," Ask question")
b1 = Button(root, text="Exibir Dialogos", command=display)
b1.pack()


root.mainloop()