from tkinter import *
from tkinter import  ttk
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
root.minsize(450,350)
root.maxsize(600,500)
#tela transparente
root.attributes('-alpha',8)

""""
frame1.grid(column=0, row=1, columnspan=1, ipadx=50, ipady=50,
            padx=10, pady=10)

frame2.grid(column=0, row=2, columnspan=1, ipadx=50, ipady=50,
            padx=10, pady=10)"""
"""
frame1.place(x=5, y=5, width=490, height=192)
frame2.place(x=5, y=203, width=490, height=190)
"""

# relativo trabalha com porcentagem onde 1 é o maximo
frame1 =Frame(root)
frame1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.48)
bt1 = Button(frame1,text='Novo', bg='gray35',fg='white', font=('verdana',12,'bold'))
bt1.place(relx=0.05, rely=0.05, relwidth=0.15, relheight=0.15)

bt2 = Button(frame1,text='Alterar', bg='gray35',fg='white', font=('verdana',12,'bold'))
bt2.place(relx=0.21, rely=0.05, relwidth=0.15, relheight=0.15)

bt3 = Button(frame1,text='Apagar', bg='gray35',fg='white', font=('verdana',12,'bold'))
bt3.place(relx=0.37, rely=0.05, relwidth=0.15, relheight=0.15)

bt4 = Button(frame1,text='Buscar', bg='gray35',fg='white', font=('verdana',12,'bold'))
bt4.place(relx=0.53, rely=0.05, relwidth=0.15, relheight=0.15)

label1 = Label(frame1, text='Codigo', font=('verdana', 12, 'bold'))
label1.place(relx=0.05, rely=0.25, relwidth=0.15, relheight=0.2)
entry1 = Entry(frame1, font=('verdana', 12, 'bold'))
entry1.place(relx=0.2, rely=0.3, relwidth=0.15, relheight=0.1)


label2 = Label(frame1, text='Nome', font=('verdana', 12, 'bold'))
label2.place(relx=0.05, rely=0.45, relwidth=0.15, relheight=0.2)
entry2 = Entry(frame1, font=('verdana', 12, 'bold'))
entry2.place(relx=0.2, rely=0.5, relwidth=0.15, relheight=0.1)

label3 = Label(frame1, text='Telefone', font=('verdana', 12, 'bold'))
label3.place(relx=0.05, rely=0.65, relwidth=0.15, relheight=0.2)
entry3 = Entry(frame1, font=('verdana', 12, 'bold'))
entry3.place(relx=0.21, rely=0.7, relwidth=0.15, relheight=0.1)

frame2 =Frame(root)
frame2.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.48)

label1 = Label(frame1, text='Label1')
label2 = Label(frame2, text='Label2')

lista = ttk.Treeview(frame2, height=5, columns=('col0','col1','col2'))
lista.heading('#0',text='Código')
lista.heading('#1',text='Nome')
lista.heading('#2',text='Telefone')
lista.column('#0', width=95)
lista.column('#1', width=195)
lista.column('#2', width=195)
lista.place(relx=0.02,rely=0.1, relwidth=0.88, relheight=0.8)
barra = ttk.Scrollbar(frame2, orient='vertical')
barra.place(relx=0.91, rely=0.1, relwidth=0.06, relheight=0.8)
root.mainloop()