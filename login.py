from tkinter import *
import base64
from subprocess import run
from sistema import Aplicacao as sistema
janela = Tk()
class Funcs():

        
class Login(Funcs):
    def __init__(self):
        self.janela = janela
        self.tela()
        # necessario looping pra manter janela aberta
        janela.mainloop()

    def tela(self):
        """Config da tela"""
        self.images_base64()
        self.janela.title("Login")
        self.janela.configure(background='#b3b3b3')
        self.janela.geometry("330x400")
        self.janela.resizable(False, False)
        self.janela.maxsize(width=330, height=400)
        self.janela.minsize(width=300, height=400)

        #img user padrão
        self.imgUser = PhotoImage(file="imagens/login5.png")
        self.imgUser = self.imgUser.subsample(2,2)
        lblUserImg = Label(janela, image=self.imgUser, bg='#b3b3b3')
        lblUserImg.place(relx=0.25, rely=0.1)
        """
        self.moldura_bt = Canvas(self.janela, bd=1, bg='#0bc90b', highlightbackground='#108ecb',
                                 highlightthickness=2)
        self.moldura_bt.place(relx=0.46, rely=0.859, relwidth=0.2,  relheight=0.1)"""
        self.bt_logar = Button(text="Logar", bd=9, bg='#12c9c1',
                                activebackground='#108ecb', activeforeground='white',
                                fg='white', font=('verdana', '8', 'bold'),command=self.logar)
        self.bt_logar.place(relx=0.41, rely=0.86, relwidth=0.25, relheight=0.1)

        self.lbl_usuario = Label(self.janela, text="Usuário:", bg='#b3b3b3', fg='white',font=('verdana', '10', 'bold'))
        self.lbl_usuario.place(relx=0.02, rely=0.633)

        self.usuario_entry = Entry(self.janela)
        self.usuario_entry.place(relx=0.25, rely=0.635, relwidth=0.58)


        self.lbl_senha = Label(self.janela, text="Senha:", bg='#b3b3b3', fg='white', font=('verdana', '10', 'bold'))
        self.lbl_senha.place(relx=0.02, rely=0.743)
        self.senha_entry = Entry(self.janela, show="*")
        self.senha_entry.place(relx=0.25, rely=0.740, relwidth=0.58)

def logar(self):
    if self.usuario_entry.get() =="Railander" and self.senha_entry.get()=="123":
        sistema.jane
Login()


