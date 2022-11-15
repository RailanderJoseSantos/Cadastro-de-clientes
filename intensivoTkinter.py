from tkinter import *
root = Tk()
""" PACK
#geometry: x, y tamanho, e x,y onde a janela aparecera
root.geometry('500x400+0+0')
root.title('Titulo janela')
root.configure(background='gray40')
root.resizable(False, False)
#frame - button - label - entry
#coloca o frame na tela
frame1 = Frame(root)
#posicionar elemento: pack/grid/place
frame1.pack(side=TOP, ipadx=210, ipady=90, padx=10, pady=10)
frame2 = Frame(root)
frame2.pack(side=BOTTOM,)
label1 = Label(frame1, text='Label1')
label1.pack()
label2 = Label(frame2, text='Label2')
label2.pack()"""


#GRID - TIPO PLANILHAS COM LINHAS E COLUNAS
root.geometry('500x400+0+0')
root.title('Titulo janela')
root.configure(background='gray40')
root.resizable(True, True)
frame1 =Frame(root)
frame2 =Frame(root)
label1 = Label(frame1, text='Label1')
label2 = Label(frame2, text='Label2')

frame1.grid(column=0, row=1, columnspan=1, ipadx=50, ipady=50,
            padx=10, pady=10)
""""
frame2.grid(column=0, row=2, columnspan=1, ipadx=50, ipady=50,
            padx=10, pady=10)"""
"""
frame1.place(x=5, y=5, width=490, height=192)
frame2.place(x=5, y=203, width=490, height=190)
"""

# relativo trabalha com porcentagem onde 1 é o maximo

frame1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.48)
frame2.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.48)

root.mainloop()